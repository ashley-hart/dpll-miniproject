# Ashley Hart
# UVA Summer Research Project
# DPLL-SAT Solver Miniproject

import solver 
import parse

verbose: bool = False
clauses = []

# If True is present in EVERY clause, return True.
# If there is a single clause that is completely False, return False.
# If there are no T's and but undefined vars exist return None to signify Unknown 
def clause_check(t_vals, verbose):
    is_SAT: bool = True

    for c in t_vals:
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


def update_truthtable(truth_values, partial, var, clauses):

    new_vals: list = []
    temp: list = []

    for i in range(len(clauses)):
        for j in range(len(clauses[i])):

            if (abs(clauses[i][j]) - 1) == var:
                if (clauses[i][j] < 0):
                    temp.append(not partial[var])
                else: 
                    temp.append(partial[var])

            else:
                temp.append(truth_values[i][j])

        new_vals.append(temp)
        temp = []
    
    if verbose:
        print("OG T_vals:", truth_values)
        print("partial: ",partial)
        print("var = ",var)
        print(new_vals)

    return new_vals
            

# TODO: Record partial solution into solution feild of Problem object.
def solve(num_vars, num_clauses, clauses, verbose):

    partial: list = []
    truth_values = [[None for lit in c if lit != 0] for c in clauses]
    clauses = clauses
    current_var = 0
    verbose = verbose

    
    if verbose:
        print("\nRECURSIVE SOLVE(): Attempting to satisfy the problem...")
        print("=======================================================================")

    is_sat = r_solve(truth_values, partial, num_vars, current_var, clauses, verbose)

    if verbose:
        print("RECURSIVE SOLVE(): Returning", is_sat)
        print("=======================================================================")
    return is_sat


def r_solve(initial_t_vals, initial_partial, num_vars, current_var, clauses, verbose):
        
    t_vals = [[t_val for t_val in c] for c in initial_t_vals]
    partial = [partial for partial in initial_partial]
    result = None

    # Base Case
    if current_var >= num_vars:

        if verbose:
            print("\nBase Case")

        return clause_check(clauses, verbose)

    # We will try to push true and false onto this for every variable
    for a in [True, False]:

        partial.append(a)

        if verbose:
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

            if verbose:
                print("Backing up...") 

            partial.pop()
            continue

        # If None, descend into another call
        else: 
            if verbose:
                print("Going down...")

            if r_solve(t_vals, partial, num_vars, current_var + 1, clauses, verbose) is True:
                return True
            # Try other option.Don't waste time updating values if we've already tried both options.
            elif a != False:
                partial.pop()
                t_vals = [[t_val for t_val in c] for c in initial_t_vals]

    
    return False
                 
