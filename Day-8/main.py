reues_status = True
while reues_status:
    details={}
    def result():
     higher_value=0
     winner=""

     for x in details:
         bid_value = details[x]
         if bid_value > higher_value:
              higher_value = bid_value
              winner = x
     print(f"the higher values are :${higher_value} and winner is:{winner}")



    name = input("say your name\n")
    price = int(input("how many are you ready to bid \n "))

    details[name]=price
    reques = input("is there is another any person to bid yes or no ").lower()

    if(reques=="yes"):
        print("\n"*100)

    else:
        print("\n" *100)
        result()
        reues_status= False


