# In a given range player will guess a number
import random

print("Enter Your range: ")
lower_bound = input("Enter lower bound: ")
upper_bound = input("Enter upper bound: ")
if lower_bound.isdigit() and upper_bound.isdigit():
    lower_bound = int(lower_bound)
    upper_bound = int(upper_bound)
    if lower_bound > upper_bound:
        print("Upper bound Must be larger than lower bound")
        quit()
    elif lower_bound<0:
        print("Give a 0 or greater than lower bound")
        quit()
    elif upper_bound <=0 :
        print("give a number greater than 0")
        quit()
    elif lower_bound == upper_bound:
        print("Give some at least some range")
        quit()
else:
    print("Enter valid numbers")
    quit()
computer_guess = random.randint(lower_bound,upper_bound)
while True:
    user_guess = input("guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == computer_guess:
            print("You got it")
            break
        elif user_guess > computer_guess:
            print("You are little higher")
        elif user_guess < computer_guess:
             print("You are little Lower")
    else:
        print("please enter a number ")


