#!/usr/bin/python3

"""
Énoncé :
Ecrire un algorithme qui demande un nombre de départ, et qui calcule la somme des entiers jusqu’à
ce nombre. Par exemple, si l’on entre 5, le programme doit calculer : 1 + 2 + 3 + 4 + 5 = 15
NB : on souhaite afficher uniquement le résultat, pas la décomposition du calcul

"""
s = 0 
x = int(input("Enter "));
for i in range(x, 1, -1):
    s = s + i;

print(s)
 