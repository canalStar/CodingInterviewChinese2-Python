#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: No17_print1_to_max_N_digits.py
# Created Date: 2018-09-22 13:55:22
# Author: canalStar
# -----
# Last Modified: 2018-09-22 15:26:02
# Last Modified By: canalStar
###

""" 剑指Offer 17.打印从1到最大的n位数
    例如：输入3，则打印出1，2，3 一直到最大的3位数999
"""

import sys

class Solution:

    def print_little_numbers(self, n):
        """打印从1到n位最大值在int范围内的数"""
        if n <= 0:
            return
        max_number = '9'*n
        max_number = int(max_number)
        for i in range(1,max_number):
            print(i, end = ',')
        print(max_number)

    def Print1ToMaxOfNDigits(self, n):
        if n <= 0:
            return
        num_list = ['0']*n
        for i in range(10):
            num_list[0] = chr(i + ord('0'))
            self.print_1_to_max_N_digits_recursively(num_list, n, 0)
        print()

    def print_1_to_max_N_digits_recursively(self, num_list, length, index):
        if index == length -1:
            self.print_number(num_list)
            return
        for i in range(10):
            num_list[index+1] = chr(i + ord('0'))
            self.print_1_to_max_N_digits_recursively(num_list, length, index+1)
    
    def print_number(self, num_list):
        is_beginning0 = True
        n_length = len(num_list)
        for i in range(n_length):
            if is_beginning0 and num_list[i] != '0':
                is_beginning0 = False
            if not is_beginning0:
                print(num_list[i], end='')
        if not is_beginning0 :
            print('',end=',')

if __name__ == '__main__':
    #输入为一个大于等于0的数字n
    n = int(input("请输处位数: "))
    if n <=0:
        print(0)
    else:
        #取得当前系统int型的最大值
        i = sys.maxsize
        #判断当前系统int型的最大值，
        #若n的位数小于最大值的位数则采用小数（较小的数）输出即可
        S = Solution()
        if n < len(str(i)):
            S.print_little_numbers(n)
        else:
            S.Print1ToMaxOfNDigits(n)