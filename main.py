import random
import hangman_words
from hangman_art import logo, stages
from replit import clear

end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You already guessed {guess}")
    if guess not in display:
        print(f"You guessed {guess}, that's not in the word. you lose a life")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])



# My code

# word_list = ["ardvark", "baboon", "camel"]
# Word = random.choice(word_list)
# blanks = []
# lives = 6

# for i in Word:
#     blanks += "_"
# print(blanks)

# word_lenth = len(Word)
# game_is_over = False
# while not game_is_over:
#     user_word = input("Guess a letter.").lower()
#     for position in range(word_lenth):
#         letter = Word[position]
#         if letter == user_word:
#             blanks[position] = letter
    
#     if user_word not in Word:
#         lives -= 1
#         print(f"you have {lives} lives left.")
#         if lives == 0:
#             game_is_over = True
#             print("You lose")
#     print(blanks)

#     if "_" not in blanks:
#         game_is_over = True
#         print("You Won")

#     print(stages[lives])






# for i in Word:
#     if i == user_word:
#         print("Right")
#     else:
#         print("Wrong")


# print(blanks)
