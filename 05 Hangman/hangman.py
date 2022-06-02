import random
from words import words
import string

# Computer has to get a random word

def get_valid_word(word):
    word = random.choice(words) # randomly chooses something from the list
    while '-' in word or ' ' in word: # rejects list elements that are not words
        word = random.choice(words)

    return word.upper() # using words in capital letters

# We need to keep track of which letters we've guessed and which letters in the word we've correctly guessed.
# We also need to keep track of what is a valid letter and what isn't.

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # What the user has guessed

    # Lives
    lives = 6

    # Get user input
    while len(word_letters) > 0 and lives > 0:
        # Letters already used
        print('You have', lives,'lives left and you have used these letters:', ' '.join(used_letters))

        # What current word is (id W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        # Check for valid letters and if not used yet, add to used_letters set
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            # if guessed letter is in the word, then remove the letter from word_letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 # Take away 1 life if user guesses incorrectly.
                print('Letter is not in word')

        elif user_letter in used_letters: # If letter has already been used, and an invalid guess
            print('You have already used that character, Please try again.')

        else:
            print('Invalid character. Please try again.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died! Sorry. The word was', word)
    else:
        print('you guessed the word', word, '!!!')

hangman()