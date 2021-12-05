#Given a n-digit number. Find the sum of its digits.
num = int(input("Enter the Number:"))
sum = 0
for i in range(0, len(num)):
    sum = sum + num[i]
print("Sum of Digits of a Number: {}".format(sum))