nombre=[1,21,5,44,4,9,5,83,29,31,25,38]
nombre_pair=[]
for i in nombre:
    if i % 2 == 0:
        nombre_pair.append(i)
print (nombre_pair)
#------------------------------------------------------#
nombre=[1,21,5,44,4,9,5,83,29,31,25,38]
nombre_pair=[i for i in nombre if i % 2 == 0]
print (nombre_pair)
#------------------------------------------------------#
nombre= range(-10,10)
positif=[]
for i in nombre:
    if i>=0:
        positif.append(i)
print(positif)
#------------------------------------------------------#
nombre= range(-10,10)
positif=[i for i in nombre if i>=0]
print(positif)
#------------------------------------------------------#
nombres = range (5)
doubles=[i*2 for i in nombres]
print(doubles)
#------------------------------------------------------#
nombre = range (10)
nombre_inverses = [i if i % 2==0 else -i for i in nombre ]
print (nombre_inverses)
#------------------------------------------------------#
for i in range (10):                # ou for i in range (1,11) print(f"utilisateur {i})
    print(f"utilisateur {i+1}")
