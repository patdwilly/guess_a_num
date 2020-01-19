import random

random.seed
num=random.randint(0,20)
guess="-1"
while int(guess) != num:
    guess=input("Guess a number between 0 and 20!\n")
    if int(guess)<num:
        print("Too Low!")
    elif int(guess)>num:
        print("Too High!")
print("Congratulations!!  The number was",num)
