#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 10:50
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : q.py



for x in range(10):
    for y in range(10):
        for z in range(10):
            a = 100 * x + 10 * y + z
            b = 100 * z + 10 * y + x
            if a * 693 == b * 396:
                print(a,b)