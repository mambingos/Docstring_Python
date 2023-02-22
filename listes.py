import pprint 
employes=["Max","Ben","Arnaud"]
employes.append(input("qui est arrivé en janvier? "))
print(employes.index(input("lequel?")))
employes.sort()             # ici c'est une méthode mais on peur prendre la fonctionON peut choisir à la place bb= sorted(employes) et faire print (bb) pour ne pas écraser la liste
print(employes)
best= employes
best.reverse()

print(best)

