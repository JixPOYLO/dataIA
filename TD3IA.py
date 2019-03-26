#from __future__ import print_function
#import sys
from ortools.constraint_solver import pywrapcp
from os import abort


def TD3sudoku():

    solver = pywrapcp.Solver('résolution sudoku');
 
 
   dim = 9


    valeurspossibles = list(range(1,9) #les valeurs pouvant etre prises sont entre 1 et 9
    ligne = valeurspossibles
    colonne = valeurspossibles
    zone = valeurspossibles                       


     grille  = [9][9]                 




    # Nous créons les contraintes 
    #pas 2 fois le meme nombre sur une meme ligne
@@ -29,3 +38,29 @@ def TD3sudoku():
            for n in range(dim):
                for m in range(n+1,dim):
                    solver.Add(grille[l0+n//dim_case[1]][c0+n%dim_case[1]] != grille[l0+m//dim_case[1]][c0+m%dim_case[1]])  

    solver.Add(grille[0][2] == 5)
    solver.Add(grille[0][4] == 6)
    solver.Add(grille[1][0] == 6)
    solver.Add(grille[2][0] == 4)
    solver.Add(grille[2][4] == 3)
    solver.Add(grille[3][1] == 3)
    solver.Add(grille[3][5] == 2)
    solver.Add(grille[4][5] == 1)
    solver.Add(grille[5][1] == 5)
    solver.Add(grille[5][3] == 2)                        

                                db = solver.Phase([grille[i//dim][i%dim] for i in range(dim*dim)], solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)
    solver.Solve(db)
    print_solution(solver, grille)

def print_solution(solver, G):
  count = 0

  while solver.NextSolution():
    count += 1
    TD3sudoku(G)
  print("\nNumber of solutions found:", count)

if __name__ == "__main__":
  main()
