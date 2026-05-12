import urllib.request
import urllib.parse
import json
import os

def push_to_bark(title, content):
    """发送 Bark 推送的辅助函数"""
    bark_key = os.environ.get("BARK_KEY")
    if not bark_key:
        print("⚠️ 未配置 BARK_KEY，跳过推送")
        return
    
    # 对 URL 参数进行编码，防止中文或特殊字符导致请求失败
    safe_title = urllib.parse.quote(title)
    safe_content = urllib.parse.quote(content)
    url = f"https://api.day.app/{bark_key}/{safe_title}/{safe_content}"
    
    try:
        urllib.request.urlopen(url)
        print("📲 Bark 推送成功！")
    except Exception as e:
        print(f"❌ Bark 推送失败: {e}")

def main():
    # 获取环境变量
    cookie = os.environ.get("GLADOS_COOKIE")
    if not cookie:
        msg = "未找到环境变量 GLADOS_COOKIE，请检查 Secrets 配置！"
        print(f"❌ 错误: {msg}")
        push_to_bark("GLaDOS 签到异常", msg)
        exit(1)

    # GLaDOS 签到接口配置
    url = "https://glados.network/api/user/checkin"
    payload = b'{"token": "glados.one"}'
    headers = {
        "Cookie": cookie,
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Origin": "https://glados.network",
        "Referer": "https://glados.network/console/checkin"
    }

    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")

    try:
        print("⏳ 正在发送签到请求...")
        with urllib.request.urlopen(req) as response:
            res_data = response.read().decode("utf-8")
            res_json = json.loads(res_data)
            
            print("✅ 请求成功！返回数据：")
            print(json.dumps(res_json, indent=2, ensure_ascii=False))
            
            # 提取接口返回的核心提示信息
            if "message" in res_json:
                msg = res_json['message']
                print(f"👉 最终状态: {msg}")
                # 签到成功或重复签到，发送推送
                push_to_bark("GLaDOS 签到通知", msg)
            else:
                push_to_bark("GLaDOS 签到通知", "请求成功，但未解析到 message 字段")
                
    except Exception as e:
        error_msg = str(e)
        if hasattr(e, 'read'):
            error_msg += " - " + e.read().decode('utf-8')
            
        print(f"❌ 签到请求失败: {error_msg}")
        # 将报错信息推送到手机
        push_to_bark("GLaDOS 签到失败", f"网络或接口报错：{error_msg}")
        exit(1)

if __name__ == "__main__":
    main()
