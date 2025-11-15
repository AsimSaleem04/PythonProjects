# Ask Some qusetions from user and after attempt display their score
print("Welcome To Our Quiz Game!")
playing = input("Do you want to play the game: ").lower()
if playing != 'yes':
    quit()
score = 0
question = input("What is cpu? ").lower()
if question == "central processing unit":
    print("correct!")
    score +=1
else:
    print("Incorrect!")
question = input("What is gpu? ").lower()
if question == "graphical processing unit":
    print("correct!")
    score +=1
else:
    print("Incorrect!")
question = input("What is psu? ").lower()
if question == "power supply unit":
    print("correct!")
    score +=1
else:
    print("Incorrect!")

question = input("What is RAM? ").lower()
if question == "randomly access memory":
    print("correct!")
    score +=1
else:
    print("Incorrect!")
print(f"You got {score}!")
