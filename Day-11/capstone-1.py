import random

def compare(u_score, c_score):
  """Compare the user's and computer's scores to determine the winner."""
  if u_score == c_score:
    return "Draw 🙃"
  elif c_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif u_score == 0:
    return "Win with a Blackjack 😎"
  elif u_score > 21:
    return "You went over. You lose 😭"
  elif c_score > 21:
    return "Opponent went over. You win 😁"
  elif u_score > c_score:
    return "You win 😃"
  else:
    return "You lose 😥"




computer_score=-1
user_score=-1
game_over = False
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card



def calculate(card):
    if sum(card)==21 and len(card)==2:
        return 0
    if 11 in card and sum(card)<21:
        card.remove(11)
        card.append(1)

    return sum(card)



user_card=[]
computer_card=[]
for _ in range(2):

    user_card.append(deal_card())
    computer_card.append(deal_card())

while not  game_over:

     user_score=calculate(user_card)
     computer_score=calculate(computer_card)
     print(f"your cards are :{user_card},total:{user_score}")
     print(f"computer first  card are {computer_card[0]}")
     if user_score ==0 and computer_score ==0:
           game_over=True
     else:
        user_second_choice = input("if y to get another cord and 'n' to pass").lower()
        if user_second_choice =="y":
            user_card.append(deal_card())

        else:
            game_over=True

while computer_score!=0 and computer_score<17:
    computer_card.append(deal_card())
print(compare(u_score=user_score,c_score=computer_score))