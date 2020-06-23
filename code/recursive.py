# Ashley Hart
# UVA Summer Research Project
# DPLL-SAT Solver Miniproject

import copy
import solver 
import parse
 
'''
IMPORTANT: THIS IS AN UPDATED VERSION OF BACKTRACK.PY!
'''

# TODO: Implement debug flag
verbose: bool = False
clauses = []

# If True is present in EVERY clause, return True.
# If there is a single clause that is completely False, return False.
# If there are no T's and but undefined vars exist return None to signify Unknown 
def clause_check(t_vals):
    is_SAT: bool = True

    for c in t_vals:
        # print("c: ", c)
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


def get_truthtable(clauses):

    tt = [[None for lit in c if lit != 0] for c in clauses]

    return tt


def update_truthtable(truth_values, partial, var, clauses):

    new_vals: list = []
    temp: list = []

    for i in range(len(clauses)):
        for j in range(len(clauses[i])):

            # print("i = ", i, "j = ", j)
            if (abs(clauses[i][j]) - 1) == var:

                if (clauses[i][j] < 0):
                    temp.append(not partial[j])
                else: 
                    temp.append(partial[j])

            else:
                temp.append(truth_values[i][j])
            
            j += 1
        i += 1

        new_vals.append(temp)
        temp = []
    
    # print(new_vals)
    return new_vals
            

def check_SAT(truth_values):
    is_SAT: bool = False

    for clause in truth_values:
        for c in clause:
            if any(c == True) or any(c == None):
                continue
            else:
                is_SAT = False


# TODO: Record partial solution into solution feild of Problem object.
def solve(num_vars, num_clauses, clauses, verbose):

    if verbose:
        print("\nRECURSIVE SOLVE(): Attempting to satisfy the problem...")
        print("=======================================================================")

    # print("verbose = ", verbose)
    partial: list = []
    truth_values = get_truthtable(clauses)
    clauses = clauses
    current_var = 0
    verbose = verbose

    is_sat = r_solve(truth_values, partial, num_vars, current_var, clauses, verbose)

    if verbose:
        print("RECURSIVE SOLVE(): Returning", is_sat)
        print("=======================================================================")
    return is_sat


def r_solve(initial_t_vals, initial_partial, num_vars, current_var, clauses, verbose):
        
    t_vals = copy.deepcopy(initial_t_vals)
    partial = copy.deepcopy(initial_partial)

    if current_var == num_vars:
        return clause_check(clauses)

    # We will try to push true and false onto this for every variable
    for a in [True, False]:

        partial.append(a)

        # Define new truth values under partial assignment.
        t_vals = update_truthtable(t_vals, partial, current_var, clauses)

        if clause_check(t_vals) == True:

            if verbose: 
                print("a = ", a)
                print("partial assignment: ", partial)
                print("t_vals: ", t_vals)
                print()
            
            if verbose:
                print("RECURSIVE_SOLVE(): Solution:", partial)
    
            return True

        elif clause_check(t_vals) == False:
            return False
        else: 
            # DELETE LATER:  In unit prop the magic happens here, simplify clause set based on choice of a. --> unit_prop.py
            if r_solve(t_vals, partial, num_vars, current_var + 1, clauses, verbose) is True:
                return True
            # Don't waste time updating values if we've already tried both options. 
            elif a != False:
                partial.pop()
                t_vals = copy.deepcopy(initial_t_vals)

    
    return False
                 




        












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

