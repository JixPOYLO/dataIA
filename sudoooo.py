#POYLO-MOUNOT

from __future__ import print_function

from ortools.sat.python import cp_model


def sudoku():
  
    # Create the model.
    model = cp_model.CpModel()
    
    ligne = list(range(0, 9)) # car nombre de lignes = 9 donc les valeurs des i sont 0<=i<9
    region = list(range(0, 3)) # car nombre de cases par regions = 3*3 


    grille = {}
    for i in ligne:     #on parcourt toutes les lignes
        for j in ligne: #on parcourt toutes les colonnes 
            grille[(i, j)] = model.NewIntVar(1, 9, 'grille %i %i' % (i, j))

#definition des contraintes : 
        for i in line: 
        model.AddAllDifferent([grille[(i, j)] for j in ligne]) #toutes les valeurs sont differentes sur une ligne
        for j in line:
        model.AddAllDifferent([grille[(i, j)] for i in ligne]) #toutes les valeurs sont differentes sur une colonne

        for i in region: 
        for j in region:
            etuderegion = []
            for a in region:
            for b in region:
                etuderegion.append(grille[(3*i + a, 3*i + b)]) #on utilise append pour ajouter un element a la fin de notre liste

            model.AddAllDifferent(etuderegion) #toutes les valeurs sont differentes dans une region

            
    # initialisation par rapport a la grille sujet que l'on souhaite resoudre      
    sujet = [[0, 6, 0, 0, 5, 0, 0, 2, 0], [0, 0, 0, 3, 0, 0, 0, 9, 0],[7, 0, 0, 6, 0, 0, 0, 1, 0], 
             [0, 0, 6, 0, 3, 0, 4, 0, 0], [0, 0, 4, 0, 7, 0, 1, 0, 0], [0, 0, 5, 0, 9, 0, 8, 0, 0], 
             [0, 4, 0, 0, 0, 1, 0, 0, 6],[0, 3, 0, 0, 0, 8, 0, 0, 0], [0, 2, 0, 0, 4, 0, 0, 5, 0]]
    for i in ligne:
     for j in ligne:
          if sujet[i][j]:
                model.Add(grille[(i, j)] == sujet[i][j])

    # Resolution et sortie de la solution dans la console
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.FEASIBLE:    #FEASIBLE = resolution possible mais resultat pas forcement optimal
        for i in ligne:
            print([int(solver.Value(grille[(i, j)])) for j in ligne])


sudoku()
