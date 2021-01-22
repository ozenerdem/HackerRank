"""
1
22
333
4444
55555
......
Can you do it using only arithmetic operations, a single for loop and print statement?

Sample Input

5
Sample Output

1
22
333
4444
"""
for i in range(1,int(input())):
    print(int(i * 10**i / 9))