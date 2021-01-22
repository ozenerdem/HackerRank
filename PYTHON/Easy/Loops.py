"""
The list of non-negative integers that are less than n=3 is [0, 1, 2]. Print the square of each number on a separate line.

Sample Input 0

5
Sample Output 0

0
1
4
9
16
"""
if __name__ == '__main__':
    n = int(input())

for i in range(n):
    print(i**2)