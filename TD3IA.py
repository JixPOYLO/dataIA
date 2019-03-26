
from __future__ import print_function
import sys
from ortools.constraint_solver import pywrapcp

def solve_sudoku():

    # Nous créons les contraintes 
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
