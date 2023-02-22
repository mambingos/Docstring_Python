age=input("quel est votre age? ")
if int(age)>=18:
    print("vous êtes majeur")
elif int(age)<18:
    print(f"il faut encore attendre {18-int(age)} pour jouer")