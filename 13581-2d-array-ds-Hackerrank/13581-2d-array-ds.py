#!/bin/python3

import math
import os
import random
import re
import sys

def hourglassSum(arr):
    max_sum = float('-inf')
    for i in range(4):
        for j in range(4):
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            down = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            hour_glass = top + middle + down
            if hour_glass > max_sum:
                max_sum = hour_glass
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna