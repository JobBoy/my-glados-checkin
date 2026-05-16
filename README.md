# 🤖 GLaDOS Auto Checkin (GLaDOS 自动签到助手)

![Python Version](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![GitHub Actions Status](https://img.shields.io/github/actions/workflow/status/JobBoy/my-glados-checkin/checkin.yml?label=Checkin%20Status) 

这是一个极简、稳定、无第三方依赖的 GLaDOS 自动签到脚本。依托 GitHub Actions 每天自动运行，并通过 Bark 实时推送签到结果。告别繁琐操作，一次配置，终身安心。

### ✨ 核心特性

* **🕒 定时触发**：每天自动在云端签到，完美避开拥堵高峰期（默认北京时间 08:37，可自定义）。
* **👥 多账号支持**：支持同时配置多个账号，一行一个，签到结果合并推送，告别消息轰炸。
* **🇨🇳 智能翻译**：自动提取 GLaDOS 冰冷的英文返回值，智能翻译为带 Emoji 的直观提示。
* **🌍 多语言配置**：支持简中、繁中及保留原生英文输出。
* **📲 实时推送**：无缝对接 iOS 开发者最爱的 Bark，成功、重复、失效随时掌控。
* **🛡️ 纯净安全**：纯 Python 编写，单文件不到 150 行代码，所有的敏感信息均通过 GitHub Secrets 隔离，安全透明。

---

## 🚀 快速开始 (Quick Start)

只需要简单的 3 步，即可拥有你专属的自动签到机器人。

### 第一步：Fork 本仓库
点击页面右上角的 **[Fork]** 按钮，将本仓库完整复制到你自己的 GitHub 账号下。**(注意：必须在你自己 Fork 后的仓库中进行后续操作！)**

### 第二步：获取必要凭证
1. **获取 Cookie**：
   * 电脑浏览器登录 GLaDOS 控制台。
   * 按 `F12` 打开开发者工具，点击 **网络 (Network)** 标签并刷新网页。
   * 找到名称为 `checkin` 或 `console` 的请求，在右侧 **请求头 (Request Headers)** 中找到 `Cookie:`。
   * ⚠️ **重要**：强烈建议完整复制，包含 `__stripe_mid=`、`koa:sess=` 以及防伪签名 `koa:sess.sig=` 等所有内容。不要包含前缀的 `Cookie: ` 字母。

2. **获取 Bark Key (仅限 iOS 用户)**：
   * 在 App Store 下载 [Bark](https://apps.apple.com/us/app/bark-customed-notifications/id1403753865)。
   * 打开 App，复制里面的那串核心密钥（例如 `Vd9xxxxxxxxx`，无需完整链接）。

### 第三步：配置 GitHub Secrets (最关键一步)
在你刚刚 Fork 的仓库顶部菜单点击 **Settings (设置)** -> 左侧边栏找到 **Secrets and variables** -> **Actions**。点击绿色的 **New repository secret** 按钮，添加以下变量：

| 变量名 (Secret Name) | 必填 | 描述与示例 |
| :--- | :---: | :--- |
| **`GLADOS_COOKIE`** | ✅ | 你的 Cookie。请参考下方“高级玩法”配置多账号。 |
| **`BARK_KEY`** | ❌ | 你的 Bark 推送密钥。如果不填则不发送手机通知。 |
| **`NOTIFY_LANG`** | ❌ | 推送语言设置。默认简中。填 `en` 保留英文，填 `zh-TW` 输出繁体。 |

### 第四步：激活并测试任务
1. 点击仓库顶部菜单的 **Actions** 标签页。
2. 可能会出现一个绿色的 `I understand my workflows, go ahead and enable them` 按钮，点击确认。
3. 在左侧菜单点击 **GLaDOS Checkin**。
4. 在右侧点击灰色的 **Run workflow** 按钮，再点击绿色的 Run 手动触发一次。
5. 等待 10 秒钟，如果你的 iPhone 收到了清脆的 Bark 提示音，恭喜！配置完美生效！🎉

---

## 👑 高级玩法

### 1. 多账号并发签到
如果你有多个账号，或者想帮家人一起代签，只需在配置 `GLADOS_COOKIE` 时，采用 **`账号名====Cookie`** 的格式，**按回车键换行**输入即可（一行一个账号）。

**输入示例：**
```text
我的主号====__stripe_mid=140...; koa:sess=eyJ1...; koa:sess.sig=3Cgo...
老婆的号====__stripe_mid=xyz...; koa:sess=abc...; koa:sess.sig=123...
测试小号====koa:sess=789...; koa:sess.sig=456...
