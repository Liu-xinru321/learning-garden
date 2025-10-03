#!/usr/bin/env python3
import sys, datetime, pathlib

def main():
    today = datetime.date.today()
    name = f"{today.year}-{today.month:02d}"
    md = f'''---
title: "月度复盘 {name}"
date: {today.isoformat()}
tags: [monthly]
---

## 🌟 本月三大收获
1. 
2. 
3. 

## 📈 指标墙
- Commits / PRs / 学习时长 / 复现实验数

## 🧩 失败与教训
-

## 🎯 下月目标（OKR）
- O1:
  - KR1:
  - KR2:
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
