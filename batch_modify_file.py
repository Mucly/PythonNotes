#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2019/1/20
# 将basepath路径下的txt文本后缀改为rgb

import os

basepath = r"D:\tmp"
res_suffix = ".txt"
dst_suffix = ".rgb"
for file in os.listdir(basepath):
    head, tail = os.path.splitext(file)  # 分离文件名和文件后缀
    if tail == res_suffix:
        new_file = head + dst_suffix
        os.rename(os.path.join(basepath, file),
                  os.path.join(basepath, new_file))
