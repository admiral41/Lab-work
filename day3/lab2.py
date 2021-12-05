# WAP which accepts marks of four subjects and display total marks, 
# percentage and grade. Hint: more than 70% –> distinction, 
# more than 60% –> first, more than 40% –> pass, less than 40% –> fail 

a = int(input("enter your mark of 1st subject"))
b = int(input("enter your marks of 2nd subject"))
c = int(input("enter your marks of 3rd subject"))
d = int(input("enter your marks of 4th subject"))
totalmark = (a+b+c+d)
print("Your total mark is {}".format(totalmark))
totalmark1 =totalmark /400 *100
print("Your total percentage is {}".format(totalmark1))
if(totalmark >= 70):
    print("Distinction")
elif(totalmark >=60):
    print("first")
elif(totalmark >= 40):
    print("second")
else:
    print("you are fail")

