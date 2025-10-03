# HOWTO: 把“修复包”应用到你的仓库（当前结构是嵌套子目录）

你的 MkDocs 项目在 `learning-garden-starter-v2/` 目录下。

## 1) 上传工作流（必做）
- 仓库网页 → Add file → Upload files
- 把本压缩包里的 `.github/workflows/pages.yml` 和 `ci.yml` 拖进去 → Commit 到 main。

## 2) 替换 mkdocs.yml（建议）
- 打开 `learning-garden-starter-v2/mkdocs.yml` → 用本包提供的同名文件内容**整体替换** → Commit。

## 3) 批量更新 title（可选）
- 把 `.github/tools/bulk_update_titles.py` 上传到仓库相同路径。
- 在 Codespaces 或你本地克隆后运行：
  ```bash
  python .github/tools/bulk_update_titles.py
  git add -A
  git commit -m "chore(docs): bulk update titles"
  git push
  ```

## 4) 开启 Pages（一次）
- Settings → Actions → General → Workflow permissions = Read and write permissions → Save
- Settings → Pages → Build & deployment = GitHub Actions

之后每次 `git push`，网站都会自动更新。