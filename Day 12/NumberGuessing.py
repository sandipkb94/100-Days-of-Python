import random
import art

def number_generator():
    random_number = random.randint(1,100)
    return random_number

random_number = number_generator()

def number_calculation(chance, random_number):
    for i in reversed(range(chance)):
        print(f"You have {i+1} attempts")
        user_input = int(input("Make a guess: "))
        if random_number == user_input :
            print("Correctly guessed")
            break
        elif random_number < user_input :
            print("Too high")
            print("Guess again")
        elif random_number > user_input :
            print("Too low")
            print("Guess again")
        
        #else:
          #  if(i==0):
          #      print("Game Over")
           # else:
               # print("Guess again")
print(art.logo)
print("I'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
#print(difficulty_level)
#print(random_number)
chance=0
if difficulty_level == "easy":
    chance = 10
elif difficulty_level == "hard":
    chance = 5
number_calculation(chance, random_number)