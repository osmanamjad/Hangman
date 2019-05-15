from random import seed
from random import randint

def updated_hangman(lives: int) -> None:
    """
    """
    print ('Sorry, that is incorrect. Number of lives remaining:', lives)
    print('   |----------------|') 
    print('   |                O')
    if lives < 4:
        print('   |                |')
    else:
        print('   |')
    if lives < 3:
        print('   |                V')
    else: 
        print('   |                 ')     
    if lives < 2:
        print('   |                |')
    else:
        print('   |                 ')
    if lives < 1:
        print('   |                A')
        print('------------------') 
        print('You lose the game. :(')
    else: 
        print('   |                 ') 
    if lives != 0:
        print('------------------') 

def ask_to_solve(updated_word: str, lives: int) -> int:
    print('Correct! The current word is: ' + updated_word)
    print('Would you like to solve? (y or n)')
    answer = input()
    if answer == 'y':
        print('Enter the word below')
        solve = input()
        if solve == word:
            print('Correct! Good job, you win!')
            lives = 0
        else:
            lives = lives - 1
            updated_hangman(lives)
    return lives

def correct_letter(lives: int) -> int:
    """
    """
    for i in range(len(word)):
        if word[i] == letter:
            spaces[i] = letter
    updated_word = ''
    for ch in spaces:
        updated_word = updated_word + ch + ' '
    if '_' not in updated_word:
        print('Correct! You win! The word is: ' + updated_word)
        lives = 0
    else:
        lives = ask_to_solve(updated_word, lives)
    return lives

print('Welcome to Hangman!')
print('   |----------------|')
print('   |')
print('   |')
print('   |')
print('   |')
print('   |')
print('------------------')
print ('To play, you may enter a number from the options below:\n1) Countries\n\
2) Fruits and Vegetables\n3) Movie Genres\n4) Sports\n5) Beliefs ')
choice = int(input())
countries = ['canada', 'pakistan', 'united states of america', 'iraq', 'kenya'\
             'luxembourg', 'zimbabwe', 'fiji', 'greece', 'swaziland']
fts_and_vgtbls = ['banana', 'corn', 'apple', 'orange', 'pineapple',\
                  'watermelon', 'cantaloupe', 'peach', 'pear', 'strawberry']
movie_genres = ['comedy', 'romance', 'horror', 'thriller', 'action',\
                'adventure', 'superhero', 'non fiction', 'fantasy', 'drama']
sports = ['basketball', 'tennis', 'hockey', 'soccer', 'football', 'golf', \
          'baseball', 'cricket', 'badminton', 'squash']
beliefs = ['islam', 'christianity', 'judaism', 'hinduism', 'buddhism', \
             'sikhism', 'zoroastrianism', 'bahai', 'spiritualism', 'atheism']
seed()
ran_num = randint(0, 9)
if choice == 1:
    word = countries[ran_num]
elif choice == 2:
    word = fts_and_vgtbls[ran_num]
elif choice == 3:
    word = movie_genres[ran_num]
elif choice == 4:
    word = sports[ran_num]
elif choice == 5:
    word = beliefs[ran_num]
unknown = ' _' * len(word)
print ('Your word is: '+ '_ '*len(word))
print('Each time you guess an incorrect letter, a part of the man is drawn and \
you lose 1 life. Once the man is fully drawn, you lose. You have 6 lives.')
lives = 5
spaces = unknown.split()
while not lives == 0:
    print ('Enter your letter guess:')
    letter = input()
    if letter in word:
        lives = correct_letter(lives)
    else:
        lives = lives - 1
        updated_hangman(lives)

