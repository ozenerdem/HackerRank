"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".

"""
def swap_case(s):
    a = list(s)
    for i in range(len(a)):
        if a[i]<= 'Z' and a[i]>= 'A':
            a[i] = a[i].lower()
        elif a[i]<='z' and a[i]>= 'a':
            a[i] = a[i].upper()
    b = ""
    for i in range(len(a)):
        b += a[i]
    return b

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)