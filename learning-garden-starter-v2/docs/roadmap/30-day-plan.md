# 30 天路线图（深度学习 × 工程化 × 快速原型）

> 每天 2–4 小时；周末半天复盘。所有任务都在本仓库以**日志 + 笔记**留痕。

## 第 1 周｜打地基：从跑通到看懂
- [ ] 6.S191：总览 + 1–2 个 Lab（见《syllabus/6s191.md》）
- [ ] PyTorch 官方教程：Quickstart / DataLoader / 训练循环（见《syllabus/pytorch.md》）
- [ ] D2L：线性模型、优化、正则化（见《syllabus/d2l.md》）
- [ ] 建立代码脚手架 `src/`：`data.py`、`models.py`、`train.py`、`utils.py`
- [ ] 输出：1 篇“训练循环从零到可复用”的技术笔记（放在 `docs/notes/pytorch/`）

## 第 2 周｜现代网络与工程化
- [ ] Karpathy ZtH：micrograd（手写反向）→ minGPT（小语言模型）
- [ ] D2L：CNN / BN / Dropout / 学习率调度
- [ ] CS231n：任选一次作业并完成报告
- [ ] 输出：一个干净的训练脚本 + TensorBoard/CSV 日志 + 早停 + Warmup/Cosine

## 第 3 周｜Transformer 直觉 + 快速原型
- [ ] 6.S191/CS231n 中的 Attention/Transformer 讲次
- [ ] fast.ai：从零构建一个可复现实战（图像或文本）并做微调对比
- [ ] 输出：最小科研原型（数据→方法→实验→结论），形成 `projects/` 页面

## 第 4 周｜巩固 + 输出
- [ ] D2L：泛化/正则化/计算性能章节查漏补缺
- [ ] 整理模型卡与失败案例
- [ ] 写成 1 页汇报（Lightning Talk 5–8 分钟脚本）
