#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 14:54
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 47-Sum_Solution.py
"""
求1+2+3+...+n，要求不能使用乘除法、
for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""
# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n and n+self.Sum_Solution(n-1)