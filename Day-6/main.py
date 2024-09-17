import random
word_list = ["car","bike","tatasummo"]
chosen_word = random.choice(word_list)

print(
    chosen_word
)
lives =6
correct_ansers=[]
placeholder =""
for r in range(len(chosen_word)):
    placeholder+="_"
print(placeholder)
gameover = False
while not gameover:
    guess = input("guess a letter").lower()
    display= ""
    for x in chosen_word:
     if guess in x:
         display+= guess
         correct_ansers.append(correct_ansers)
     elif guess in correct_ansers:
         display+=correct_ansers
     if guess not in  correct_ansers:
         lives=lives-1
         if lives ==0:
            print("you loose")
            gameover=True


     else:
                display+= "_"
    if "_" not in display:
        gameover = True
    if guess not in correct_ansers:
        lives = lives - 1
        if lives == 0:
            print("you loose")
            gameover = True

    print(display)
