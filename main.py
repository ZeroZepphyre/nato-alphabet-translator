import pandas


# Criar um dicionário com o conteúdo do csv.
nato_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')

dict_NATO = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

# Criar uma lista que contém os fonéticos correspondentes a cada letra da palavra do usuário.
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
            print("Sorry, use only letters in the alphabet (A-Z).")
        else:
            print(word_NATO)
