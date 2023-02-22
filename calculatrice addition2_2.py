
#------------------------------------------------------# avec boucles while

a = b =""
while not (a.isdigit() and b.isdigit()):
    a = input("choisissez un nombre : ")
    b = input("choisissez un second nombre : ")
    if not (a.isdigit() and b.isdigit()):
        print ("veillez rentrer 2 nombres valides")
print (f"le résultat de l'addition de {a} et de {b} est {int(a)+int(b)}")