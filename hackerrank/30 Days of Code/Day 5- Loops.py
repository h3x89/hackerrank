# https://www.hackerrank.com/challenges/30-loops/copy-from/407625244

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    for i in range(1, 11):
        print(n, "x", i, "=", i*n)
