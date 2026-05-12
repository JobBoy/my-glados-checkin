# 🤖 GLaDOS 自动签到助手 (附 Bark 消息推送)

这是一个极简、稳定、无第三方依赖的 GLaDOS 自动签到脚本。部署在 GitHub Actions 上，每天自动运行，并通过 Bark 将中文翻译后的签到结果推送到你的 iPhone。

### ✨ 核心功能

* **🕒 定时触发**：每天北京时间早上 8:37 自动在云端签到（可在 `.yml` 中修改时间）。
* **🇨🇳 智能翻译**：自动将 GLaDOS 冰冷的英文返回值提取并翻译为带 Emoji 的中文。
* **📲 实时推送**：无缝对接 iOS 开发者最爱的 Bark，成功、重复、失败或失效都会弹窗通知。
* **🛡️ 纯净安全**：纯 Python 编写，不到 100 行代码，没有任何隐藏的流氓逻辑。

---

## 🛠️ 首次配置指南

只需要配置两个环境变量（Secrets），即可让脚本跑起来！

### 第一步：获取你的专属凭证

1. **获取 Cookie**：
* 在电脑浏览器登录 GLaDOS。
* 按 `F12` 打开开发者工具，点击 **网络 (Network)** 标签。
* 刷新网页，随便找一个名叫 `checkin` 或 `console` 的请求点开。
* 在请求头 (Request Headers) 里找到 `Cookie:`。
* **⚠️ 注意**：只复制 `koa:sess=` 开头的一大串字符，千万不要把前缀 `Cookie: ` 给复制进去了。


2. **获取 Bark Key**：
* 在 iPhone 上下载 [Bark App](https://apps.apple.com/us/app/bark-customed-notifications/id1403753865)。
* 打开 App，复制里面的那串乱码 Key（比如 `Vd9xxxxxxxxx`），不要复制完整的网址。



### 第二步：配置 GitHub Secrets

1. 在本仓库的顶部菜单点击 **Settings (设置)**。
2. 左侧边栏点击 **Secrets and variables** -> **Actions**。
3. 点击绿色的 **New repository secret** 按钮，分别添加以下两个密钥：
* 变量名 `GLADOS_COOKIE` 👉 填入你刚才复制的 Cookie。
* 变量名 `BARK_KEY` 👉 填入你的 Bark Key。



### 第三步：手动运行测试

1. 点击仓库顶部菜单的 **Actions**。
2. 左侧点击 **GLaDOS Checkin**。
3. 右侧点击灰色的 **Run workflow** 下拉按钮，再点一次绿色的 Run。
4. 几秒钟后，你的 iPhone 就会收到一条清脆的签到通知！这说明一切配置完美生效。

---

## 🔄 维护与 Cookie 更新教程

GLaDOS 的 Cookie 一般可以存活好几个月。如果某天你的手机收到报错通知：**“⚠️ 身份信息失效，请重新抓取 Cookie 更新！”**，请按以下步骤操作：

1. 重新在电脑上登录 GLaDOS，按 `F12` 抓取一段全新的 Cookie。
2. 回到本仓库的 **Settings** -> **Secrets and variables** -> **Actions**。
3. 找到 `GLADOS_COOKIE`，点击它右边的 ✏️ **铅笔图标**。
4. 粘贴新的 Cookie 覆盖旧的，点击 **Update secret** 保存。
5. 去 **Actions** 里手动点一次 `Run workflow` 跑通即可，它明天又会自动工作了。
