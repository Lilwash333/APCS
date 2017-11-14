#Julius Washington
print("Let's multiple of 4, even, or odd?\n")
ans = int(input("Gimme a number:\n"))
if(ans % 4 == 0):
    print("This is a multiple of 4!\n")
elif (ans % 2 == 0):
    print("This number is even!\n")
else:
    print("This number is odd!\n")

print("Can you get a remainder of 0?")
num = int(input("Gimme another number:\n"))
check = int(input("One more number:\n"))
if(num % check == 0 ):
    print("Good Job!")
else:
    print("Try again!")
