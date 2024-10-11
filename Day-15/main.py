MENU={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,

    },
    "latte":{
        "ingredients":{
            "water": 200,
            "coffee": 24,
            "milk":150

        },
        "cost":2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    }

}
def check_sufficient(reses,ques):
    for x in ques:
        if(ques[x] > reses[x]):

            print(f" Sorry there is not enough {x}")
            return False
    return True

def changecheck(orginal_coast):
    quater = int(input("enter how much amount for the quaters"))
    dimes = int(input("enter the amount that you are giving for dimes"))
    nickels = int(input("ellai nickels kudu la"))
    pennies = int(input("ellai pennis kusu la"))
    calculatedvalue =0.25*quater+0.10*dimes+0.05*nickels+0.01*pennies
    if(calculatedvalue<orginal_coast):
        return "bye"
    elif(calculatedvalue==orginal_coast):
        return True
    elif(calculatedvalue>orginal_coast):
        r = calculatedvalue-orginal_coast
        return  round(r,2)







resources={
    "water":300,
    "milk":200,
    "coffee":100,
    "money":0
}
game_true=True
print("welcome to the coffe machine")
while game_true:
    user_daivan = input("What would you like? (espresso/latte/cappuccino):").lower()
    if(user_daivan=="off"):
        print("sorry the machine is shut down")
        game_true=False
    elif(user_daivan=="report"):
        for x in resources:
            print(f"{x}:{resources[x]} ")


    elif(user_daivan=="espresso" or user_daivan=="latte" or user_daivan=="cappuccino" ):
        if(check_sufficient(reses=resources,ques=MENU[user_daivan]["ingredients"]) == True):
                # changecheck(orginal_coast=MENU[user_daivan]["cost"])
                xell = changecheck(orginal_coast=MENU[user_daivan]["cost"])
                if(xell == True):
                    xy = MENU[user_daivan]["cost"]
                    yx= resources["money"]
                    resources["money"] = xy+yx


                    yel =  MENU[user_daivan]["ingredients"]
                    for xenter in yel:
                        resources[xenter] = resources[xenter] - MENU[user_daivan]["ingredients"][xenter]
                        print(f"enjoy your  {user_daivan} ☕️see you again")







                elif(xell=="bye"):
                    print("amma kitta kasu vangitu va")



                else:

                    xy = MENU[user_daivan]["cost"]
                    yx = resources["money"]
                    resources["money"] = xy + yx
                    yel = MENU[user_daivan]["ingredients"]
                    for xenter in yel:
                        resources[xenter] = resources[xenter] - MENU[user_daivan]["ingredients"][xenter]

                    print(f"your remaining values are {xell}")
                    print(f"enjoy your  {user_daivan} ☕️see you again")













