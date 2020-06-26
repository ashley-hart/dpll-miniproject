# Ashley Hart
# UVA Summer Research Project
# DPLL-SAT Solver Miniproject

import copy

# Check if the truth values satisfiy the problem
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
        print(new_vals)

    return new_vals


# Reduces clauses based on a literal if possible.
# Returns reduced clauses.
def reduce_clauses(clauses, literal, verbose):

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
        print("clauses:", clauses)
        print("literal:",literal)
        print("new clauses:", new_clauses)

    return new_clauses


 # Attempt to solve with a propagation optimization.
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
    result = None

    # Base Case
    if current_var >= num_vars:

        if verbose:
            print("\nBase Case")

        return clause_check(clauses, verbose)

    # Attempt to assign True and False to every variable
    for a in [True, False]:

        partial.append(a)

        # Reduce clause set based on the current variable's assignment 
        if a == True:
            new_clauses = reduce_clauses(clauses, vars[current_var],  verbose)
        else:
            new_clauses = reduce_clauses(clauses, (vars[current_var] * -1), verbose)

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
                 
