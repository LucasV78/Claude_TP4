#! /usr/bin/env python3

""" Implémentation des parcours de l’arbre de calculs à la volée :
- parcours en profondeur d’abord itératif
- parcours en profondeur d’abord récursif
- parcours en largeur d’abord itératif """

from TAD.piles_listes_python import Pile
from TAD.files_listes_python import File
#from TAD.piles_listes_simplement_chainees import Pile
#from TAD.files_listes_doublement_chainees import File
from notation_polonaise_inverse import *
import time

def parcours_DFS(cartons, cible) : 
    deb=time.perf_counter()
    # cartons : une liste
    # cible : entier 
    nb_noeuds = 0
    meilleure_expression = []
    Noeuds=Pile()
    Noeuds.empiler(([],cartons))
    while not Noeuds.est_vide():
        nb_noeuds+=1
        pere=Noeuds.depiler()
        op,reste=pere
        for i in range(len(reste)):
                nouv=(op[:]+[reste[i]],reste[:i]+reste[i+1:])
                test=eval_NPI_liste(nouv[0])
                if not test[1]==None:
                    eps=abs(cible-test[1])
                    meilleure=eval_NPI_liste(meilleure_expression)[1]
                    if meilleure==None or eps<abs(cible-meilleure):
                        meilleure_expression=nouv[0]
                        print(f"{meilleure_expression} résultat : {test[1]}")
                        if eps==0:
                            fin=time.perf_counter()
                            return meilleure_expression, nb_noeuds, fin-deb
                if test[0]:
                    Noeuds.empiler(nouv)
        for x in ["+","-","*","/"]:
                nouv=(op[:]+[x],reste)
                test=eval_NPI_liste(nouv[0])
                if not test[1]==None:
                    eps=abs(cible-test[1])
                    meilleure=eval_NPI_liste(meilleure_expression)[1]
                    if meilleure==None or eps<abs(cible-meilleure):
                        meilleure_expression=nouv[0]
                        print(f"{meilleure_expression} résultat : {test[1]}")
                        if eps==0:
                            fin=time.perf_counter()
                            return meilleure_expression, nb_noeuds, fin-deb
                if test[0]:
                    Noeuds.empiler(nouv)
    fin=time.perf_counter()
    return meilleure_expression, nb_noeuds, fin-deb


def parcours_BFS(cartons, cible) : 
    deb=time.perf_counter()
    # cartons : une liste
    # cible : entier 
    nb_noeuds = 0
    meilleure_expression = []
    Noeuds=File()
    Noeuds.enfiler(([],cartons))
    while not Noeuds.est_vide():
        nb_noeuds+=1
        pere=Noeuds.defiler()
        op, reste=pere
        for i in range(len(reste)):
                nouv=(op[:]+[reste[i]],reste[:i]+reste[i+1:])
                test=eval_NPI_liste(nouv[0])
                if not test[1]==None:
                    eps=abs(cible-test[1])
                    meilleure=eval_NPI_liste(meilleure_expression)[1]
                    if meilleure==None or eps<abs(cible-meilleure):
                        meilleure_expression=nouv[0]
                        print(f"{meilleure_expression} résultat : {test[1]}")
                        if eps==0:
                            fin=time.perf_counter()
                            return meilleure_expression, nb_noeuds, fin-deb
                if test[0]:
                    Noeuds.enfiler(nouv)
        for x in ["+","-","*","/"]:
                nouv=(op[:]+[x],reste)
                test=eval_NPI_liste(nouv[0])
                if not test[1]==None:
                    eps=abs(cible-test[1])
                    meilleure=eval_NPI_liste(meilleure_expression)[1]
                    if meilleure==None or eps<abs(cible-meilleure):
                        meilleure_expression=nouv[0]
                        print(f"{meilleure_expression} résultat : {test[1]}")
                        if eps==0:
                            fin=time.perf_counter()
                            return meilleure_expression, nb_noeuds, fin-deb
                if test[0]:
                    Noeuds.enfiler(nouv)
    fin=time.perf_counter()
    return meilleure_expression, nb_noeuds, fin-deb

def parcours_DFS_recursif(cartons, cible) :
    deb=time.perf_counter()
    meilleure_expression = []
    nb_noeuds = 0
    trouve=False

    def parcours_DFSR_aux(choisis, restants) :
        nonlocal meilleure_expression,nb_noeuds,cible,trouve
        nb_noeuds+=1
        for i in range(len(restants)):
                nouv=(choisis[:]+[restants[i]],restants[:i]+restants[i+1:])
                test=eval_NPI_liste(nouv[0])
                if not test[1]==None:
                    eps=abs(cible-test[1])
                    meilleure=eval_NPI_liste(meilleure_expression)[1]
                    if meilleure==None or eps<abs(cible-meilleure):
                        meilleure_expression=nouv[0]
                        print(f"{meilleure_expression} résultat : {test[1]}")
                        if eps==0:
                            trouve=True
                            return
                if test[0]:
                    parcours_DFSR_aux(nouv[0],nouv[1])
                    if trouve:
                        return
        for x in ["+","-","*","/"]:
                nouv=(choisis[:]+[x],restants)
                test=eval_NPI_liste(nouv[0])
                if not test[1]==None:
                    eps=abs(cible-test[1])
                    meilleure=eval_NPI_liste(meilleure_expression)[1]
                    if meilleure==None or eps<abs(cible-meilleure):
                        meilleure_expression=nouv[0]
                        print(f"{meilleure_expression} résultat : {test[1]}")
                        if eps==0:
                            trouve=True
                            return
                if test[0]:
                    parcours_DFSR_aux(nouv[0],nouv[1])
                    if trouve:
                        return
    parcours_DFSR_aux([], cartons)
    fin=time.perf_counter()
    return meilleure_expression, nb_noeuds, fin-deb



if __name__ == "__main__":
    print(parcours_DFS([3,5, 7, 9, 25, 50], 859))
    print(parcours_BFS([3,5, 7, 9, 25, 50], 859))
    print(parcours_DFS_recursif([3,5, 7, 9, 25, 50], 859))
 
