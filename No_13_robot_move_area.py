#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: No_13_robot_move_area.py
# Created Date: 2018-09-14 01:30:59
# Author: canalStar
# -----
# Last Modified: 2018-09-14 02:48:40
# Last Modified By: canalStar
###

"""问题描述：(来源及参考：牛客网(www.nowcoder.com)，《剑指Offer(第二版）》)
    地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
    但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），
    因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
    解析： 
        输入:行列坐标数位之和k，方格大小m,n
        输出：机器人可以到达的格子数目
    考察回溯法
"""
class Solution:
    def movingCount(self, threshold, rows, cols):
        """ 输入：行列坐标和阈值，方格行数，列数
            输出：机器人可达坐标总数
        """
        if threshold < 0 or rows <= 0 or cols <= 0:
            return 0
        #初始化位置及标记矩阵
        visited = [False] * rows * cols
        row = 0
        col = 0
        #返回可达位置总数
        return self.moving_count_core(threshold, rows, cols, row, col, visited)

    def moving_count_core(self, threshold, rows, cols, row, col, visited):
        """ 输入：阈值，总行/列数，当前所处行/列数，标记当前位置是否被访问过的矩阵
            输出：遍历的点的数目
        """
        #初始化计数为0
        count = 0
        #检查该点是否满足条件
        if self.check(threshold, rows, cols, row, col, visited):
            #若满足条件，该点visited标记置为True
            visited[row * cols + col] = True
            #计数值等于该点的计数1及其上下左右符合要求的位置计数值
            count =( 1 + self.moving_count_core(threshold, rows, cols, row -1, col, visited)
                    + self.moving_count_core(threshold, rows, cols, row, col -1, visited)
                    + self.moving_count_core(threshold, rows, cols, row + 1, col, visited)
                    + self.moving_count_core(threshold, rows, cols, row, col + 1, visited))
        #返回路径
        if count > 0:
            print("row: %d, col: %d"%(row, col))
        #返回计数值
        return count

    def check(self, threshold, rows, cols, row, col, visited):
        """ 输入：阈值，总行/列数，当前所处行/列数，标记当前位置是否被访问过的矩阵
            输出：当前位置满足要求：True，否则：False
        """
        check_ans = (row >= 0 and col >= 0 and row < rows and col < cols
                and self.get_digit_sum(row, col) <= threshold and
                not visited[row * cols + col])
        return check_ans

    def get_digit_sum(self, row, col):
        """ 输入：行数，列数
            输出：该行列各位数字之总和
        """
        sum = 0
        for num in [row, col]:
            while num > 0:
                sum += num % 10
                num //= 10
        return sum

if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(3, 6, 5))