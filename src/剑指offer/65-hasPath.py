#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 14:05
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 65-hasPath.py
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
        if not matrix:
            return False
        if not path:
            return True
        x = [list(matrix[i*cols:i*cols+ cols]) for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if self.exist_helper(x, i, j, path):
                    return True
        return False

    def exist_helper(self, matrix, i, j, p):
        if matrix[i][j] == p[0]:
            if not p[1:]:return True
            matrix[i][j] = ''
            if i > 0 and self.exist_helper(matrix,i-1,j,p[1:]):return True
            if i < len(matrix) - 1 and  self.exist_helper(matrix,i+1,j,p[1:]):return True
            if j > 0 and self.exist_helper(matrix,i,j-1,p[1:]):return True
            if j < len(matrix[0]) - 1 and self.exist_helper(matrix,i,j+1,p[1:]):return True
            matrix[i][j] = p[0]
            return False




s =Solution()
s.hasPath("ABCESFCSADEE",3,4,"ABCB")