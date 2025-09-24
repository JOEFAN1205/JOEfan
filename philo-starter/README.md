# PhiloHub Starter

这是一个**零后端静态网站**起步包，包含：`index.html`、`lesson.html`。你可以直接在本地双击打开，也可以部署到 Vercel / Netlify / GitHub Pages。

## 本地预览
直接双击 `index.html` 打开。

## 快速发布到 Vercel
1. 新建 GitHub 仓库并推送本项目文件。
2. 打开 https://vercel.com ，选择 `New Project` → 导入 GitHub 仓库。
3. 构建设置：Framework 选择 `Other`（静态），保持默认。
4. 部署完成后，会得到一个 `*.vercel.app` 预览域名。

### 绑定自定义域名（推荐直接在 Vercel 购买域名以免手动配置）
- 方案 A：在 Vercel 内购买域名 → 自动完成 DNS 和 HTTPS。
- 方案 B：在任意注册商购买域名（如 Namecheap / Porkbun / Hover / Squarespace Domains），在 Vercel 的 `Domains` 页面添加你的域名，它会提示你：
  - 要么把域名的 **Nameservers** 改成 Vercel 提供的 NS（推荐，省心）。
  - 要么保留注册商的 DNS，在注册商处添加 Vercel 提示的 **A/CNAME** 记录。

## 发布到 Netlify（可选）
1. 打开 https://app.netlify.com/ → `New site from Git` → 连接 GitHub 仓库。
2. Build 命令留空，Publish 目录选择根目录或 `/`。
3. 部署后获得 `*.netlify.app` 预览域名。
4. 在 `Domain management` 里添加你的自定义域名，根据向导配置 Nameservers 或 DNS 记录。

## GitHub Pages（可选）
1. 将本项目推送到 GitHub。
2. 进入仓库 `Settings` → `Pages`，选择 `Deploy from a branch`，分支选 `main`，目录 `/root`。
3. 保存后会得到 `https://<username>.github.io/<repo>`。
4. 自定义域名：在注册商添加 CNAME `www` 指向 `username.github.io`，并在仓库 Pages 设置里填写你的域名。

## 内容结构
- 修改 `index.html` 的首页模块卡片链接即可接入更多课程页。
- 新增页面：复制 `lesson.html` 另存为，如 `truth.html`。

## 可访问性小清单
- 所有图片加 alt；所有交互有键盘焦点；色彩对比 ≥ 4.5:1。

祝发布顺利！
