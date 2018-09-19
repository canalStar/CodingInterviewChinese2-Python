#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: No_14_cutting_rope.py
# Created Date: 2018-09-15 02:04:27
# Author: canalStar
# -----
# Last Modified: 2018-09-20 03:17:41
# Last Modified By: canalStar
###

"""问题描述：（参考《剑指Offer(第二版）》(github.com/zhedahht/CodingInterviewChinese2/blob/master/)）
   题目：给你一根长度为n绳子，请把绳子剪成m段（m、n都是整数，n>1并且m≥1）。
   每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0]*k[1]*…*k[m]可能的最大乘
   积是多少？例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此
   时得到最大的乘积18。
   输入：n(绳子长度)
   输出：最大长度
"""
class Solution:
    def max_product_after_cutting_dp(self, length):
        """ 输入：length(int)-绳子长度
            输出：max length (int) -可以通过剪切得到的最大值
        """
        #最少要剪一次
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        # 创建存储数组，记忆子问题最优解
        products = [0] * (length + 1)
        products[0:4] = [0, 1, 2, 3]

        max = 0
        for i in range(4, length + 1):
            max = 0
            for j in range(i//2 + 1):
                product = products[j] * products[i - j]
                if max < product:
                    max = product
            products[i] = max
        return products[-1]

if __name__ == '__main__':
    #length = list(map(int, input().split()))[0]
    length = eval(input())  #eval()函数将输入直接转化为对应类型
    S = Solution()
    max_product = S.max_product_after_cutting_dp(length)
    print(max_product)