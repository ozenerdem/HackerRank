"""
Function Description

Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.

simpleArraySum has the following parameter(s):

ar: an array of integers

Input Format

The first line contains an integer, n , denoting the size of the array.
The second line contains n space-separated integers representing the array's elements.
Sample Input

6
1 2 3 4 10 11
Sample Output

31
"""

import os
import sys
def simpleArraySum(ar):
    result = 0
    for i in ar:
        result += i
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

# def simpleArraySum(ar):
#     sonuc = 0
#     for i in ar:
#         sonuc += i
#     return sonuc
# if __name__ == '__main__':
#     ar_count = int(input())
#     ar = list(map(int, input().rstrip().split()))
#     result = simpleArraySum(ar)
# print(result)



