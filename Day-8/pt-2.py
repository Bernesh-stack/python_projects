student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


def winner():
    h = 0
    winner = 0
    for x in student_scores:
        bid_value = student_scores[x]
        if bid_value > h:
            h = bid_value
            winner = x
    print(x)


winner()