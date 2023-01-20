#!/usr/bin/env python
# coding: utf-8

# - Exercici 1
# L'exercici consisteix a crear un programa que et classifiqui una variable numèrica en funció de l’escala Suspès/Aprovat/Notable/Excel·lent.
# 
# Recorda que Suspès < 5, Aprovat > 5 i < 7, Notable > 7 i < 9 i Excel·lent > 9.

# In[ ]:


print("Bon dia")
nota = int(input("Introdueixi la nota obtinguda: "))
if nota > 0 and nota <= 4:
    print("Suspès")
if nota >= 5 and nota <= 6:
    print( "Aprovat")
if nota >= 7 and nota <= 8:
    print("Notable")
if nota >= 9 and nota <= 10:
    print("Excel·lent")


#  Exercici 2
# Utilitzant el següent tutorial crea un programa que et pregunti dos números. T’ha de mostrar un missatge dient si el primer és més gran, el segon és més gran o són iguals.

# In[ ]:


print("Segueix les instruccións següents: ")
n1=int(input("Introdueix el primer número del 1 al 10: "))
n2=int(input("Introdueix el segon número del 1 al 10: "))
if n1==n2:
    print("Els dos números tenen el mateix valor")
elif n1>n2:
    print(f"El número {n1} es més gran que {n2}")
else:
    print(f"El {n2} es més petit que {n1}")


# - Exercici 3
# Crea un programa que et pregunti el teu nom, i et demani un número. Si el número és 0, hauria de mostrar un missatge d’error. En cas contrari, hauria de mostrar el nom repetit tants cops com indiqui el número. Per exemple, “Joan Joan Joan”.

# In[ ]:


print("Bon dia! segueix les instruccions: ")
nom=input("Introduiex el teu nom: ")
num=int(input("Introdueixi un número fins al 5: "))
if num==0:
    print("Error, número introduït incorrecte")
if num >= 6:
    print("Error, número introduït incorrecte")
if num==1:
    print(nom)
if num==2:
    print(nom)
    print(nom)
if num==3:
    print(nom)
    print(nom)
    print(nom)
if num==4:
    print(nom)
    print(nom)
    print(nom)
    print(nom)
if num==5:
    print(nom)
    print(nom)
    print(nom)
    print(nom)
    print(nom)


# - Exercici 4
# Crea un programa que donada una llista qualsevol, et digui si és simètrica o no. Si ho és, que et digui quants elements té.

# In[ ]:
# Si no fos simètrica
lista1 = [1, 6, 5, 7, 10, 15, 12, 7, 1, 5, 8, 7, 10]
def simetrica(lista1):
    izquierda = 0
    derecha = len(lista1)-1
    while derecha >= izquierda:
        if not lista1[izquierda] == lista1[derecha]:
            return False
        izquierda += 1
        derecha -=1
    return True
print(simetrica(lista1))

# Si fos simètrica
lista2 = [1, 2, 3, 6, 6, 3, 2, 1]
def simetrica(lista2):
    izquierda = 0
    derecha = len(lista2)-1
    while derecha >= izquierda:
        if not lista2[izquierda] == lista2[derecha]:
            return False
        izquierda += 1
        derecha -=1
    return True
print(simetrica(lista2))

conjunto = set(lista2)
resultado = len(lista2) - len(conjunto)
print(resultado)

# - Exercici 5
# Crea un programa que donada una llista, et digui quants números coincideixen amb la seva posició. Per exemple [3,4,2,0,2,3,6] el 2 i el 6 coincideixen.

# In[ ]:
x = range(15)
list(x)

import random
y = [random.randint(0, 15) for x in range(15)]
print(y)

def cuenta_coincidentes(x, y):
    res = 0
    num_coincidente = len(x)
    for x in range(num_coincidente):
        if x[x] == y[x]:
            res += 1
    return res;

# per veure si entre les dos llistes en la mateixa posició coincideix algún valor
print(sum(a == b for a, b in zip(x, y)))

# cas de que SI coincideixin, només em dona el número de coincidències

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [3, 4, 2, 0, 2, 3, 6, 8, 8, 3]

def cuenta_coincidentes(l1, l2):
    resto = 0
    num_coincidente = len(l1)
    for x in range(num_coincidente):
        if l1[x] == l2[x]:
            resto += 1
    return resto;
print(cuenta_coincidentes(l1, l2))


print(sum(a == b for a, b in zip(l1, l2)))






