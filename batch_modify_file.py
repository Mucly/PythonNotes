#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2019/1/20

import os
import fnmatch


def changeSuffix(path, res_suffix, dst_suffix):
    '''
        将basepath路径下，所有后缀为res_suffix的文件，后缀改为dst_suffix
        后缀即文件的拓展名，即文件类型
    '''
    for file in os.listdir(path):
        head, tail = os.path.splitext(file)  # 分离文件名和文件后缀
        if tail == res_suffix:
            new_file = head + dst_suffix
            os.rename(os.path.join(path, file),
                      os.path.join(path, new_file))

if __name__ == '__main__':
    pass
    basepath = os.path.realpath('.')
    # changeSuffix(basepath, '.aaa', '.txt') # 将文件后缀为.aaa的文件，后缀改为.txt
