#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: No_12_string_path_matrix.py
# Created Date: 2018-09-13 01:39:31
# Author: canalStar
# -----
# Last Modified: 2018-09-13 01:44:11
# Last Modified By: canalStar
###

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        """ hasPath()函数判断在矩阵中是否存在该路径
            Input: matrix:输入矩阵，判断字符串是否在其中
            rows,cols:输入矩阵的行数，列数
            path:用于判断的字符串
            Output: 若存在路径则：true
                    若不存在路径：false
        """