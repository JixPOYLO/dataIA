#Jean-Alix POYLO - Louis MOUNOT
#Resolution sudoku 

from _future_ import print_function
from ortools.sat.python import cp_model

def sudoku():
  
# creation de notre modele de sudoku
    model = cp_model.CpModel()
    ligne = list(range(0, 9)) # car nombre de lignes = 9 donc les valeurs des i sont 0<=i<9
    region = list(range(0, 3)) # car une region sera assimilee a une grille de 3 lignes et 3 colonnes

    grille = {}         #declaration de notre grille 
    for i in ligne:     #on parcourt toutes les lignes
        for j in ligne: #on parcourt toutes les colonnes 
            grille[(i, j)] = model.NewIntVar(1, 9, 'grille %i %i' % (i, j))   #

# definition des contraintes : 

    for i in ligne:
        model.AddAllDifferent([grille[(i, j)] for j in ligne]) # valeur differente sur chaque ligne

    for j in ligne:
        model.AddAllDifferent([grille[(i, j)] for i in ligne]) # valeur differente sur chaque colonne

    for i in region: 
        for j in region:
            etuderegion = []
            for a in region: #dans le but de parcourir la region etudiee
                for b in region:
                    etuderegion.append(grille[(3*i + a, 3*i + b)]) #on utilise append pour ajouter un element a la fin de notre liste

            model.AddAllDifferent(etuderegion) #toutes les valeurs sont differentes dans la region etudiee

            
    #initialisation par rapport a la grille sujet que l on souhaite resoudre 
     
    sujet = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0],[0, 9, 8, 0, 0, 0, 0, 6, 0], 
             [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6], 
             [0, 6, 0, 0, 0, 0, 2, 8, 0],[0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    for i in ligne:
     for j in ligne:
          if sujet[i][j]:
                model.Add(grille[(i, j)] == sujet[i][j])

    # resolution et sortie de la solution dans la console
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.FEASIBLE:    #FEASIBLE = resolution possible mais resultat pas forcement optimal
        for i in ligne:
            print([int(solver.Value(grille[(i, j)])) for j in ligne])

sudoku()
