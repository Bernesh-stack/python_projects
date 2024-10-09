import random,game_data,art
game = True
Score = 0
def compare(comp_1, comp_2):
    if comp_1 > comp_2:
        return "a"
    else:
        return "b"
compare_a = random.choice(game_data.data)
compare_b = random.choice(game_data.data)
print(art.logo)
print(f"Compare A:{compare_a['name']}{compare_a['description']} ,from:{compare_a['country']}"
)
print(art.vs)
print(
    f"Compare A:{compare_b['name']},{compare_b['description']} ,from:{compare_b['country']}"
)
while game:
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    checker = compare(compare_a['follower_count'], compare_b['follower_count'])
    if user_input == checker:
        game = True

        Score += 1
        print("\n" * 100)
        print(art.logo)
        print(f"You're right! Current score: {Score}")
        compare_a = compare_b
        print(f"Compare A:{compare_a['name']},{compare_a['description']} ,from:{compare_a['country']}" )
        print(art.vs)
        compare_b = random.choice(game_data.data)
        print(f"Compare A:{compare_b['name']},{compare_b['description']}            {compare_b['country']}")
    else:
        game = False
        print("\n"*100)
        print("You lose")
        print(f"Sorry, that's wrong. Final score: {Score}")
