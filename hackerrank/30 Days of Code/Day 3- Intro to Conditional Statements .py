# https://www.hackerrank.com/challenges/30-conditional-statements/submissions/code/407096211

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    
    # Check conditions in the given order
    if N % 2 != 0:
        # N is odd
        print("Weird")
    elif N % 2 == 0 and 2 <= N <= 5:
        # N is even and in the range 2-5
        print("Not Weird")
    elif N % 2 == 0 and 6 <= N <= 20:
        # N is even and in the range 6-20
        print("Weird")
    elif N % 2 == 0 and N > 20:
        # N is even and greater than 20
        print("Not Weird")
