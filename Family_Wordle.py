'''
Wordle - Baby Announcement Edition
Nicholas Wilkins
11/23/2023
'''
import random 
import time

play_again = 'yes'

while play_again.lower() == 'yes':
    # list of possible words
    words = ['baby', 'child', 'grandson', 'crib', 'pacifier', 'cousin', 'bassinet']   
    # selects a word at random from the list 
    win = random.choice(words)   
    # sets the guess count to 1 in case the user gets it right the first time
    guess_count = 1    
    print('\nWelcome to the word guessing game!\n')
    print('This game is very similar to the game "Wordle", made popular by the NYT. The rules are as follows:\n')
    print('1. Your guess must have the same number of letters as the secret word.\n2. If a letter is in the secret word, it will be printed as lowercase in the next hint.\n3. If a letter in your guess is in the same place as it is in the secret word, it will be capitalized.\n4. Have fun and brainstorm with others if needed!\n')
    print(f'The secret word has {len(win)} letters in it!\n')
    # This next line of code will enable it so that "your hint is" has the hint underscores print on the same line
    print('Your hint is: ', end = ' ')
    for i in range(len(win)):
        print('_', end = ' ')
    # Program will ask user for an input on what the secret word is
    print() 
    print()
    guess = input('What is the secret word?: ')
    while guess.lower() != win:
        # adds one to guess count since the user got it wrong
        guess_count = guess_count + 1  
        print()  
        # This next line of code will check if the user input is the same length as the win word
        if len(guess) != len(win):
            print(f'Your guess was not the same length as the word. The word has {len(win)} letters. Please try again.')
        else: 
            print('I am sorry, that is not the secret word!')
            print()
            print('Your hint is: ', end = ' ')
            for i in range(len(guess)) and range(len(win)):
                if guess[i] == win[i]:
                    print(guess[i].upper(), end = ' ')
                elif guess[i] in win:
                    print(guess[i].lower(), end = ' ')
                else:
                    print('_', end = ' ')
        print()
        print()
        guess = input('What is the secret word?: ')
    # user guessed the word correctly
    print(f'\nCongratulations, you found the secret word! Your total number of guesses was {guess_count}.\n')
    time.sleep(2)
    print('Want to know a secret?\n')
    time.sleep(3)
    print('Jannetta is pregnant with her first child!\n')
    time.sleep(3)
    print('Want to know another secret?\n')
    time.sleep(3)
    print("It's a baby boy! He is due May 31st, 2024!\n")
    time.sleep(3)
    print("Isn't that exciting?!\n")
    time.sleep(3)
    play_again = input('Would you like to play again? (yes or no): ')
# user did not want to play again
print('\nThank you for playing. Have a nice day!\n') 