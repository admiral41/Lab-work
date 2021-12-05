# Given the integer N - the number of minutes that is passed since midnight - how many
# hours and minutes are displayed on the 24h digital clock?
inte = int(input("enter the integer N : "))
hour = inte // 60
minutes = inte  % 60 
print (hour,minutes)