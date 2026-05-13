# 🤖 GLaDOS Auto Checkin (GLaDOS 自动签到助手)

![Python Version](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![GitHub Actions Status](https://img.shields.io/github/actions/workflow/status/YourUsername/YourRepoName/checkin.yml?label=Checkin%20Status) 
*(💡 提示：记得把上方徽章链接里的 YourUsername 和 YourRepoName 换成你自己的)*

这是一个极简、稳定、无第三方依赖的 GLaDOS 自动签到脚本。依托 GitHub Actions 每天自动运行，并通过 Bark 实时推送签到结果。告别繁琐操作，一次配置，终身安心。

### ✨ 核心特性

* **🕒 定时触发**：每天自动在云端签到，完美避开拥堵高峰期（默认北京时间 08:37，可自定义）。
* **🇨🇳 智能翻译**：自动提取 GLaDOS 冰冷的英文返回值，智能翻译为带 Emoji 的直观提示。
* **🌍 多语言支持**：支持简中、繁中及保留原生英文输出。
* **📲 实时推送**：无缝对接 iOS 开发者最爱的 Bark，成功、重复、失效随时掌控。
* **🛡️ 纯净安全**：纯 Python 编写，单文件不到 100 行代码，所有的敏感信息均通过 GitHub Secrets 隔离，安全透明。

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
   * ⚠️ **重要**：只复制 `koa:sess=` 开头的一大串字符，**不要**包含前缀的 `Cookie: ` 字母。

2. **获取 Bark Key (仅限 iOS 用户)**：
   * 在 App Store 下载 [Bark](https://apps.apple.com/us/app/bark-customed-notifications/id1403753865)。
   * 打开 App，复制里面的那串核心密钥（例如 `Vd9xxxxxxxxx`，无需完整链接）。

### 第三步：配置 GitHub Secrets (最关键一步)
在你刚刚 Fork 的仓库顶部菜单点击 **Settings (设置)** -> 左侧边栏找到 **Secrets and variables** -> **Actions**。点击绿色的 **New repository secret** 按钮，添加以下变量：

| 变量名 (Secret Name) | 必填 | 描述与示例 |
| :--- | :---: | :--- |
| **`GLADOS_COOKIE`** | ✅ | 你抓取到的 Cookie。例：`koa:sess=eyJh...` |
| **`BARK_KEY`** | ❌ | 你的 Bark 推送密钥。如果不填则不发送手机通知。例：`Vd9xxxxxxxxx` |
| **`NOTIFY_LANG`** | ❌ | 推送语言设置。默认简中。填 `en` 保留英文，填 `zh-TW` 输出繁体。 |

### 第四步：激活并测试任务
1. 点击仓库顶部菜单的 **Actions** 标签页。
2. 可能会出现一个绿色的 `I understand my workflows, go ahead and enable them` 按钮，点击确认。
3. 在左侧菜单点击 **GLaDOS Checkin**。
4. 在右侧点击灰色的 **Run workflow** 按钮，再点击绿色的 Run 手动触发一次。
5. 等待 10 秒钟，如果你的 iPhone 收到了清脆的 Bark 提示音，恭喜！配置完美生效！🎉

---

## 🔄 维护指南：如何更新 Cookie？

GLaDOS 的 Cookie 通常有效期为数月。如果你某天收到了 **“⚠️ 身份信息失效，请重新抓取 Cookie 更新！”** 的推送，请按以下步骤无痛恢复：

1. 重新在电脑上登录 GLaDOS，按 `F12` 抓取一段全新的 Cookie。
2. 回到本仓库的 **Settings** -> **Secrets and variables** -> **Actions**。
3. 找到原有的 `GLADOS_COOKIE`，点击它右边的 ✏️ **铅笔图标**。
4. 粘贴新的 Cookie 覆盖旧的，点击 **Update secret** 保存。
5. 去 **Actions** 里手动点一次 `Run workflow` 跑通即可，无需更改任何代码。

---

## 🛠️ 高级玩法

**修改自动签到时间：**
如果你想修改触发时间，可以直接编辑 `.github/workflows/checkin.yml` 文件。
找到 `cron: '37 0 * * *'` 这一行修改即可。（格式为 UTC 时间，即北京时间减去 8 小时。建议避开 00:00 整点高峰以防拥堵）。

---

## ⚠️ 免责声明 (Disclaimer)

* 本项目仅供编程学习与交流使用，旨在展示 Python 自动化请求及 GitHub Actions 的基础应用。
* 请勿滥用本脚本向目标服务器发送高频或恶意请求。
* 使用本脚本产生的一切后果由使用者自行承担，与项目作者无关。

## 📄 开源协议
本项目基于 [MIT License](LICENSE) 开源。欢迎大家提出 Issue，或提交 Pull Request 共同完善！
