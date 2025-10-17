import random
playing=True
number=str(random.randint(1,10))
print("I will generate a number between 0 to 9")
while playing:
    guess=input("Enter your gueess:  ")
    if guess == number:
        print("You won the game :)")
        print("Your gues is",number)
        break
    else:
        print("You lose the game :( ")