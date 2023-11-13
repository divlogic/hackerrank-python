#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def migratoryBirds(arr):
    # Write your code here
    counter = {}
    birds_at_max = {}
    max_sightings = 0
    for bird in arr:
        counter[bird] = counter.get(bird, 0) + 1
        if counter[bird] > max_sightings:
            max_sightings += counter[bird]
            birds_at_max = {bird: max_sightings}
        if counter[bird] == max_sightings:
            birds_at_max[bird] = max_sightings
    sorted_maxes = sorted(birds_at_max.keys())
    return int(sorted_maxes[0])


if __name__ == "__main__":
    fptr = sys.stdout

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
