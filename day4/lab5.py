# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

heldclass = int(input("enter the number  of class held"))
attendclass = int(input("enter the number of class attended"))
percentage =(attendclass/heldclass)*100
print("your total attendence is {}".format(percentage))
if(percentage >= 75):
    print("You can sit in exam")
else:
    print("you cannot sit in exam")