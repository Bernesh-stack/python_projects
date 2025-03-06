import pandas as pd
import random
df = pd.read_csv("../flash-card-project-start/data/french_words.csv")
xy = df.to_dict(orient="records")

def next_card():
    current_card = random.choice(xy)
    print(current_card)