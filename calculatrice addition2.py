a = input("choisissez un nombre : ")
b = input("coisissez un second nombre : ")
if a.isdigit() and b.isdigit():
    print (f"le résultat de l'addition de {a} et de {b} est {int(a)+int(b)}")
else:
    print ("veillez rentrer 2 nombres valides")