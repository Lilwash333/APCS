#Julius Washington
import random
rand = random.randint(1,10)
give = 0
print("Give me a number from 1 - 10")
while(give != rand):
    give = int(input())
    if(give > rand):
        print("Your number is too high!\n Try again!")
    elif(give < rand):
        print("Your number is too low!\n Try again!")
    else:
        print("That's it!")
