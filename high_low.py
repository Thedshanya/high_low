from game_data import data
import art
from replit import clear
import random


def generate_random(number1,number2):

   

    name1=data[number1]['name']
    desc1=data[number1]['description']
    con1=data[number1]['country']

    name2=data[number2]['name']
    desc2=data[number2]['description']
    con2=data[number2]['country']

    print(f"Compare A:{name1}, {desc1}, from{con1}\n")

    print(f"Compare B:{name2}, {desc2}, from { con2}\n")

score=0
run_again=True



while run_again:
    

    number1=random.randint(0,49)

    number2=random.randint(0,49)
    print(f"SCORE = {score}")
    generate_random(number1,number2)

    toContinue=True

    while toContinue==True:
        ans = input("WHO HAS MORE FOLLOWERS-A OR B:")

        fol1=data[number1]["follower_count"]
        fol2=data[number2]["follower_count"]

        if ans=='A':
            ans=fol1-fol2
        else:
            ans=fol2-fol1

        
        clear()
        # print(f"SCORE = {score}")


        if ans>0:
            number1=number2
            number2=random.randint(0,49)
            
            
            score+=1
            print(f"SCORE = {score}")
            generate_random(number1,number2)
            
        
            
        else:
            # clear()
            print(f"YOU LOST. YOUR SCORE IS {score}")
        
            play_again=input("Do You wish to continue:(Y OR N):")
            clear()
            toContinue=False
            if(play_again=='N'):
                run_again=False
                
                









