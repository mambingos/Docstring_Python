import sys
import random
user_life = 50
cl = 50
number_of_potion = 3
skip_turn = False

while True:
    if skip_turn:
        print("vous passez votre tour...")
        skip_turn=False
    
    else:
        user_choice=""
        while user_choice not in ["1","2"]:
            user_choice=input("souhaitez-vous attaquer (1) ou prendre une potion (2) ? ")      
        if user_choice == "1":
            u=random.randint(5,10)
            cl=cl-u
            print (f"Vous avez infligé {u} points de dégat à l'ennemie")
            

        elif user_choice =="2":
            if number_of_potion==0:
                print("vous n'avez plus de potion")
                continue
            else:
                number_of_potion-=1
                potion=random.randint(15,50)
                user_life+=potion
                print(f"vous avez pris une potion ({number_of_potion} restantes)")
                print(f"vous avez récupéré {potion} points de vie")
                skip_turn=True
    
    if cl<=0:
        print("vous avez gagné")
        print("fin du jeu")
        print("*"*50)
        break
    else:
        computer_attack= random.randint(5,15)
        print(f"l'ennemi vous a infligé {computer_attack}")
        user_life-=computer_attack

    if user_life<= 0:
        print("vous avez perdu")
        print("fin du jeu")
        print("*"*50)
        break
    

    

    print(f"il vous reste {user_life} points de vie. Il reste à l'ennemie {cl} points de vie")
    print("*"*50)


sys.exit()







