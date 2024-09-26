# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 14:31:11 2024

@author: Chakraa
"""

# Scenario1

task_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]

robot_list = [[1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1]]

cost_matrix = [[ 0,  7,  7, 23, 20, 27, 27,  6,  9, 27, 18, 15, 23, 29,  9, 13, 29, 21, 17, 19,  8, 20, 16, 27, 31, 15, 15, 13,  5, 14],
               [ 7,  0,  8, 18, 27, 15, 12, 13, 16, 17, 11, 13, 30, 20,  6, 14, 25, 28, 11, 19, 15, 13, 23, 17, 19, 15, 22, 15, 12, 21],
               [ 7,  8,  0, 26, 27, 20, 20, 13, 16, 25, 19,  8, 30, 16,  2,  6, 33, 28, 19, 15, 15, 21, 23, 23, 27, 22, 15, 20, 12, 14],
               [23, 18, 26,  0, 32, 19,  8, 18, 21, 10, 12, 14, 29, 12, 21, 16, 18, 11,  7,  8, 20, 14, 16, 29,  8,  8, 28, 12, 19, 26],
               [20, 27, 27, 32,  0, 22, 28, 18, 21, 39, 26, 27,  3, 21, 29, 28, 22,  9, 27, 31, 18, 28,  4,  7, 40, 30, 27,  9, 17, 28],
               [27, 15, 20, 19, 22,  0, 18, 28, 23, 10,  4,  6, 22,  7, 21,  8, 18, 23, 17, 12, 30,  6, 18, 18, 25,  8, 30, 20, 20, 26],
               [27, 12, 20,  8, 28, 18,  0, 12, 15, 18, 20, 19, 31, 20, 18, 21, 25, 19,  1, 16, 14, 22, 24, 29, 16, 16, 20, 19, 13, 21],
               [ 6, 13, 13, 18, 18, 28, 12,  0,  3, 21, 17,  9, 18, 23, 15, 11, 25, 17, 11, 15,  2, 16, 22, 22, 26, 21, 10,  7,  1, 11],
               [ 9, 16, 16, 21, 21, 23, 15,  3,  0, 24,  8,  6, 21, 20, 18,  8, 28, 20, 14, 18,  5, 10, 20,  6,  8, 12,  7,  4,  4,  8],
               [27, 17, 25, 10, 39, 10, 18, 21, 24,  0,  6,  8, 32, 17, 15, 10, 8, 21, 17,  2, 23,  8, 26, 23, 15, 10, 31, 19, 16, 28],
               [18, 11, 19, 12, 26,  4, 20, 17,  8,  6,  0,  2, 24, 11, 17,  4, 14, 23, 19,  8, 13,  2, 22, 14, 16,  4, 15, 12, 12, 16],
               [15, 13,  8, 14, 27,  6, 19,  9,  6,  8,  2,  0, 19, 13, 10,  2, 16, 25, 20, 10, 11,  4, 24, 12, 14,  6, 13, 10, 10, 14],
               [23, 30, 30, 29,  3, 22, 31, 18, 21, 32, 24, 19,  0, 24, 29, 21, 25, 12, 29, 27, 16, 23,  7,  4, 26, 25, 24,  6, 19, 25],
               [29, 20, 16, 12, 21,  7, 20, 23, 20, 17, 11, 13, 24,  0, 14, 15, 25, 23, 19, 19, 24, 13, 25, 25, 20, 15, 26, 23, 23, 27],
               [ 9,  6,  2, 21, 29, 21, 18, 15, 18, 15, 17, 10, 29, 14,  0,  8, 23, 30, 17, 13, 17, 14, 25, 22, 24, 16, 17, 20, 14, 16],
               [13, 14,  6, 16, 28,  8, 21, 11,  8, 10,  4,  2, 21, 15,  8,  0, 18, 27, 22, 12, 13,  6, 26, 14, 16,  8, 15, 12, 12, 16],
               [29, 25, 33, 18, 22, 18, 25, 25, 28,  8, 14, 16, 25, 25, 23, 18, 0, 13, 24, 10, 27, 12, 18, 28, 23, 18, 29, 26, 24, 30],
               [21, 28, 28, 11,  9, 23, 19, 17, 20, 21, 23, 25, 12, 23, 30, 27, 13,  0, 18, 19, 16, 25,  5, 16, 19, 19, 27, 18, 16, 28],
               [17, 11, 19,  7, 27, 17,  1, 11, 14, 17, 19, 20, 29, 19, 17, 22, 24, 18,  0, 15, 13, 21, 23, 20, 15, 15, 21, 18, 12, 22],
               [19, 19, 15,  8, 31, 12, 16, 15, 18,  2,  8, 10, 27, 19, 13, 12, 10, 19, 15,  0, 17, 10, 24, 22, 16, 12, 23, 20, 14, 24],
               [ 8, 15, 15, 20, 18, 30, 14,  2,  5, 23, 13, 11, 16, 24, 17, 13, 27, 16, 13, 17,  0, 15, 21, 11, 13, 17, 12,  9,  3, 13],
               [20, 13, 21, 14, 28,  6, 22, 16, 10,  8,  2,  4, 23, 13, 14,  6, 12, 25, 21, 10, 15,  0, 24, 16, 18,  6, 17, 14, 14, 18],
               [16, 23, 23, 16,  4, 18, 24, 22, 20, 26, 22, 24,  7, 25, 25, 26, 18,  5, 23, 24, 21, 24,  0, 11, 20, 24, 27, 13, 21, 28],
               [27, 17, 23, 29,  7, 18, 29, 22,  6, 23, 14, 12,  4, 25, 22, 14, 28, 16, 20, 22, 11, 16, 11,  0,  6, 18, 13,  2, 10, 14],
               [31, 19, 27,  8, 40, 25, 16, 26,  8, 15, 16, 14, 26, 20, 24, 16, 23, 19, 15, 16, 13, 18, 20,  6,  0, 16, 15,  4, 12, 16],
               [15, 15, 22,  8, 30,  8, 16, 21, 12, 10,  4,  6, 25, 15, 16,  8, 18, 19, 15, 12, 17,  6, 24, 18, 16,  0, 19, 16, 16, 18],
               [15, 22, 15, 28, 27, 30, 20, 10,  7, 31, 15, 13, 24, 26, 17, 15, 29, 27, 21, 23, 12, 17, 27, 13, 15, 19,  0, 11, 11,  1],
               [13, 15, 20, 12,  9, 20, 19,  7,  4, 19, 12, 10,  6, 23, 20, 12, 26, 18, 18, 20,  9, 14, 13,  2,  4, 16, 11,  0,  8, 12],
               [ 5, 12, 12, 19, 17, 20, 13,  1,  4, 16, 12, 10, 19, 23, 14, 12, 24, 16, 12, 14,  3, 14, 21, 10, 12, 16, 11,  8,  0, 12],
               [14, 21, 14, 26, 28, 26, 21, 11,  8, 28, 16, 14, 25, 27, 16, 16, 30, 28, 22, 24, 13, 18, 28, 14, 16, 18,  1, 12, 12,  0]]