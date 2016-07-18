"""
Evil Mystery Word
Nathan Rogers
July 17, 2017
Did not finish, code is not in working state.  
"""

import random
from mystery_word import (get_random_word, get_easy_words, get_normal_words,
                          get_hard_words, word_guessed, display_word,
                          get_word_list)


def name_word_fam(word, letter):
    word_fam = ''
    for character in word:
        if letter == character:
            word_fam += letter
        else:
            word_fam += '_'
    return word_fam


def create_word_families(word_list, guessed_letter_list):
    """EDIT THIS DESCRIPTION: Takes a list of guesses, Returns a list of list of word families."""
    word_families = {}
    for letter in guessed_letter_list:
        for word in word_list:
            word_fam = name_word_fam(word, letter)
            if word_fam in word_families:
                word_families[word_fam].append(word)
            else:
                word_families[word_fam] = [word]
    return word_families


def get_longest_word_fam(word_families):
    """Take a word_families object and returns the largest word list and
       corresponding word_fam"""
    word_fam = max(word_families, key=lambda x: len(word_families[x]))
    return word_fam, word_families[word_fam]


def correct_guess(guess, word_list):
    """Returns True if the user has correctly guessed the word"""
    pass


def main():
    while True:
        print("Welcome to Evil Hangman!")

        word_length = int(input("How many letters would you like? "))

        word_list = get_word_list()
        word_list = [word for word in word_list if len(word) == word_length]

        print("The computer answer is {} letters long.".format(word_length))
        display_word = '_' * word_length)

        guesses = 8
        guessed_letter_list = []

        while guesses > 0:

            print("You have {} remaining guesses.".format(guesses))
            print("You have guessed: {}".format(guessed_letter_list))
            print(display_word)

            guess = input("Please guess a single letter: ").lower()

            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letter_list:
                    print("You already guessed {}".format(guess))
                else:
                    guessed_letter_list.append(guess)

                    word_families = create_word_families(answer_length, word_list, guessed_letter_list)

                    common_word_fam = max(word_families, key=lambda x: len(word_families[x]))
                    common_word_fam_list = word_families[common_word_fam]





                    # This needs to be reworked!
                    if guess in word_fam:
                        print("Nice!")
                    else:
                        print("Sorry, {} is not in the answer.".format(guess))
                        guesses -= 1
                    if word_guessed(answer, guessed_letter_list):#I MAY ALSO NEED TO CHANGE THIS
                        print("You have won the game!")
                        break
                    print(display_word(answer, guessed_letter_list)) #Maybe instead of this, just print word_fam??
            else:
                print("Please follow instructions.")

        if guesses == 0:
            print("Sorry, you lose! The correct word was '{}'.".format(answer))

        play_again = input("'Y') play again, any other key) quit: ").lower()
        if play_again == 'y':
            print("Good luck!")
        else:
            print("Thanks for playing!")
            break


if __name__ == '__main__':
    main()
