# Learning Garden

一个用于**长期积累深度学习/AI for Science**学习内容的 GitHub 模板仓库：
- 使用 **MkDocs Material** 自动构建网站（GitHub Pages）
- `docs/learning-log/` 下**每日学习日志**（Markdown 模板）
- `docs/notes/` 下**系统化笔记**
- `notebooks/` 存放 Jupyter 笔记本（通过 `mkdocs-jupyter` 在线渲染）
- `.github/ISSUE_TEMPLATE/` 包含**每日/周/月学习 Issue 表单**（可在 Issues 中打卡）
- GitHub Actions：
  - `ci.yml`：在 PR 上**检查能否成功构建文档**
  - `pages.yml`：合并到 `main` 后**自动发布到 GitHub Pages**

## 快速开始
1. 在 GitHub 新建一个空仓库（或将此文件夹作为模板上传）。
2. 推送：
   ```bash
   git init
   git remote add origin <YOUR_REPO_URL>
   git add .
   git commit -m "init: learning garden scaffold"
   git branch -M main
   git push -u origin main
   ```
3. 打开仓库 **Settings → Actions → General**：Workflow permissions 选择 **Read and write permissions**；保存。
4. 打开仓库 **Settings → Pages**：将 **Build and deployment** 选择为 **GitHub Actions**。
5. 本地预览文档：
   ```bash
   pip install -r requirements.txt
   mkdocs serve  # 浏览器打开 http://127.0.0.1:8000
   ```

## 日志与发布
- 每天复制 `docs/learning-log/_TEMPLATE.md` 创建一份 `2025-10-03.md`，或直接在 **Issues** 用表单打卡，然后把要点同步到 `docs/learning-log/`。
- 推送到 `main` 分支后，GitHub Actions 会自动构建并更新你的学习网站。

## 目录结构
```
docs/
  index.md
  roadmap/30-day-plan.md
  syllabus/
  learning-log/
    _TEMPLATE.md
    2025-10-03.md
  notes/
  projects/
notebooks/
.github/
  ISSUE_TEMPLATE/
  workflows/
scripts/
```

## 许可证
默认 **MIT License**（见 `LICENSE`），可按需替换。

---

## GitHub 端到端实现方法（一步步）

### A. 创建仓库并启用 Pages
1. 在 GitHub 新建空仓库（建议命名 `learning-garden`）。
2. 本地执行：
   ```bash
   git init && git add .
   git commit -m "init: learning garden scaffold"
   git branch -M main
   git remote add origin <YOUR_REPO_URL>
   git push -u origin main
   ```
3. 打开 **Settings → Actions → General**：Workflow permissions 选择 **Read and write permissions**；保存。
4. 打开 **Settings → Pages**：**Build and deployment** 选择 **GitHub Actions**（已内置 `pages.yml` 工作流）。

### B. 每日到月度的记录方法
- **每日**：运行 `python scripts/new_daily_log.py` 生成当天日志，或在 Issues 用「📘 每日学习记录」表单打卡。
- **每周**：`python scripts/new_weekly_review.py` 生成 `YYYY-WW.md` 并总结本周要点。
- **每月**：`python scripts/new_monthly_review.py` 生成 `YYYY-MM.md`，用 OKR 方式计划下月。

### C. 课程/网站与笔记的组织
- 按照 `docs/syllabus/` 的纲要学习，对应在 `docs/notes/<课程代码>/` 建立主题笔记。
- 关键示例代码放在 `notebooks/` 或 `src/`，在日志中链接提交哈希。

### D. PR/分支与规范化
- 推荐 **分支命名**：`notes/<area>-<topic>`、`log/<date>`、`project/<name>`。
- **提交规范**（可选 Conventional Commits）：`feat: ...` / `docs: ...` / `chore: ...`。
- 每次学习完成后开一个小 PR，触发 `ci.yml` 构建检查，合并即自动发布网站。

### E. 进阶（可选）
- 在仓库 **Projects** 创建看板：To do / Doing / Done；把每日 Issue 拖拽管理。
- 打开 **Discussions** 用于问题归档与经验分享。
- 如需私密内容，可建一个私有仓库或在公开仓库中使用不暴露数据的要点式记录。
