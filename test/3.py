#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 11:08
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 3.py
n ,m = map(int,input().split(" "))
n = n / 100
dp = [0]
dp[0] = n / 2
i = 1
h = [0]
h[0] = n - dp[0]
# h[1] = h[0] + dp[1]

while dp[i-1] +n <= m:
    dp.append(dp[i-1]/2)


print(dp)
print(h)
print(len(h)+1)