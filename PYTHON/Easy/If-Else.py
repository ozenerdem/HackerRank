"""
Task
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Sample Input 1

24
Sample Output 1

Not Weird
"""
#!/bin/python3
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())

if 1 <= n and n <= 100:
    if n%2 == 1:
        print ("Weird")
    elif n in range (2,5):
        print ("Not Weird")
    elif n in range (6,21):
        print ("Weird")
    elif n > 20:
        print ("Not Weird")
    else:
        print("Not Weird")
