#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 23:12
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 15-ReverseList.py


"""
输入一个链表，反转链表后，输出新链表的表头。
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pre = None
        cur = pHead
        nex = None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre
