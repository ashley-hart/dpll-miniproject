# Ashley Hart
# UVA Summer Research Project
# DPLL-SAT Solver Miniproject

import copy

# Checks a set of truth values derived from a partial assignment and a clause set.
# Determines if the assignment satisfies the problem.
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

# Updates the set of truth values under a given assignemnt. Also converts clauses 
# to booleans.
def update_truthtable(truth_values, partial, var, clauses, verbose):

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
        print("new_vals: ",new_vals)

    return new_vals

def reduce_t_vals(clauses, partial, t_vals, verbose):

        new_vals = []
        temp = []

        for i in range(0, len(clauses)):
                for j in range(0, len(clauses[i])):
                        index = abs(clauses[i][j])

                        if clauses[i][j] > 0:
                                temp.append(partial[abs(clauses[i][j]) - 1])
                        elif clauses[i][j]:
                                temp.append(not partial[abs(clauses[i][j]) - 1])

                new_vals.append(temp)
                temp = []

        if verbose:
                print("TRIM T_VALS(): Given clauses:", clauses)
                print("new_vals: ", new_vals)
                print()

        return new_vals


# Reduces clauses based on a literal if possible.
# Returns reduced clauses.
def unit_propagation(clauses, literal, verbose):

    new_clauses = []
    temp = []

    for c in clauses: 

        if literal in c and len(c) > 1:     
            continue
        elif (literal * -1) in c and len(c) > 1:
            for lit in c:
                if lit != (literal * -1):
                    temp.append(lit)
        else:
            temp = copy.deepcopy(c)

        new_clauses.append(temp)
        temp = []
            
    if verbose:
        print("REDUCE_CLAUSES(): clauses:", clauses)
        print("REDUCE_CLAUSES(): literal:",literal)
        print("REDUCE_CLAUSES(): new clauses:", new_clauses)

    return new_clauses


 # Attempt to solve with a unit propagation optimization.
def solve(problem):

    current_var = 0

    verbose = problem.verbose

    truth_values = [[None for lit in c if lit != 0] for c in problem.clauses]
    partial: list = []
    vars: list = []

    for i in range(0, problem.num_vars):
        vars.append(i + 1)

    if verbose:
        print("\n\nUNIT_PROP SOLVE(): Attempting to satisfy the problem...")
        print("=======================================================================")
        print("variables: ", vars)
        print("clauses:", problem.clauses)

    is_sat = r_solve(truth_values, partial, problem.num_vars, current_var, problem.clauses, vars, verbose)

    if verbose:
        print("UNIT_PROP SOLVE(): Returning", is_sat)
        print("=======================================================================")

    return is_sat


def r_solve(initial_t_vals, initial_partial, num_vars, current_var, clauses, vars, verbose):
        
    t_vals = [[t_val for t_val in c] for c in initial_t_vals]
    partial = [partial for partial in initial_partial]
    new_clauses = clauses
    result = None

    # Shrink clauses based on a previous assignment with unit propagation
    if current_var != 0:
        if verbose:    
                print("UNIT PROPOGATION!")
                print("============================")

        if partial[current_var - 1] == True:
                new_clauses = unit_propagation(clauses, (vars[current_var - 1]), verbose)
                # t_vals = [[None for t_val in c] for c in new_clauses]      
        elif partial[current_var - 1] == False:
                new_clauses = unit_propagation(clauses, (vars[current_var - 1] * -1), verbose)
                # t_vals = [[None for t_val in c] for c in new_clauses]

                
    if [] in new_clauses:
            if verbose:
                    print("EMPTY SET PRODUCED BY UNIT PROPAGATION! RETURNING FALSE!")

            return False 

    # Base Case
    if current_var >= num_vars:

        if verbose:
            print("\nBase Case")

        return clause_check(clauses, verbose)

    # Attempt to assign True and False to every variable
    for a in [True, False]:

        partial.append(a)

        if verbose:
            print("\na =", a)
            print("partial assignment: ", partial)
            print("current_var:", current_var)

        # Define new truth values under partial assignment. Check if SAT.
        t_vals = update_truthtable(initial_t_vals, partial, current_var, new_clauses, verbose)
        result = clause_check(t_vals, verbose)


        # If True, send this result right back up
        if result == True:

            if verbose: 
                print("\na =", a)
                print("clauses =", clauses)
                print("partial assignment: ", partial)
                print("t_vals: ", t_vals)
                print()
                print("UNIT_PROP SOLVE(): Solution:", partial)
    
            return True

        # If False remove assignment and try something else.
        elif result == False:

            if verbose:
                print("Backing up...") 

            partial.pop()
            continue

        # If None, descend into another call, if that call fails, unwind and try another assignment.
        else: 
            if verbose:
                print("Going down...")

            if r_solve(t_vals, partial, num_vars, current_var + 1, new_clauses, vars, verbose) is True:
                return True
            # Try other option. Don't waste time updating values if we've already tried both options.
            elif a != False:
                partial.pop()
                t_vals = [[t_val for t_val in c] for c in initial_t_vals]
                new_clauses = clauses

    
    return False
                 
