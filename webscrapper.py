#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = int(input("Enter score for alice:"))
    bob = int(input("Enter score for bob:"))

    score_alice = []
    score_bob = []

    if alice > bob:
        return score_alice.append("1")
    elif alice < bob:
        return score_bob.append("1")
    else:
        return None

    return score_alice + score_bob

res = compareTriplets("alice", "bob")
print(res)

