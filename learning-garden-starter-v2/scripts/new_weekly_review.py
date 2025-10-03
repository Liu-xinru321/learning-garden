#!/usr/bin/env python3
import sys, datetime, pathlib

def main():
    today = datetime.date.today()
    year, week, _ = today.isocalendar()
    name = f"{year}-W{week:02d}"
    md = f'''---
title: "周复盘 {name}"
date: {today.isoformat()}
tags: [weekly]
---

## ✅ 本周完成
-

## 📊 指标与成果
- 图表/模型卡/关键日志链接等

## 🧠 复盘与反思
-

## 🎯 下周目标（1–3 个）
-
'''
    p = pathlib.Path(f"docs/learning-log/{name}.md")
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        print(f"File exists: {p}")
        return
    p.write_text(md, encoding="utf-8")
    print(f"Created: {p}")

if __name__ == "__main__":
    main()
