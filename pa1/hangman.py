# assignment: programming assignment 1
# author: sebastian avila
# date: 1/23/23
# file: hangman.py is a program that plays a game of hangman with user's choice of word size and number of lives
# input: two integers from user, then single characters from user
# output: game interface and prompts for input

from random import choice, randint

dictionary_file = "dictionary.txt"   

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12

def import_dictionary (filename) :
    dictionary = {}
    try:
        with open(filename, 'r') as file:
            all_words = file.read()
        all_words = all_words.split()
        for x in range(1,12):
            l = []
            for word in all_words:
                if len(word) == x:
                    l.append(word)    
            dictionary[x] = l
        long_words = []
        for word in all_words: 
            if len(word) >= 12:
                long_words.append(word)
        dictionary[12] = long_words
    except:
        pass
    return dictionary

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options () :
    size, lives = 0,0
    try:
        size = int(input('Please choose a size of a word to be guessed [3 - 12, default any size]: \n'))
        if size > 12 or size < 3:
            raise
        else:
            print(f'The word size is set to {size}.')
    except:
        size = randint(3,12)
        print('A dictionary word of any size will be chosen.')
        
    try:
        lives = int(input('Please choose a number of lives [1 - 10, default 5]: \n'))
        if lives > 10 or lives < 1:
            raise
        else:
            print(f'You have {lives} lives.')
    except:
        lives = 5
        print('You have 5 lives.')
    return (size, lives)

def print_game_interface(letters_chosen,game_letters,lives_left,start_lives):
    lives_image = ''
    lives_x = start_lives - lives_left
    for x in range(lives_x):
        lives_image += 'X'
    for x in range(lives_left):
        lives_image += 'O'
    print(f"Letters chosen: {', '.join(letters_chosen)}\n{'  '.join(game_letters)}   lives: {lives_left} {lives_image}")

# MAIN

if __name__ == '__main__' :

    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)

    # print a game introduction
    print('Welcome to the Hangman Game!')

    # START MAIN LOOP (OUTER PROGRAM LOOP)
    while True:

    # set up game options (the word size and number of lives
        size, lives = get_game_options()
    # select a word from a dictionary (according to the game options)
    # use choice() function that selects an item from a list randomly, for example:
    # mylist = ['apple', 'banana', 'orange', 'strawberry']
    # word = choice(mylist)
        possible_words = dictionary[size]
        word = choice(possible_words)        
        start_lives = lives
        letters_chosen = []
        correct_letters = [x for x in word]
        game_letters = []
        for i in range(len(word)):
            game_letters.append("__")
        if '-' in word:
            game_letters[correct_letters.index('-')] = '-'
    # START GAME LOOP   (INNER PROGRAM LOOP)
        while True:
        # format and print the game interface:
        # Letters chosen: E, S, P                list of chosen letters
        # __ P P __ E    lives: 4   XOOOO        hidden word and lives
            print_game_interface(letters_chosen,game_letters,lives,start_lives)
             
        # ask the user to guess a letter
            try:
                while True:
                    user_guess = str(input('Please choose a new letter >\n'))
                    if user_guess.isalpha() and len(user_guess) == 1:
                        if user_guess.upper() in letters_chosen:
                            print('You have already chosen this letter.')
                            continue
                        else:
                            break
    
                letters_chosen.append(user_guess.upper())
                if user_guess in word:
                    for i in range(0,len(correct_letters)):
                        if user_guess.upper() == correct_letters[i].upper():
                            game_letters[i] = user_guess.upper()
                    print('You guessed right!')
                else:
                    lives -= 1
                    print('You guessed wrong, you lost one life.')
            except:
                pass
                
        # update the list of chosen letters

        # if the letter is correct update the hidden word,
        # else update the number of lives
        # and print interactive messages      

        # END GAME LOOP   (INNER PROGRAM LOOP)
        # check if the user guesses the word correctly or lost all lives,
        # if yes finish the game
            if lives == 0:
                print_game_interface(letters_chosen,game_letters,lives,start_lives)
                print(f'You lost! The word is {word.upper()}!')
                break
            elif '__' not in game_letters:
                print_game_interface(letters_chosen,game_letters,lives,start_lives)
                print(f'Congratulations!!! You won! The word is {word.upper()}!')
                break
    # END MAIN LOOP (OUTER PROGRAM LOOP)
        try:
            again = str(input('Would you like to play again [Y/N]?\n'))
            if again.upper() == 'Y':
                pass 
            else:
                raise
        except:
            print('Goodbye!')
            quit()
    # ask if the user wants to continue playing, 
    # if yes start a new game, otherwise terminate the program
