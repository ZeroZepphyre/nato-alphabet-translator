import pandas


# TODO 1. Create a dictionary in this format:
nato_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')

dict_NATO = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
isRunning = True
while isRunning:
    word = input("Choose a word to translate to NATO: ").upper()
    if word == 'EXIT':
        print("Exiting program.")
        isRunning = False
    else:
        try:
            word_NATO = [dict_NATO[letter] for letter in word]
        except KeyError:
            print("Sorry, use only letters in the alphabet.")
        else:
            print(word_NATO)