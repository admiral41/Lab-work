# Write a Python program to sum three given integers. However, if two or more values are
# equal sum will be zero.

x = int(input("enter 1st integer"))
y = int(input("enter 2nd integer"))
z = int(input("enter 3rd integer"))
if x == y or y == z or x==z:
        sum = 0
        print("Integer is equa2l")
else:
        sum = x + y + z
        print("integer is not equal {}".format(sum))