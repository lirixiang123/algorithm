#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 14:05
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 66-hasPath.py
"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子
。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 例如


  矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符
  b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""
# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here