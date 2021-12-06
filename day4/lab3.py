# Ask user to enter age, gender ( M or F ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# And any other input of age should print "ERROR".

age = int(input("enter you age : "))
gender = str(input("enter you gender"))
if( gender == "female"):
    print("You will only work in urban")
elif(gender == "male" and age in range(20,40)):
    print("you can work any where")
elif(gender == "male" and age in range(40,60)): 
    print("he will work in urban areas only")
else:
    print("error")
