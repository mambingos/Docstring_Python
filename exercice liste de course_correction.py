import sys

LISTE = []

MENU ="""Choisissez parmi les options suivantes:
1: Ajouter un élément
2: Retirer un élement
3: Afficher la liste
4: Vider la liste
5: Quitter
Votre choix: """

MENU_CHOICES = ["1","2","3","4","5"]

while True:
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        print("choisissez une option valide")
        user_choice=input(MENU)
    if user_choice=="1":
        a = input("Quel est le nom de l'élement à ajouter? ")
        if a not in LISTE:
            LISTE.append(a)
            print (f"l'élément {a} a été ajouté à la liste")
        else:
            print (f"l'élément{a} est déjà présent dans la liste")


    elif user_choice=="2":
        b = input("Quel est le nom de l'élement à retirer? ")
        if b in LISTE:
            LISTE.remove(b)
            print (f"l'élément {b} a été retiré de la liste")
        else:
            print (f"l'élément{b} n'est pas présent dans la liste")
    
    elif user_choice=="3":
        if not LISTE:
            print("la liste est vide")
        else:
            print("voici votre liste:")
            for i, a in enumerate(LISTE,1):
                print (f"{i}.{a}")

        

    elif user_choice=="4":
        LISTE.clear
        print("la liste a été effacée")

    elif user_choice=="5":
        print("A bientôt!")
        sys.exit()
  
    print("-"*50)
print("-"*50) 







