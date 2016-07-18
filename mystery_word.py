"""
Nathan Rogers
Mystery Word
July 15, 2016
Due Sunday at Midnight
"""

import random


def get_word_list():
    """Returns a list of words from computer's dictionary file"""
    with open('/usr/share/dict/words' , 'r') as word_file:
        word_list = word_file.readlines()
        word_list = [word.strip().lower() for word in word_list]
        return word_list


def is_easy_word(word):
    """Determines if a given word is 'Easy'"""
    length = len(word)
    return length >= 4 and length <= 6

def is_normal_word(word):
    """Determines if a given word is 'Normal'"""
    length = len(word)
    return length >= 6 and length <= 8

def is_hard_word(word):
    """Determines if a given word is 'Hard'"""
    return len(word) > 8

def get_easy_words(word_list):
    """Returns list of all easy words from word list"""
    return list(filter(is_easy_word, word_list))

def get_normal_words(word_list):
    """Returns list of all normal words from word list"""
    return list(filter(is_normal_word, word_list))

def get_hard_words(word_list):
    """Returns list of all hard words from word list"""
    return list(filter(is_hard_word, word_list))

def get_random_word(word_list):
    """Returns a random word from a given word list"""
    return random.choice(word_list)

def display_word(answer, guessed_letter_list):
    """Returns a formatted string of the users partial answer"""
    display = ''
    for letter in answer:
        if letter in guessed_letter_list:
            display += (letter + ' ')
        else:
            display += ('_ ')
    return display

def word_guessed(answer, guessed_letter_list):
    """Determines if the word has been fully guessed."""
    for letter in answer:
        if letter not in guessed_letter_list:
            return False
    return True


def get_answer():
    """Asks the user for a difficulty and returns an 'answer' word."""
    difficulty = input("""Choose difficulty: Any Key for Easy, 'N' for Normal,
                       and 'H' for Hard: """).lower()
    # VERIFY CHECK USER INPUT
    word_list = get_word_list()

    if difficulty == 'h':
        word_list = get_hard_words(word_list)
    elif difficulty == 'n':
        word_list = get_normal_words(word_list)
    else:
        word_list = get_easy_words(word_list)

    answer = get_random_word(word_list)
    print("The computer answer is {} letters long.".format(len(answer)))
    return answer


def main():
    while True:
        answer = get_answer() #Asks user for difficulty, returns 'answer' word
        guesses = 8
        guessed_letter_list = []

        while guesses > 0:
            print("You have {} remaining guesses.".format(guesses))
            guess = input("Please guess a single letter: ").lower()

            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letter_list:
                    print("You already guessed {}".format(guess))
                else:
                    guessed_letter_list.append(guess)
                    if guess in answer:
                        print("Nice!")
                    else:
                        print("Sorry, {} is not in the answer.".format(guess))
                        guesses -= 1
                    if word_guessed(answer, guessed_letter_list):
                        print("You have won the game!")
                        print(display_word(answer, guessed_letter_list))
                        break
                    print(display_word(answer, guessed_letter_list))
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
