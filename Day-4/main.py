import random
num = [0,1,2]
user_choice = int(input("what is the number you are choosing\n0=stone,1=siscsor,2=paperda\n"))
computer_choice=random.choice(num)

if user_choice>=0 & user_choice<=2:
    if user_choice==0 & computer_choice==0:
        print("unna enna pethangala illa yenna yethachum kakicha")
    elif user_choice==1 & computer_choice==1:
        print("unna enna pethangala illa yenna yethachum kakicha")
    elif user_choice == 2 & computer_choice == 2:
        print("unna enna pethangala illa yenna yethachum kakicha")

    elif user_choice == 0 & computer_choice == 1:
        print("you won")
    elif user_choice == 1 & computer_choice == 0:
        print("computer won")
    elif user_choice == 1 & computer_choice == 2:
        print("you won")
    elif user_choice == 2 & computer_choice == 1:
        print("computer won")
    elif user_choice == 0 & computer_choice == 2:
        print("computer won")
    elif user_choice == 2 & computer_choice == 0:
        print("you won")
else:
    print("dai potta poriki number correct aaa parru")


