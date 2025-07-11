#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os

# 输入和输出文件路径
input_file = "data/DPO_for_huccination.json"
output_file = "data/DPO_for_hallucination_clean.json"

# 读取原始数据
with open(input_file, 'r', encoding='utf-8') as f:
    raw_data = f.read()

# 解析成列表形式
raw_items = json.loads(raw_data)
cleaned_items = []

# 处理每个项目
for item in raw_items:
    # 移除每一项开头的```json\n和结尾的\n```
    clean_item = item.strip()
    if clean_item.startswith("```json\n"):
        clean_item = clean_item[8:]
    if clean_item.endswith("\n```"):
        clean_item = clean_item[:-4]
    
    # 解析为JSON对象
    try:
        json_item = json.loads(clean_item)
        cleaned_items.append(json_item)
    except json.JSONDecodeError as e:
        print(f"解析错误: {e}")
        print(f"问题内容: {clean_item[:100]}...")

# 保存清理后的数据
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(cleaned_items, f, ensure_ascii=False, indent=2)

print(f"处理完成! 总共处理了 {len(cleaned_items)} 条数据")
print(f"清理后的文件保存在: {output_file}") 