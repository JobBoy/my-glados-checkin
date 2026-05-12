import urllib.request
import json
import os

# 获取环境变量中的 Cookie
cookie = os.environ.get("GLADOS_COOKIE")
if not cookie:
    print("❌ 错误: 未找到环境变量 GLADOS_COOKIE")
    exit(1)

# GLaDOS 签到接口
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
        
        if "message" in res_json:
            print(f"👉 最终状态: {res_json['message']}")
            
except Exception as e:
    print(f"❌ 签到请求失败: {e}")
    if hasattr(e, 'read'):
        print("详细报错:", e.read().decode('utf-8'))
    exit(1)
