#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: No_14_number_of _1.py
# Created Date: 2018-09-20 03:30:16
# Author: canalStar
# -----
# Last Modified: 2018-09-20 04:00:12
# Last Modified By: canalStar
###

class Solution:
    def number_of_1(self, bin_num):
        count = 0
        while(bin_num):
            bin_num = (bin_num - 1) & bin_num
            count += 1
        return count

if __name__ == '__main__':
    bin_num  = eval(input())
    S = Solution()
    print(S.number_of_1(bin_num))
