"""
Nathan Rogers
Mystery Word
July 15, 2016
Due Sunday at Midnight

### Questions/Assumptions
1. What test functions should I write?  Do I need a test function for
    test every function
    test edge cases (e.g. for integer: test odd and even, negative and positive)
### Next Steps
1. Write test functions
2. Update README.md
3. Push to github repo
4. Advanced Mode (optional)

Implement the evil version of this game.
Write it in a new Python program named evil_mystery_word.py.
Write tests for new functionality you introduce in evil_mystery_word_tests.py.

"""

import random


def get_word_list():
    """Returns a list of words from computer's dictionary file"""
    with open('/usr/share/dict/words' , 'r') as word_file:
        word_list = word_file.readlines()
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

    answer = get_random_word(word_list).strip().lower()
    print("The computer answer is {} letters long.".format(len(answer)))
    return answer


def main():
    answer = get_answer() #Asks user for difficulty, returns 'answer' word
    guesses = 8
    guessed_letter_list = []

    while guesses > 0:

        print("You have {} remaining guesses.".format(guesses))

        guess = input("Please guess a single letter: ").lower()

        print(answer) #GET RID OF LATER

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
                    break
                print(display_word(answer, guessed_letter_list))



        else:
            print("Please follow instructions.")

    if guesses == 0:
        print("Sorry, you lose! The correct word was '{}'.").format(answer)

"""
Let the user choose a level of difficulty at the beginning of the program.
    Easy mode only has words of 4-6 characters; normal mode only has words of 6-8 characters;
    hard mode only has words of 8+ characters.
At the start of the game, let the user know how many letters the computer's word contains.
Ask the user to supply one guess (i.e. letter) per round. This letter can be upper or lower case and it does not matter. If a user enters more than one letter, tell them the input is invalid and let them try again.
Let the user know if their guess appears in the computer's word.
Display the partially guessed word, as well as letters that have not been guessed. For example, if the word is BOMBARD and the letters guessed are a, b, and d, the screen would display:

A user is allowed 8 guesses. Remind the user of how many guesses they have left after each round.

A user loses a guess only when they guess incorrectly. If they guess a letter that is in the computer's word, they do not lose a guess.

- If the user guesses the same letter twice, do not take away a guess. Instead, print a message letting them know they've already guessed that letter and ask them to try again.

The game will end when the user constructs the full word or runs out of guesses. If the player runs out of guesses, reveal the word to the user when the game ends.

When a game ends, ask the user if they want to play again. The game begins again if they reply positively.

Requirements

- Write functions to select a subset of the complete word list.
- Write a function to select a word at random from the word list.
- Write a function to display a word with blanks/letters filled in the appropriate spots.
- Write a function to check if a word has been completely guessed.
- Write other helper functions as necessary to help with the flow of the game.
Run mystery_word_test.py and ensure you pass all the unit tests.


"""


if __name__ == '__main__':
    main()
