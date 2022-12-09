# Given an image represented by an N x N matrix, where each pixel in the image is represented by an integer
# Write a method to rotate the image by 90 degrees. Can you do it in place?

from typing import *
import unittest
import time
from collections import defaultdict
from copy import deepcopy

#NxN matrix
def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]

            #left -> top
            matrix[first][i] = matrix[last - offset][first]

            #bot -> left
            matrix[last-offset][first] = matrix[last][last-offset]

            #right -> bot
            matrix[last][last-offset] = matrix[i][last]

            #top-> right
            matrix[i][last] = top
    return matrix

class Test(unittest.TestCase):

    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]
    testable_functions = [
        # rotate_matrix_pythonic,
        rotate_matrix,
        # rotate_matrix_pythonic_alternate,
    ]

    def test_rotate_matrix(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = deepcopy(test_matrix)
                assert f(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()