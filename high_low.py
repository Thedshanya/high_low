from game_data import data
from replit import clear
import random

number1=random.randint(0,50)

number2=random.randint(0,50)

score=0

def printing(name1,desc1,con1,name2,desc2,con2):


    name1=data[number1]['name']
    desc1=data[number1]['description']
    con1=data[number1]['country']

    name2=data[number2]['name']
    desc2=data[number2]['description']
    con2=data[number2]['country']

    print(f"Compare A:{name1}, {desc1}, from{con1}\n")
    
    print(f"Compare B:{name2}, {desc2}, from { con2}\n")

printing(name1,desc1,con1,name2,desc2,con2)
ans=input("Guess who has more follower_count(A OR B):")
if data[number1]["follower_count"]>data[number2]["follower_count"]:
    if ans=='A':
        # name1=name2
        # desc1=desc2
        # con1=con2

        number1=number2

        number2=random.randint(1,50)
        printing(name1,desc1,con1,name2,desc2,con2)
        score+=1
        print(number1,number2)


    else:
        clear()
        print(f"You lost.Your highest score is {score}\n")

else:
    if ans=='B':
        # name1=name2
        # desc1=desc2
        # con1=con2
        number1=number2
        number2=random.randint(1,50)
        printing(name1,desc1,con1,name2,desc2,con2)
        score+=1
        print(number1,number2)
    else:
        clear()
        print(f"You lost.Your highest score is {score}")










