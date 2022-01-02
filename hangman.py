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
while letters_added < word_length:
    display_word_list.append("_")
    letters_added += 1

def add_letters(letter_order, guess):
    letters_added = 0
    while letters_added < word_length:
        if letters_added == letter_order:
           display_word_list.append(guess)

def display_word():
    display_word = "" 
    for letter in display_word_list:
        display_word += letter + " "
    
print(display_word)
while wrong_guesses < 4:
    guess = input("enter a letter: ")
    for letter in letters: 
        if guess == letter:
            correct_guess = True
            letter_order = letters.index(guess) + 1
            print(f"{guess} is letter {letter_order} in the word")
            add_letters(letter_order, guess)
            display_word()
        else:
            wrong_guesses += 1