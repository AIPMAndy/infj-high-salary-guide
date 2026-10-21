# 5 分钟部署到 GitHub Pages

## 一、创建独立仓库（不要覆盖 INTJ 仓库）

打开 https://github.com/new ，选择账户 `AIPMAndy`，仓库名填：`infj-high-salary-guide`，**Public**。如果用此代码包导入，创建时不要自动生成 README / .gitignore / LICENSE，避免初始提交冲突。

> 原 INTJ 项目 `intj-growth-guide` 保持不变。两个网站是同系列的独立仓库。

## 二、上传代码

下载本项目 ZIP 解压后，在本地终端运行：

```bash
cd infj-high-salary-guide
git init
git add .
git commit -m "feat: launch INFJ high salary career field guide"
git branch -M main
git remote add origin https://github.com/AIPMAndy/infj-high-salary-guide.git
git push -u origin main
```

如果本地已经有 git 仓库，跳过 `git init`，检查 `git remote -v`，**确保远程指向新仓库**。GitHub 认证请使用你自己的 Git Credential Manager、SSH 或 `gh auth login`；不要把令牌放在脚本或仓库中。

## 三、打开 Pages 部署

进入新仓库：

https://github.com/AIPMAndy/infj-high-salary-guide/settings/pages

在 `Build and deployment` 里把 **Source 选择 `GitHub Actions`**。仓库已经包含 `.github/workflows/deploy-pages.yml`，推送到 `main` 即可触发部署；如果此前推送时还未启用 Pages，可到 **Actions → Deploy GitHub Pages → Run workflow** 手动启动。

Actions 配置依据 GitHub 文档：[Configuring a publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)。

## 四、上线后核验

- 网站主页：`https://aipmandy.github.io/infj-high-salary-guide/`
- 仓库：`https://github.com/AIPMAndy/infj-high-salary-guide`
- 自动部署：`https://github.com/AIPMAndy/infj-high-salary-guide/actions/workflows/deploy-pages.yml`

1. 手机和电脑打开首页，检查文字排版与响应式布局。
2. 用导航打开职业路线、话术、总包计算器、30 天任务。
3. 筛选职业、复制话术、计算总包、勾选任务、刷新页面、导出清单。
4. 检查「查看咨询与陪跑服务」是否跳到 `https://metaver.vip/services`。
5. 查看 GitHub 代码文件与引用资料，确认链接可访问。

**404 常见原因**：新仓库没建立、还未成功部署、Pages Source 与 Action 模式不一致、入口 `index.html` 未位于项目根目录。GitHub Pages 的发布需要 Actions 运行成功之后才能算已上线。

## 五、后续维护

`data/content.js` 管理职业路线 / 话术 / 任务；`assets/site.css` 管理样式；`assets/site.js` 管理交互；`README.md` 和 `guides/` 是详细内容。修改并推送 main 后，自动部署将发布更新。上线前建议执行：

```bash
python3 -m unittest discover -s tests -v
python3 -m http.server 8000
```

访问本地 `http://localhost:8000` 手动测试。**不要把这个 ZIP 上传到现有的 INTJ 仓库根目录。**
