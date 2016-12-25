__author__ = 'Vishal'

import random
from collections import defaultdict

hangman = ['''
 
    +---+
    |   |
        |
        |
        |
        |
  =========''', '''
  
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
  
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
  
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
  
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
  
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
  
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']


def get_random_movie():
    movies_dict = defaultdict(list)

    with open('movies.txt') as f:
        data = f.readlines()
        data = [d.strip() for d in data]
        for d in data:
            actor = d[:d.find(':')]
            movies = d[d.find(':') + 2:]
            movie = movies.split(',')
            for i in range(len(movie)):
                movie[i] = movie[i].strip()
            movies_dict[actor] = movie

    movie = random.choice(movies_dict[random.choice([a for a, m in movies_dict.items()])])

    hints = []
    for actor, movies in movies_dict.items():
        if movie in movies:
            hints.append(actor)

    return [movie, hints]


def introduction():

    print()
    print("Welcome to Vishal's HANGMAN GAME!".center(64))

    how_to_play = """
            1. Play individually or in groups. 
            2. Have the user select a letter of the alphabet.
            3. If the letter is contained in the name of the movie, the user takes another turn guessing a letter. 
            4. If the letter is not contained in the name of the movie, you will lose a chance. 
            5. The game continues until: 
                (a) The name of the movie is guessed (all letters are revealed) – WINNER or,
                (b) All the parts of the hangman are displayed – LOSER
                
            Note: (a) Input will be considered case insensitive.
                  (b) Input may also contain whitespace characters. 
        """

    print()
    print("How to play the game".center(64))
    print(how_to_play)
    print()


def display_movie(chances, movie, correct_letters):

    print()
    print(hangman[len(hangman) - chances])
    print()
    print('Movie to be guessed is:\n')

    for char in movie.lower():
        if char in correct_letters:
            print(char, end=' ')
        else:
            print('_', end=' ')
    print()


def get_guess(guessed_letters):

    while True:
        print('Guess a letter.')
        guess = input().lower()
        if len(guess) != 1:
            print('Please enter a single letter only.')
        elif guess in guessed_letters:
            print('You have already guessed that letter. Choose again.')
        else:
            return guess


def wrong_guess(hints):
    print()
    print('OOPS! That was a wrong guess!')
    if len(hints) > 0:
        print()
        get_hint = input('Want some hints? [%s available]  [Y/N]' % len(hints))
        print()
        if get_hint.lower().startswith('y'):
            print()
            print('%s was the lead actor of the movie' % hints[-1])
            hints.pop()
            print()
    else:
        print()
        print("All hints are used up! :(")
        print()


def start_game():

    introduction()

    input_data = get_random_movie()

    movie, hints = input_data[0], input_data[1]

    guessed_letters = ''
    correct_letters = ''
    chances = len(hangman)

    while chances != 0:

        display_movie(chances, movie, correct_letters)

        guess = get_guess(guessed_letters)
        guessed_letters += guess

        if guess in movie.lower():
            correct_letters += guess

        else:
            wrong_guess(hints)
            chances -= 1
            if chances == 0:
                print()
                print('You lost! Try again..')
                print('The movie was {}'.format(movie))
            continue

        found_all_letters = True
        for char in movie.lower():
            if char not in correct_letters:
                found_all_letters = False
                break

        if found_all_letters:
            print()
            print("Yes the movie was %s" % movie)
            print('Congratulations, You won with %s chances left!' % chances)
            break


if __name__ == '__main__':
    start_game()
