#This is the current year
year = 2017
#Take in name and age in two separate variables (one str one int)
name = input("What is your name?\n")
age = int(input("How old are you?\n"))
#Make year variable equal to current year minus age plus 100
year = str(2017 - age + 100)
#Repeat print x number of times the user request
repeat = int(input("Gimme a random number!\n"))
ans = name + ", you will be 100 in year: " + year + ".\n"
print(ans * repeat)
