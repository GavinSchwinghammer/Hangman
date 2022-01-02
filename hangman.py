from words import words
import random

word_item = random.randint(0, 1521)
word = words[word_item]
word_length = len(word)
letters = list(word)
print(word)
print(letters)
print(f"there are {word_length} letters in the word")
wrong_guesses = 0

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
    letters_added = 0
    while letters_added < word_length:
        if letters_added == letter_order:
           display_word_list[letter_order] = guess
    return display_word_list
    
while wrong_guesses < 4:
    guess = input("enter a letter: ")
    for letter in letters: 
        if guess == letter:
            correct_guess = True
            letter_order = letters.index(guess) + 1
            print(f"{guess} is letter {letter_order} in the word")
            display_word_list = add_letters(letter_order, guess)
            print(display_word_list)
            word_output = display_word(display_word_list)
            print(word_output)
        else:
            wrong_guesses += 1