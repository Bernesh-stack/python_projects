
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")


#TODO 1. Create a dictionary in this format:

dict = {row.letter:row.code for (index,row) in data.iterrows() }
print(dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# word = input("enter the word").upper()
# List = [dict[x] for x in word]
# print(List)