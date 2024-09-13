import random




print("Welcome to the pyPassword generator")
letter = int(input("how many letter you want in your password\n"))
numbers = int(input("how many letter you want in your password\n"))
symbol = int(input("how many symbol you want\n"))
ber = []

Letters = ["a", "b" ,"c" ,"d", "e", "f" ,"g" ,"h" ,"i" ,"j" ,"k", "l" ,"m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y ", " z"]
Symbol = ["#" ,"$" ,"%", "^" ,"&"]
Numbers = ["1","2","3","4","5","6","7","8","9"]
for x in range(0,letter+1):
    v=random.choice(Letters)
    ber.append(v)


for n in range(0,numbers+1):
    y=random.choice(Numbers)
    ber.append(y)

for x in range(0,symbol+1):
    j= random.choice(Symbol)
    ber.append(j)

sukuna=""
random.shuffle(ber)
for x in ber:
    sukuna+=x



print(sukuna)

