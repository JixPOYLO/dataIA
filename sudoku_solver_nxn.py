#suduku solver nxn


from __future__ import print_function
import sys
from ortools.constraint_solver import pywrapcp

dim = 6
dim_case = [2,3]

def afficher_sudoku(G):
    print("\n\nsolution sudoku")
    print("+"+("-"*dim_case[1]+"+")*dim_case[0])
    for l in range(dim):
        print('|',end="")
        for c in range(dim):
            print(G[l][c].Value(), end=""+"|"*(c%dim_case[1]==dim_case[1]-1))
        print(("\n+"+("-"*dim_case[1]+"+")*dim_case[0])*(l%dim_case[0]==dim_case[0]-1))
            
def main():
    solver = pywrapcp.Solver("sudoku_"+str(dim)+"x"+str(dim))
    # Create the variables.
    grille = [[i for i in range(dim)] for j in range(dim)]
    for l in range(dim):
        for c in range(dim):
            grille[l][c] = solver.IntVar(1, dim, "l"+str(l)+"c"+str(c))
    # Create the constraints.
    #pas 2 fois le meme nombre sur une meme ligne
    for l in range(dim):
        for n in range(dim):
            for m in range(n+1,dim):
                solver.Add(grille[l][n] != grille[l][m])
    #pas 2 fois le meme nombre sur une meme colonne
    for c in range(dim):
        for n in range(dim):
            for m in range(n+1,dim):
                solver.Add(grille[n][c] != grille[m][c])
    #pas 2 fois le meme nombre dans une meme case
    for l0 in range(0,dim,dim_case[0]):
        for c0 in range(0,dim,dim_case[1]):
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
    #Call the solver.

    db = solver.Phase([grille[i//dim][i%dim] for i in range(dim*dim)], solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)
    solver.Solve(db)
    print_solution(solver, grille)
    
def print_solution(solver, G):
  count = 0

  while solver.NextSolution():
    count += 1
    afficher_sudoku(G)
  print("\nNumber of solutions found:", count)

if __name__ == "__main__":
  main()
