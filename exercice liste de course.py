
a=b="",""
liste=[]
choix= range(1,6)
#Choisir= "Choisissez parmi les options suivantes: \n 1: Ajouter un élément \n 2: Retirer un élément \n 3: Afficher la liste \n 4: Vider la liste \n 5: Quitter"
while choix!=5:
    
    choix = input("Choisissez parmi les options suivantes: \n 1: Ajouter un élément \n 2: Retirer un élément \n 3: Afficher la liste \n 4: Vider la liste \n 5: Quitter\n Votre choix: ")
    if int(choix) ==1:
        a = input("Quel est le nom de l'élément à ajouter à la liste de course? ")
        if a not in liste:
            liste.append(a)
    elif int(choix) ==2:
        b = input("Quel est le nom de l'élément à retirer de la liste de course? ")
        if b in liste:
         liste.remove(b)
    elif int(choix) == 3:
        if not liste:
            print("la liste est vide")
        else:
            print(liste)
    elif int(choix) == 4:
        liste.clear
    elif int(choix) == 5:
        exit()


