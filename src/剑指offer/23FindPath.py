#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 15:41
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 23FindPath.py
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
"""
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        self.res = []
        if not root: return []
        self.subFindPath(root,[],expectNumber)
        return self.res


    def subFindPath(self,root,path,expectNumber):
        if root.left:
            self.subFindPath(root.left,path + [root.val],expectNumber-root.val)

        if root.right:
            self.subFindPath(root.right,path + [root.val],expectNumber-root.val)

        if not root.left and not root.right:
            if expectNumber == root.val:
                self.res.append(path + [root.val])
