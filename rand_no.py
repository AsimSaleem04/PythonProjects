import random
Num = random.randint(1,100)
attempt = 0
max_attempt = 7
flag = 0
print("Guess a Number from 1 to 100")
while attempt <= max_attempt:
    guess = int(input("Enter Your Number: "))
    attempt += 1
    if guess == Num:
            print(f"Congrutulation! You have Guess the right one, {guess} = {Num}")
            flag = 1
            break
    elif guess > Num:
            print("Too High")
    else:
            print("Too low")
else:
    print(f"Game Over, The Number was {Num}")
if flag == 1 :
    print(" Winner") 
