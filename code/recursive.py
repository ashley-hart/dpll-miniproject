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
def clause_check(t_vals, verbose):
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

    if verbose: 
        print("CLAUSE_CHECK(): Given", t_vals)
        print("CLAUSE_CHECK(): Returning", is_SAT)

    return is_SAT



def get_truthtable(clauses):

    tt = [[None for lit in c if lit != 0] for c in clauses]

    return tt


def update_truthtable(truth_values, partial, var, clauses):

    new_vals: list = []
    temp: list = []
    # print("var = ",var)

    for i in range(len(clauses)):
        for j in range(len(clauses[i])):

            # print("i = ", i, "j = ", j)
            if (abs(clauses[i][j]) - 1) == var:
                # print("curr literal: ", clauses[i][j])
                if (clauses[i][j] < 0):
                    temp.append(not partial[var])
                    # print("hi")
                else: 
                    temp.append(partial[var])
                    # print("hi 2")

            else:
                temp.append(truth_values[i][j])

        new_vals.append(temp)
        temp = []
    
    
    # print("OG T_vals:", truth_values)
    # print("partial: ",partial)
    print(new_vals)
    return new_vals
            


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
    result = None

    # Base Case
    if current_var >= num_vars:
        print("\nBase Case")
        print()
        return clause_check(clauses, verbose)

    # We will try to push true and false onto this for every variable
    for a in [True, False]:

        partial.append(a)
        print("\na =", a)
        print("partial assignment: ", partial)

        # Define new truth values under partial assignment.
        t_vals = update_truthtable(initial_t_vals, partial, current_var, clauses)
        result = clause_check(t_vals, verbose)

        # If True, send this result right back up
        if result == True:

            if verbose: 
                print("\na =", a)
                print("clauses =", clauses)
                print("partial assignment: ", partial)
                print("t_vals: ", t_vals)
                print()
                print("RECURSIVE_SOLVE(): Solution:", partial)
    
            return True
        # If False, dont waste anymore time on this branch
        elif result == False:
            print("Backing up...")
            partial.pop()
            continue
            # return False
        # If None, descend into another call
        else: 
            print("Going down...")
            if r_solve(t_vals, partial, num_vars, current_var + 1, clauses, verbose) is True:
                return True
            # Don't waste time updating values if we've already tried both options.
            # Try another option. 
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

