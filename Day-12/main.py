import random
game = True
lives=0
computer_number=random.randint(1,101)

def values(us,comp,liv,gam):
    """checks answers"""
    if us >comp:
        print("Too high")
        print("guess again")
        return liv-1
    elif us<comp:
        print("Too low.")
        print("guess again")
        return liv - 1
    elif us ==comp:
        print("you got it")
        return liv==90





print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
user_input = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
print(computer_number)
if user_input =="easy":
    print("you have 10 lives")

    lives=10
else:
    print("you have 5 lives")
    lives=5
while game:
    user_in_num = int(input("Make a guess:"))
    lives=values(us= user_in_num,comp=computer_number,liv=lives,gam=game)
    if(lives==0):
        print("you have no chane sorry")
        game=False
    elif(lives!=0):
        print(f"You have {lives} attempts remaining to guess the number ")

    else:
        print("you got it")








