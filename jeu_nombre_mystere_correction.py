import sys
import random

ESSAIS_RESTANTS = 5
RESULTAT = random.randint(1,100)
user_choice = ""
print("*** le jeu mystère ***".upper())

while ESSAIS_RESTANTS > 0:
    user_choice = input (f"""Trouvez un nombre entre 1 et 100.
    il vous reste {ESSAIS_RESTANTS} essai{'s'if ESSAIS_RESTANTS>1 else ''}
    Votre choix: """)
    if not user_choice.isdigit:
        print("Veiller choisir un nombre valide")
        #continue
    else:
        
        if RESULTAT == int(user_choice):
            break
        
    

        if RESULTAT > int(user_choice):
            print (f"le nombre mystère est plus grand que {user_choice}")
            

        if RESULTAT < int(user_choice):
            print (f"le nombre mystère est plus petit que {user_choice}")
        
    ESSAIS_RESTANTS -= 1

if ESSAIS_RESTANTS == 0:
    print (f"""Dommage! le nombre mystère était {RESULTAT}
        *** FIN DU JEU ***""")
    sys.exit()
else:
    print (f"""BRAVO!👍 le nombre mystère était bien {RESULTAT}
        Vous avez trouvé en {5-ESSAIS_RESTANTS} essai{'s'if ESSAIS_RESTANTS < 4 else''} """)