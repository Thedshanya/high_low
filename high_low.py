from game_data import data
from art import logo,vs
from replit import clear
import random

print(logo)
score=0

def generate_random(person):

   

    name=person['name']
    desc=person['description']
    con=person['country']

    

    return(f"{name}, {desc}, from {con}\n")


def checkAnswer(guess,follA_count,follB_count):
    if follA_count>follB_count:
        return guess == 'a'
    else:
        return guess == 'b'


personB=random.choice(data)

run_again=True



while run_again:
    personA=personB

    personB=random.choice(data)

    while(personA==personB):
        personB=random.choice(data)

    print(f"Compare A: {generate_random(personA)}")
    print(vs)
    print( f"Against B:{generate_random(personB)}")

    ans = input("WHO HAS MORE FOLLOWERS-A OR B:").lower()

    folA=personA["follower_count"]
    folB=personB["follower_count"]

    clear()
    print(logo)

    is_correct = checkAnswer(ans,folA,folB)

    if(is_correct):
        score+=1
        print(f"You're correct! Current score: {score}")
    else:
        run_again=False
        print(f"You lost. Your final score: {score}")


    
    
   
    