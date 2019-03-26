
from ortools.constraint_solver import pywrapcp
from os import abort

def coloration():
  # Constraint programming engine
  solver = pywrapcp.Solver('trois coloration de graphe');

  kBase = 3

  wa = solver.IntVar(1,kBase, 'wa');
  nt = solver.IntVar(1,kBase, 'nt');
  q = solver.IntVar(1,kBase, 'q');
  nsw = solver.IntVar(1,kBase, 'nsw');
  v = solver.IntVar(1,kBase, 'v');
  sa = solver.IntVar(1,kBase, 'sa');
  t = solver.IntVar(1,kBase, 't');

  # We need to group variables in a list to use the constraint AllDifferent.
  letters = [wa, nt, q, nsw, v, sa, t];

  # Define constraints.
  solver.Add (sa != wa);
  solver.Add(sa != nt);
  solver.Add(sa != q);
  solver.Add(sa != nsw);
  solver.Add(sa != v);
  solver.Add(q != nt);
  solver.Add(q != nsw);
  solver.Add(nsw != v);
  

 
  db = solver.Phase(letters, solver.INT_VAR_DEFAULT,
                             solver.INT_VALUE_DEFAULT)
  solver.NewSearch(db)

  while solver.NextSolution():
    print(letters)

  solver.EndSearch()

  return


if __name__ == '__main__':
  coloration()

 
