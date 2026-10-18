import random
HANGMAN_PICS = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''', '''
  +---+

  |   |
  O   |
 /|\\  |
 /    |

      |
=========''', '''
  +---+

  |   |
  O   |
 /|\\  |

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

  |   |
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
      |

      |
      |
      |
=========''']

wordList = ["apple", "banana", "bichi", "orange", "pineapple"]
#wordList = ["bichi"]
chosenWord = random.choice(wordList)
lives = 6
print(chosenWord)
# print _ for the words from wordlist
placeHolder = ""
for position in range(len(chosenWord)) : 
    placeHolder += "_"
print(placeHolder)
correct_letters = []
gameOver = False
while not gameOver :
    guess = input("Guess the letter: ").lower()
    display = ""
    for letter in chosenWord :
        if letter == guess : 
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters :
            display += letter
        else : 
            display += "_"
    print(display)
    if guess not in chosenWord :
        lives -= 1
        print ("Wrong Guess! Remaining lives : ",lives)
        if lives == 0 :
            gameOver = True
            print ("You lose")
    
    print(HANGMAN_PICS[lives])
    if "_" not in display :
        gameOver = True
        print("You win")
