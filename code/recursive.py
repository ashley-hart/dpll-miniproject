# # Ashley Hart
# # UVA Summer Research Project
# # DPLL-SAT Solver Miniproject

from collections import deque
import copy
import sys
import solver 
import parse
 
'''
IMPORTANT: THIS IS AN UPDATED VERSION OF BACKTRACK.PY!
'''

# Check for false clauses under an assignment. 
def clause_check(clause):
    is_SAT: bool = False

    for literal in clause:
        if literal == 0:
            continue
        if literal > 0:
            is_SAT = True

    return is_SAT

# Take a boolean statement and change all the literals according to their 
# assignments
def assign_vals(clauses, assignments):

    new_clauses = [[assignments[abs(lit)-1]*lit for lit in c if assignments[abs(lit)-1] is not 0] for c in clauses]
    return new_clauses


# Wrapper function
def solve(num_vars, num_clauses, clauses):

    clauses: list = clauses
    variables: list = [] 
    assignments: list = []
    satisfiable = False

    i = 1

    # The zero ('0') assignment means that a value has not been assigned yet.
    # -1 is false and 1 is true
    while i <= num_vars:
        variables.append(i)
        assignments.append(0)
        i += 1

    satisfiable = solve_recursive(clauses, variables, assignments, 0, False)

    return satisfiable


def solve_recursive(clauses, variables, assignments, current_var, satisfiable):

    # See if every clause can be satisfied with the assignment set.
    # If we don't get a 'False' back from clause_check() then we are good to go.
    if current_var == len(variables):
        temp_clauses = assign_vals(clauses, assignments)

        for c in temp_clauses:
            satisfiable = clause_check(c)

            if satisfiable is False:
                break 

        return satisfiable
            
    # Two-way branch in search of a solution
    for a in [-1, 1]:
        assignments[current_var] = a

        if satisfiable is True:
            return satisfiable

        satisfiable = solve_recursive(clauses, variables, assignments, current_var + 1, satisfiable)


    return satisfiable

