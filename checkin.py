import urllib.request
import urllib.parse
import json
import os
import re

def push_to_bark(title, content):
    """发送 Bark 推送"""
    bark_key = os.environ.get("BARK_KEY")
    if not bark_key:
        print("⚠️ 未配置 BARK_KEY，跳过推送")
        return
    
    safe_title = urllib.parse.quote(title)
    safe_content = urllib.parse.quote(content)
    url = f"https://api.day.app/{bark_key}/{safe_title}/{safe_content}"
    
    try:
        urllib.request.urlopen(url)
        print("📲 Bark 推送成功！")
    except Exception as e:
        print(f"❌ Bark 推送失败: {e}")

def translate_msg(msg, lang="zh-CN"):
    """GLaDOS 专属翻译器，支持指定语言"""
    # 如果指定了 en (英文) 或 none，则直接返回原始信息不作翻译
    if lang.lower() in ["en", "none", "english"]:
        return msg

    original = str(msg).lower()
    
    if "already" in original:
        if lang == "zh-TW": return "您今天已經簽到過了 😅"
        return "您今天已经签到过了 😅"
    elif "get" in original and "point" in original:
        points = re.findall(r'\d+', original)
        p_str = points[0] if points else "?"
        if lang == "zh-TW": return f"簽到成功！獲得 {p_str} 積分 🎉"
        return f"签到成功！获得 {p_str} 积分 🎉"
    elif "token" in original or "login" in original or "cookie" in original:
        if lang == "zh-TW": return "身份信息失效，請重新抓取 Cookie 更新！ ⚠️"
        return "身份信息失效，请重新抓取 Cookie 更新！ ⚠️"
    elif "tomorrow" in original:
        if lang == "zh-TW": return "今天次數已用完，請明天再試 ⏳"
        return "今天次数已用完，请明天再试 ⏳"
    else:
        return msg 

def get_push_title(lang, is_error=False):
    """根据语言动态返回推送标题"""
    if lang.lower() in ["en", "none", "english"]:
        return "GLaDOS Error" if is_error else "GLaDOS Checkin"
    elif lang == "zh-TW":
        return "GLaDOS 異常" if is_error else "GLaDOS 每日簽到"
    else:
        return "GLaDOS 异常" if is_error else "GLaDOS 每日签到"

def main():
    # 获取语言配置，如果没填则默认 'zh-CN'
    notify_lang = os.environ.get("NOTIFY_LANG", "zh-CN")
    
    cookie = os.environ.get("GLADOS_COOKIE")
    if not cookie:
        err_title = get_push_title(notify_lang, is_error=True)
        push_to_bark(err_title, "未找到 Cookie，请检查 GitHub Secrets！")
        exit(1)

    url = "https://glados.network/api/user/checkin"
    payload = b'{"token": "glados.one"}'
    headers = {
        "Cookie": cookie,
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
        "Origin": "https://glados.network",
        "Referer": "https://glados.network/console/checkin"
    }

    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as response:
            res_json = json.loads(response.read().decode("utf-8"))
            
            if "message" in res_json:
                original_msg = res_json['message']
                print(f"👉 原始返回: {original_msg}")
                
                # 传入指定的语言进行翻译
                final_msg = translate_msg(original_msg, notify_lang)
                print(f"💬 最终推送内容: {final_msg}")
                
                push_title = get_push_title(notify_lang)
                push_to_bark(push_title, final_msg)
            else:
                push_title = get_push_title(notify_lang)
                push_to_bark(push_title, "请求成功，但格式未知 / Request success, unknown format")
                
    except Exception as e:
        error_msg = str(e)
        if hasattr(e, 'read'):
            error_msg += " - " + e.read().decode('utf-8')
        print(f"❌ 签到失败: {error_msg}")
        
        err_title = get_push_title(notify_lang, is_error=True)
        push_to_bark(err_title, f"接口报错 / API Error：{error_msg}")
        exit(1)

if __name__ == "__main__":
    main()
