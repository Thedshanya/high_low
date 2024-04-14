from game_data import data
from replit import clear
import random
score=0
toContinue=True


number1=random.randint(0,50)

number2=random.randint(0,50)


def generate_random(number1,number2):

    name1=data[number1]['name']
    desc1=data[number1]['description']
    con1=data[number1]['country']

    name2=data[number2]['name']
    desc2=data[number2]['description']
    con2=data[number2]['country']

    print(f"Compare A:{name1}, {desc1}, from{con1}\n")

    print(f"Compare B:{name2}, {desc2}, from { con2}\n")



generate_random(number1,number2)

while toContinue==True:
    ans = input("WHO HAS MORE FOLLOWERS-A OR B:")

    fol1=data[number1]["follower_count"]
    fol2=data[number2]["follower_count"]

    if ans=='A':
        ans=fol1-fol2
    else:
        ans=fol2-fol1



    if ans>0:
        number1=number2
        number2=random.randint(0,50)
        generate_random(number1,number2)
        score+=1
        print(f"YOUR SCORE IS {score}")
        
    else:
        clear()
        print(f"YOU LOST. YOUR SCORE IS {score}")
        toContinue=False










