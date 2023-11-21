#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked, player):
    # Write your code here
    player_length = len(player)

    answer = []
    place_tracker = 1
    current_rank = 0

    for i in range(0, len(ranked)):
        if ranked[i] == ranked[i - 1] and (i - 1) != -1:
            continue

        current_rank += 1
        for j in range(0, player_length - place_tracker):
            if player[-place_tracker] >= ranked[i]:
                answer.insert(0, current_rank)
                place_tracker += 1

    if place_tracker <= player_length:
        while place_tracker <= player_length:
            if player[-place_tracker] != player[-place_tracker + 1]:
                current_rank += 1
            answer.insert(0, current_rank)
            place_tracker += 1

    return answer


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
