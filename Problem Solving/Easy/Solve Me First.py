"""
Function Description
Complete the solveMeFirst function in the editor below.
solveMeFirst has the following parameters:
int a: the first value
int b: the second value
Returns
- int: the sum of a and b
Sample Input

a = 2
b = 3
Sample Output

5
"""
def solveMeFirst(a,b):
    return a+b

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)