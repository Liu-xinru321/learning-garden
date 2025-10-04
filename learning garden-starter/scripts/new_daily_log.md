#!/usr/bin/env python3
import sys, datetime, pathlib

def main():
    date = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
    title = f"学习日志 {date}"
    md = f'''---
title: "{title}"
date: {date}
tags: [daily]
hours: 
---

## 🎯 今日目标
-

## 📚 输入资源（课程/论文/代码）
-

## 🛠️ 实践（代码/实验）
-

## 📈 结果与指标
-

## 🤔 反思/问题清单
-

## 🗓️ 明日计划
-
'''
    p = pathlib.Path(f"docs/learning-log/{date}.md")
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        print(f"File exists: {p}")
        return
    p.write_text(md, encoding="utf-8")
    print(f"Created: {p}")

if __name__ == "__main__":
    main()
