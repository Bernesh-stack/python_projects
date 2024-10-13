from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
game_is_on = True
my_money_machine = MoneyMachine()


coffe = CoffeeMaker()
# coffe.report()
my_money_machine.report()
Menui = Menu()

while game_is_on:
    x = Menui.get_items()
    input_ans = input(f"dai unaku enna coffe venum {x}")
    find_drink = Menui.find_drink(input_ans)
    if( coffe.is_resource_sufficient(find_drink) == True):
        if(my_money_machine.make_payment(find_drink.cost) ==True):
            coffe.make_coffee(input_ans)








