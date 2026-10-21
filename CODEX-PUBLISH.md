# 可以直接交给 Codex 的发布任务

请执行如下操作，执行前务必先检查远程仓库，避免覆盖其他项目：

```text
你是我的 GitHub 静态站发布工程师。工作目录是当前的 infj-high-salary-guide 文件夹。

目标：将这个完整项目发布到独立的新仓库 AIPMAndy/infj-high-salary-guide，并启用 GitHub Pages。原项目 AIPMAndy/intj-growth-guide 必须保持完全不变。

1. 确认用户当前 GitHub 登录账号和仓库权限，检查新仓库是否已存在。若不存在且已有 GitHub CLI 认证，可执行：
   gh repo create AIPMAndy/infj-high-salary-guide --public --source=. --remote=origin --push
   如果当前目录尚未初始化 Git，请先 git init、git add、git commit、git branch -M main，再按 CLI 的提示创建；不要提交令牌。
2. 若目标仓库已存在，先读取其默认分支和现有文件；不得使用 --force 推送，不得覆盖已有数据。仅在确认冲突处理方案后合并新内容。
3. 在本地检查 HTML/CSS/JS 语法与路径，运行：python3 -m unittest discover -s tests -v。检查 10 条职业路线、12 段话术、30 天任务、薪酬计算器；不得把演示场景冒充真实成功案例。
4. 提交所有文件，推送 main 分支。
5. 打开仓库 Settings -> Pages，把 Source 设置为 GitHub Actions。`.github/workflows/deploy-pages.yml` 已包含部署流水线。
6. 验证 Actions 流水线显示 success，打开 https://aipmandy.github.io/infj-high-salary-guide/，在桌面和移动端测试交互、导航、复制、计算器、任务保存 / 导出。
7. 若出现报错，先修复，再重新运行测试和部署；没有通过之前不得汇报“上线成功”。
8. 最终报告实际存在的 GitHub 仓库链接、已成功打开的网站链接、部署运行结果和剩余问题。

禁止改动 AIPMAndy/intj-growth-guide，禁止上传私密信息，禁止虚构流量、成交或薪资数据。
```

如果 Codex 无法访问 GitHub 页面配置，但已经能将内容推送，可按 [发布文档](docs/PUBLISH.md) 在浏览器里完成唯一需要的 Pages Source 选择操作。
