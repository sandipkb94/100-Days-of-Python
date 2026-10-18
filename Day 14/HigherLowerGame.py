from GameData import data
import random
import art

def getRandomData():
    return random.choice(data)

def formatData(account):
    name = account["name"]
    follower_count = int(account["follower_count"])
    description = account["description"]
    country = account["country"]
    return f"{name} is {description} from {country}"

def game():
    print(art.logo)
    score = 0
    continue_game = True
    account_A = getRandomData()
    account_B = getRandomData()
    while continue_game :
        #account_A = account_B
        #account_B = getRandomData()
        while account_A == account_B:
            account_B = getRandomData()
        print(f"Compare A : {formatData(account_A)}")
        print(art.vs)
        print(f"Compare B : {formatData(account_B)}")
        guess = input("Guesst who has more follower A or B ").lower()
        #correct_answer = compareFollower(guess, account_A["follower_count"], account_B["follower_count")
        if account_A["follower_count"] > account_B["follower_count"] :
            correct_answer = "a"
            account_B = getRandomData()
        elif account_A["follower_count"] < account_B["follower_count"] :
            correct_answer = "b"
            account_A = account_B
            account_B = getRandomData()
        if guess == correct_answer:
            score+=1
            print(f"You're right! Current score: {score}.")
            
        else:
            continue_game= False
            print(f"Sorry, that's wrong. Final score: {score}")

    #print(formatData(account_A))


game()