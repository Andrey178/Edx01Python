# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    all_letters_guessed = True
    for letter in secretWord:
        if letter not in lettersGuessed:
            all_letters_guessed = False
    return all_letters_guessed




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessed_word = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed_word += letter
        else:
            guessed_word += '_ '
    return guessed_word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    available_letters = 'abcdefghijklmnopqrstuvwxyz'
    letters_left = []

    for letter in available_letters:
        if letter not in lettersGuessed:
            letters_left.append(letter)

    return ''.join(letters_left)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    cut_line = '-------------'
    secret_word = secretWord
    guesses_left = 8
    letters_guessed = []
    letters_entered = []

    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print(cut_line)

    while not isWordGuessed(secret_word, letters_guessed) and guesses_left > 0:
        print('You have', guesses_left, 'guesses left.')
        print('Available letters:', getAvailableLetters(letters_entered))
        letter = input('Please guess a letter: ').lower()

        if letter in secret_word:
            if letter not in letters_guessed:
                letters_guessed.append(letter)
                print('Good guess:', getGuessedWord(secret_word, letters_guessed))
            else:
                print("Oops! You've already guessed that letter:", getGuessedWord(secret_word, letters_guessed))
        else:
            if letter not in letters_entered:
                print('Oops! That letter is not in my word:', getGuessedWord(secret_word, letters_guessed))
                guesses_left -= 1
            else:
                print("Oops! You've already guessed that letter:", getGuessedWord(secret_word, letters_guessed))
        letters_entered.append(letter)
        print(cut_line)

    if guesses_left == 0:
        print('Sorry, you ran out of guesses. The word was', secret_word, '.')
    else:
        print('Congratulations, you won!')



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
secretWord = 'c'
hangman(secretWord)
