import sys
import random
RESULTAT = random.randint(1,100)
ESSAIS = 5

JEU=f""""Devinez le nombre mystère (entre 1 et 100 inclu)
Il vous reste {ESSAIS} essais
Votre Choix: """

user_choice=input(JEU)

while ESSAIS > 0:
    ESSAIS-=1  
    #for i in range(1,6):
    
    if user_choice.isdigit:
           # i+=1
        #ESSAIS-=1
        if int(user_choice)==RESULTAT:
            print(f"""Bravo, le nombre mystère était bien {RESULTAT}
            tu a trouvé en {5-ESSAIS} essais""")
            sys.exit()
        elif int(user_choice)>RESULTAT:
            #ESSAIS-=1        
            user_choice = input(f"Le nombre mystère est plus petit que {user_choice} il vous reste {ESSAIS} essais. Votre choix?")
                  
        elif int(user_choice)<RESULTAT:
            #ESSAIS-=1    
            user_choice = input(f"Le nombre mystère est plus grand que {user_choice} il vous reste {ESSAIS} essais. Votre choix?")




    else:
        print("Veiller choisir un nombre valide!")

print(f"Dommage! le nombre cherché était{RESULTAT}")



print(f"Dommage le nombre mystère était {RESULTAT}")
sys.exit()

