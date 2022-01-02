from words import words
import random

word_item = random.randint(0, 1521)
word = words[word_item]
word_length = len(word)
letters = list(word)
print(word)
print(letters)
print(f"there are {word_length} letters in the word")


letters_added = 0
display_word_list = []

def display_word(display_word_list):
    word_completed = "" 
    for letter in display_word_list:
        word_completed += letter + " "
    return word_completed

while letters_added < word_length:
    display_word_list.append("_")
    letters_added += 1

word_output = display_word(display_word_list)
print(word_output)

def add_letters(letter_order, guess):
    
    letter_index = letter_order-1
    letters_added = 0
    while letters_added <= word_length:
        if letters_added == letter_index:
           display_word_list[letter_index] = guess
           break
        else:
            letters_added+=1
    return display_word_list

correct_guesses = 0
guesses = 0
wrong_guesses = 0

while wrong_guesses < 6:
    guess = input("enter a letter: ")
    for letter in letters: 
        if guess == letter:
            correct_guesses += 1
            letter_order = letters.index(guess) + 1
            print(f"{guess} is letter {letter_order} in the word")
            display_word_list = add_letters(letter_order, guess)
            word_output = display_word(display_word_list)
            print(word_output)
    guesses += 1
    wrong_guesses = guesses - correct_guesses