# python3

import sys
import math
from math import gcd
# from fractions import gcd

def lcm(a, b):
    return int(a * b / math.gcd(a, b))


print(lcm(18, 35))

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     a, b = map(int, input.split())
#     print(lcm(a, b))
