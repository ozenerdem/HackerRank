"""
Output Format
Print the result of a^b + c^d on one line.

Sample Input

9
29
7
27
Sample Output

4710194409608608369201743232
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
result = pow(a,b) + pow(c,d)
print(result)