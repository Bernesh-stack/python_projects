def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multi(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1%n2

operations={
    "+":add,
    "-":sub,
    "*":multi,
    "%":div
}
sector_1 = True
def who():

    num_1 = float(input("what is the first number"))
    for x in operations:
        print(x)
    op = input("enyter the operator")
    num_2 =float( input("enter the second number"))
    out = operations[op](num_1,num_2)
    print(f"{num_1} {op} {num_2}={out}")
    second_it = input(f"Type 'y' to continue calculating with {op}, or type 'n' to start a new calculation:").lower()
    if second_it=="y":
        for x in operations:
            print(x)
        op_2 = input("select the second op")
        num_3 =float (input("select the num_3"))
        out_2 = operations[op_2](out, num_3)
        print(f"{out} {op_2} {num_3}={out_2}")

    else:
        print("\n"*20)
        who()

who()
