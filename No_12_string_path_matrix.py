#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: No_12_string_path_matrix.py
# Created Date: 2018-09-13 01:39:31
# Author: canalStar
# -----
# Last Modified: 2018-09-13 13:57:04
# Last Modified By: canalStar
###

"""题目介绍：(Source:https://github.com/zhedahht/CodingInterviewChinese2
                /blob/master/12_StringPathInMatrix/StringPathInMatrix.cpp)
    面试题12：矩阵中的路径
    题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有
    字符的路径。路径可以从矩阵中任意一格开始，每一步可以在矩阵中向左、右、
    上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入
    该格子。例如在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字
    母用下划线标出）。但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个
    字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
    A B T G
    C F C S
    J D E H

"""

class Solution:
    def has_path(self, matrix, rows, cols, path):
        """ hasPath()函数判断在矩阵中是否存在该路径（矩阵用数组模拟）
            Input: matrix:输入矩阵，判断字符串是否在其中
            rows,cols:输入矩阵的行数，列数
            path:用于判断的字符串
            Output: 若存在路径则：true
                    若不存在路径：false
        """
        #先判断矩阵、字符串的大小长度是否满足要求
        if matrix == None or rows < 1 or cols < 1 or not path.strip():
            return False
        #初始化标记变量，用于判断矩阵中某个位置是否被访问过
        visited = [0] * (rows * cols)
        path_length = 0
        for row in range(rows):
            for col in range(cols):
                label, path_length = self.has_path_core(matrix, rows, cols, row, col,
                                                        path, path_length, visited)
                if label:
                    return True
        #若没有遍历到，返回False
        return False
    def has_path_core(self, matrix, rows, cols, row, col, path, path_length, visited):
        """判断矩阵中当前的位置与字符串中是否匹配
            Input：matrix:用于判断的矩阵；rows，cols分别为该矩阵的行列数
                row，col用于定位要判断的点的位置，path是被比较的字符串
                path_length：是当前字符串中要比较的位置，visited:是标记某点是否被访问过的矩阵
            Output：label：bool，判断当前的矩阵中的点与字符串中是否匹配，
                    path_lenght:更新当前字符串的位置
                    注：visited矩阵是可变参数，会在过程中隐含自动更新
        """
        #若path_length已经超过字符串末尾，则表示已经匹配成功，返回True
        if path_length >= len(path):
            return True, path_length
        has_path = False
        pos = row * cols + col  #当前矩阵中的位置
        #若矩阵中的位置与字符串中的位置相同，且矩阵中位置没被访问过，则检查其周围的点是否匹配
        if(row >= 0 and col >= 0 and row < rows and col < cols and 
            (matrix[pos] == path[path_length]) and not visited[pos]):
            path_length += 1
            visited[pos] = True
            #检查其周围的点是否匹配
            return_tuple_l = self.has_path_core(matrix, rows, cols, row, col - 1, path,
                                     path_length, visited)
            return_tuple_r = self.has_path_core(matrix, rows, cols, row, col + 1, path,
                                     path_length, visited)
            return_tuple_u = self.has_path_core(matrix, rows, cols, row - 1, col, path,
                                     path_length, visited)
            return_tuple_d = self.has_path_core(matrix, rows, cols, row + 1, col, path,
                                     path_length, visited)
            has_path = return_tuple_l[0] or return_tuple_r[0] or \
                        return_tuple_u[0] or return_tuple_d[0]
            #若周围点都不匹配，则向上回溯
            if not has_path:
                path_length -= 1
                visited[pos] = False
        return has_path, path_length