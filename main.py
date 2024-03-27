
import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter: row.code for (index, row) in nato_df.iterrows()}
# print(nato_dictionary)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def make_word():
    word = input("Convert a word to NATO: ").upper()
    try:
            word_as_nato = [nato_dictionary[letter] for letter in word]
    except KeyError:
        print("only alphabet letters please")
        make_word()
    else:
        print(word_as_nato)

make_word()
