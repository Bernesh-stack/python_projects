
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z"]

contine = True
def casear(orginal_text,shift_amount,Directions):
    result = ""
    if(Directions=="decrypt"):
        shift_amount*=-1
    for x in orginal_text:
        decode_index = alphabets.index(x)
        shift_decode = decode_index + shift_amount
        shift_decode %= len(alphabets)
        xe = alphabets[shift_decode]
        result += xe

    print(f"here is the {Directions}msg:{result}")
    xc = input("if you want to continue plx enter yes or no").lower()
    if xc =="no":
        contine=False






while contine:
    direction = input("enter the value for ther encrypt or the decrypt")
    text = input("type your mesage:\n").lower()
    shift = int(input("Type the shift value"))
    casear(text, shift, direction)
