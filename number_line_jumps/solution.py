#!/bin/python3

import math
import os
import random
import re
import sys
import debugpy

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#


def kangaroo(x1, v1, x2, v2):
    debugpy.debug_this_thread()
    # Write your code here
    if v2 >= v1:
        return "NO"
    for i in range(0, 10001):
        position_1 = x1 + (i * v1)
        position_2 = x2 + (i * v2)

        if position_1 > 10000 or position_2 > 10000 or position_1 > position_2:
            return "NO"

        if position_1 == position_2:
            return "YES"
    return "NO"


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + "\n")

    fptr.close()
