# def simpleArraySum(ar):
#     result = 0
#     for i in ar:
#         result += i
#     return result
# print(simpleArraySum([1,2,3,4,5]))
######################################
# def compareTriplets(a, b):
#     result=[0, 0]
#     for i in range(3):
#         if a[i] < b[i]:
#             result[1] += 1
#         elif a[i] > b[i]:
#             result[0] += 1
#     return result
# print(compareTriplets([1,5,7], [2,6,3]))
######################################
# def weird(n):
#     if n%2 == 1:
#         return ("Weird")
#     elif n in range (2, 5):
#         return ("Not Weird")
#     elif n in range (6,20):
#         return ("Weird")
#     elif n > 20:
#         return ("Not Weird")
# print(weird(3))
######################################
# n = int(input("giriniz"))
# for i in range(n):
#     print(i, end="")
######################################
# sayi = int(input("Sayi"))
# binary = print(bin(sayi))
# octal = print(oct(sayi))
# hexadecimal = print(hex(sayi))
######################################
# num = int(input("giriniz."))
# for i in range(num):
#     print("{}\t{}\t{}\t{:>5}".format(i+1, oct(i+1)[2::1], hex(i+1)[2::1].capitalize(), bin(i+1)[2::1]))
######################################
# 1 4  ,  x**3 + x**2 + x + 1
# giris = input("giriniz.")
# x = int(giris[0])
# k = int(giris[2])
# string = input("giriniz")
# if k == eval(string):
#     print("True")
######################################
# def is_leap(year):
#     leap = False
#     if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
#             leap = True
#     return leap
# print(is_leap(1800))
######################################
# year = int(input("giriniz"))
# if (year % 4) == 0:
#     if (year % 100) == 0:
#         if (year % 400) == 0:
#             print("{0} artık yıl".format(year))
#         else:
#             print("{0} artık yıl degil".format(year))
#     else:
#         print("{0} artık yıl".format(year))
# else:
#     print("{0} artık yıl degil".format(year))
######################################













