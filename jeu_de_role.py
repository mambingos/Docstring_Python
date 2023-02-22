import sys
import random
user_life = 50
computer_life = 50

life_potion = random.randint(15,50)
number_of_potion =3
user_attack = random.randint(5,10)
computer_attack = random.randint(5,15)
choice = ["1","2"]

while user_life > 0 and computer_life > 0:
    user_choice = input("souhaiter vous attaquer (1) ou ou utiliser une potion (2): ")
    if user_choice not in choice:
        print("veillez faire un choix valide")
        continue
    else:
        if user_choice == "1":
            user_attack = random.randint(5,10)
            computer_attack = random.randint(5,15)
            computer_life -= user_attack
            user_life -= computer_attack
            if user_life < 0 or computer_life < 0:
                
                break
            else:
                print (f"""Vous avez infligé {user_attack} points de dégat à l'ennemi🪓
            L'ennemi vous a infligé {computer_attack} points de dégat🪓
            Il vous reste maintenant {user_life} points de vie
            Il reste à l'ennemi {computer_life} points de vie""")
            print("_"*50)

        elif user_choice == "2":
            if number_of_potion == 0:
                print("Vous n'avez plus de potion...")
                continue
            else:
                computer_attack = random.randint(5,15)
                life_potion = random.randint(15,50)
                number_of_potion-=1
                user_life = user_life - computer_attack + life_potion
                print (f"""Vous avez récuppéré {life_potion} points de vie ({number_of_potion} restante{'s' if number_of_potion !=1 else ')'}
                L'ennemi vous a infligé {computer_attack} points de dégat🪓
                Il vous reste maintenant {user_life} points de vie
                Il reste à l'ennemi {computer_life} points de vie""")
            
                print("_" * 50)
                computer_attack = random.randint(5,15)
                life_potion = random.randint(15,50)
                user_life = user_life - computer_attack 
                print(f"""Vous passez votre tour...
                L'ennemi vous a infligé {computer_attack} points de dégat🪓
                Il vous reste maintenant {user_life} points de vie
                Il reste à l'ennemi {computer_life} points de vie""")
                print("_" * 50)

if computer_life < 0:
    print(f"vous avez infligé {user_attack} points de dégat à l'ennemi🪓")
    print(""" Tu as gagné!
    fin du jeu!""")

elif user_life <0 and computer_life > 0:
    print("""Perdu
    fin du jeu""")

sys.exit()







