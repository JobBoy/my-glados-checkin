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

def translate_msg(msg):
    """GLaDOS 专属中文翻译器（提取关键信息，转换为直观的中文）"""
    original = str(msg).lower()
    
    if "already" in original:
        return "您今天已经签到过了 😅"
    elif "get" in original and "point" in original:
        # 智能提取返回文本里的积分数字
        points = re.findall(r'\d+', original)
        p_str = points[0] if points else "?"
        return f"签到成功！获得 {p_str} 积分 🎉"
    elif "token" in original or "login" in original or "cookie" in original:
        return "身份信息失效，请重新抓取 Cookie 更新！ ⚠️"
    elif "tomorrow" in original:
        return "今天次数已用完，请明天再试 ⏳"
    else:
        # 如果 GLaDOS 出了什么新的没见过的提示，就返回原文
        return msg 

def main():
    cookie = os.environ.get("GLADOS_COOKIE")
    if not cookie:
        push_to_bark("GLaDOS 异常", "未找到 Cookie，请检查 GitHub Secrets！")
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
                
                # 调用我们的中文翻译函数
                cn_msg = translate_msg(original_msg)
                print(f"🇨🇳 翻译结果: {cn_msg}")
                
                push_to_bark("GLaDOS 每日签到", cn_msg)
            else:
                push_to_bark("GLaDOS 通知", "请求成功，但格式未知")
                
    except Exception as e:
        error_msg = str(e)
        if hasattr(e, 'read'):
            error_msg += " - " + e.read().decode('utf-8')
        print(f"❌ 签到失败: {error_msg}")
        push_to_bark("GLaDOS 签到失败", f"接口报错：{error_msg}")
        exit(1)

if __name__ == "__main__":
    main()
