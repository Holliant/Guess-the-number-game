#importing random libary
import random
#makeing the varible n + a and making it = to a number between 0 and 10 using the random libary
n = random.randint(0,10)
a = random.randint(0,10)


#user's chance to pick a number between 0 and 10
x = input("pick a number beteen 0 and 10\n")
#checking if the randomly generated is the same as the users chose 
if str(x) == str(n):
    print("You guessed correctly\n Number = " + str(n) + " Guess = " + str(x))
else:
    print("You guessed incorectly\n Number = " + str(n) + " Guess = " + str(x))
    exit()

#asking the user if he would like to try again
c = input("If you would like to contine enter y, if you don't enter n\n")
if c == ("n"):
    print("Thank you for playing your score = 1")
    exit()
if c == ("y"):
#user's second chance to pick a number between 0 and 10
    ab = input("pick a number beteen 0 and 10\n")
if str(a) == str(ab):
    print("You guessed correctly\n Number = " + str(a) + " Guess = " + str(ab))

    


