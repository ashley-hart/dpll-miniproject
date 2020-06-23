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

# TODO: Implement debug flag
# verbose: bool = False

# Check for false clauses under a truth assignment. 
def clause_check(t_vals):
    is_SAT: bool = True

    # Look for a True in every clause. If T is present in EVERY clause, return True.
    # If there is a single clause that is completely False, return False.
    # If there are no T's and undefined vars (None) return None to signify Unknown
    for c in t_vals:
        print("c: ", c)
        if True in c:
            continue
        elif None in c: 
            is_SAT = None
            continue    
        else:   
            is_SAT = False
            break

    return is_SAT

# Take a boolean statement and change all the literals according to their 
# assignments
def assign_vals(clauses, assignments):

    new_clauses = [[assignments[abs(lit)-1]*lit for lit in c if assignments[abs(lit)-1] is not 0] for c in clauses]

    return new_clauses

def convert_to_bool(clauses):
    
    bool_set = [[True if lit > 0 and lit != 0 else False for lit in c] for c in clauses]

    return bool_set

def get_truthtable(clauses):

    tt = [[None for lit in c if lit != 0] for c in clauses]

    return tt

def update_truthtable(truth_values, partial, clauses):

    new_vals: list = []
    temp: list = []

    for i in range(0, len(clauses)):

        for j in range(len(clauses[i])):
            if (abs(clauses[i][j]) - 1) < len(partial):

                if (clauses[i][j] < 0):
                    temp.append(not partial[j])
                else: 
                    temp.append(partial[j])

            else:
                temp.append(None)

        new_vals.append(temp)
        temp = []
    
    return new_vals
            

def check_SAT(truth_values):
    is_SAT: bool = False

    for clause in truth_values:
        for c in clause:
            if any(c == True) or any(c == None):
                continue
            else:
                is_SAT = False



# NOTE: Stack can't be bigger than num_vars at any time.
def solve(num_vars, num_clauses, clauses):

    partial: list = []
    current_var = 0
    truth_values = get_truthtable(clauses)
    bool_set = convert_to_bool(clauses)

    # Make room to try every possible comnination
    for i in range(0, (2**(num_vars + 1)) - 1):
        # We will try to push true and false onto this for every variable
        for a in [True, False]:

            partial.append(a)

            # Operate and check
            truth_values = update_truthtable(truth_values, partial, clauses)

            # If we still have hope, keep going.
            if clause_check(truth_values) == None:
                print("Need to descend...")
                

            # If we need to backtrack, pop off the last value and backtrack.
            partial.pop()











# This is another recursive solution I started working on. I was trying to 
# get a feel for what my stack needed to do.

'''
# Wrapper function
def solve(num_vars, num_clauses, clauses):

    clauses: list = clauses
    variables: list = [] 
    pa: list = []
    assignments = []
    satisfiable = False

    i = 1

    while i <= num_vars:
        variables.append(i)
        assignments.append(0)
        i += 1

    print("variables: ", variables)
    print("assignments: ", assignments)
    print("clauses ", clauses)

    satisfiable = solve_recursive(clauses, variables, assignments, 0, False)

   


def solve_recursive(clauses, variables, assignments, current_var, satisfiable):
    
    # Base Case - force a check if we reach the bottom of the stack.
    if current_var == (len(variables) - 1):
        satisfiable = clause_check(clauses)

        print("Base Case! Returning ", satisfiable)
        return satisfiable

    temp_clauses = copy.deepcopy(clauses)

    # Try true, then try False 
    for a in [1, -1]:

        if satisfiable == True:
            return True

        print("current variable: ", current_var)

        # Update partial assignment
        assignments[current_var] = a
        print("assignments: ", assignments)


        # Update values in the clauses
        temp_clauses = assign_vals(clauses, assignments)
        print("updated clauses: ", temp_clauses)

        # Check to see if you've got it. If you don't, go deeper.
        if clause_check != True:
            satisfiable = solve_recursive(temp_clauses, variables, assignments, current_var + 1, satisfiable)

        # Unwind if a False is hit.
        if current_var != 0:
            current_var -= 1

    return satisfiable

  '''  

