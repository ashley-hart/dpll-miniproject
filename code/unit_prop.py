# Ashley Hart
# UVA Summer Research Project
# DPLL-SAT Solver Miniproject

import copy

def solve(num_vars, num_clauses, clauses, verbose):
    print("Unit prop solution is under construction.")

    return False

def reduce_clauses(clauses):
    new_clauses = copy.deepcopy(clauses)

    return new_clauses

'''

def solve(num_vars, num_clauses, clauses, verbose):

    if verbose:
        print("\nUNIT_PROP SOLVE(): Attempting to satisfy the problem...")
        print("=======================================================================")

    # print("verbose = ", verbose)
    partial: list = []
    truth_values = get_truthtable(clauses)
    clauses = clauses
    current_var = 0
    verbose = verbose

    is_sat = r_solve(truth_values, partial, num_vars, current_var, clauses, verbose)

    if verbose:
        print("UNIT_PROP SOLVE(): Returning", is_sat)
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
'''