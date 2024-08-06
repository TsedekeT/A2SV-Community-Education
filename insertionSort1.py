#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Element to be inserted into its correct position
    key = arr[-1]
    j = n - 2
    
    # Shift elements of the sorted part of the array that are greater than the key to one position ahead
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        print(" ".join(map(str, arr)))
        j -= 1
    
    # Insert the key at the correct position
    arr[j + 1] = key
    print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)

