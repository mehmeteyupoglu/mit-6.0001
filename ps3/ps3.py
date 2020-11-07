# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Mehmet Eyüpoğlu
# Collaborators : None
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    
    first_component = 0
    
    for i in word.lower(): 
        if i in CONSONANTS or i in VOWELS:     
            first_component += SCRABBLE_LETTER_VALUES[i]
        else: pass
    
    second_component = 7 * len(word) - 3 * (n - len(word)) 
    
    if second_component < 0 : 
        second_component = 1
    
    return first_component * second_component

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    letters = []
    
    for letter in hand.keys():
        for j in range(hand[letter]):
            letters.append(letter)
            
    return letters                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    handCopy = hand.copy()
    new_hand = display_hand(handCopy)
    for i in word.lower(): 
        if i in new_hand: 
            new_hand.remove(i)
    
    result = get_frequency_dict(new_hand)
    return result

# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    word_list = load_words() #returns an array
    hand_copy = hand.copy()
    
    return_value = True
    
    word = word.lower()
    word_as_dictionary = get_frequency_dict(word)

    if word in word_list:  
        for i in word_as_dictionary.keys(): 
            if hand_copy.get(i, 0) == word_as_dictionary.get(i, 0) or hand_copy.get(i, 0) > word_as_dictionary.get(i, 0): 
                return_value
            else: 
                # print('else i is ', hand_copy.get(i, 0))
                return False
    else: 
        if '*' in word: 
            for i in VOWELS: 
                updated_word = word.replace('*', i)
                if updated_word in word_list: 
                    return updated_word
        return False
 
    return return_value

# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    num_letters = 0
    for i in hand.keys():
        num_letters += hand[i]
    
    return num_letters
        
hand = {'c': 1, 'o': 1, '*': 1, 'w': 1, 's':1, 'z':1, 'y': 2}
calculate_handlen(hand)

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    score = 0
    end_game = False

        
    while calculate_handlen(hand) > 0: 

        user_input = input('Enter word, or "!!" to indicate that you are finished: ')

        if user_input == "!!": 
            end_game = True
            break 
        else: 
            if is_valid_word(user_input, hand, word_list): 
                n = calculate_handlen(hand)
                score += get_word_score(user_input, n)
                hand = update_hand(hand, user_input)
                print('updated hand ', hand)
                print('You earned: ', get_word_score(user_input, n))
                print(user_input, 'earned', get_word_score(user_input, n), 'points. Total:', score, 'points')
                
            else:     
                hand = update_hand(hand, user_input)
                print(user_input, ' is invalid!')
                update_hand(hand, user_input)
            
    if end_game == True: 
        print('Total score for this hand:', score)
        print('-' * 50)
        return score
    
    if calculate_handlen(hand) < 1: 
        print('Ran out of letters ')
        print('Total score for this hand:', score)
        return score
    
# hand = {'c': 1, 'o': 1, '*': 1, 'w': 1, 's':1, 'z':1, 'y': 2}
# word_list = load_words()

# play_hand(hand, word_list)

# Problem #6: Playing a game

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    hand_letter = display_hand(hand)
    hand_copy = hand.copy()
    letters = string.ascii_lowercase
    
    try: 
        for i in hand_letter: 
            if i in letters: 
                letters = letters.replace(i, '')
        
        random_letter = random.choice(letters)
        
        if random_letter in hand_letter: 
            return hand_copy
        else: 
            hand_copy[random_letter] = hand_copy[letter]
            hand_copy.pop(letter)
    except KeyError: 
        print('You entered a character not in the hand. Give a letter that exist in the hand. ')
    
    return hand_copy
        
def add_asterisk(hand): 

    running = True
    
    hand_copy = hand.copy()
    hand_keys = display_hand(hand_copy)
    
    while running: 
        random_key = random.choice(hand_keys)
        if random_key in VOWELS and hand_copy.get(random_key, 0) == 1:
            print(random_key)
            hand_copy['*'] = hand_copy[random_key]
            hand_copy.pop(random_key)
            break
    return hand_copy

# hand = deal_hand(HAND_SIZE)
# add_asterisk(hand)
        
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    number_of_hands = input('Enter total number of hands: ')
    number_of_hands = int(number_of_hands)
    total_score = 0
    
    
    
    
    while number_of_hands > 0:
        print('Hand number:', number_of_hands)

        hand = deal_hand(HAND_SIZE)
        hand = add_asterisk(hand)
        word_list = load_words()
        current_hand = display_hand(hand)
        print('Current hand: ', current_hand)
        
        substitute = input('Would you like to substitute a letter?')
        
        if substitute.lower() == 'yes': 
            letter_asked = input('Which letter would you like to replace: ')
            while letter_asked not in string.ascii_lowercase: 
                letter_asked = input('The word to replace should be an alphabet: ')    
            hand = substitute_hand(hand, letter_asked)
            print('Substituted hand:', hand)
        
        play_hand(hand, word_list)
        
        one_more_time = input('Would you like to replay the hand? ')
        
        if one_more_time.lower() == 'yes':
            play_hand(hand, word_list)
            
        total_score += play_hand(hand, word_list)
        number_of_hands -= 1
    
    if number_of_hands == 0: 
        print('Your overall score is ', total_score)
        
#

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
