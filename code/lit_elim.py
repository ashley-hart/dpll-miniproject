# Ashley Hart
# UVA Summer Research Project
# DPLL-SAT Solver Miniproject

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
            
def get_pure_literals(clauses, num_vars, verbose):

    lits = []

    # Add all possible literals to a list for elimination.
    for i in range(1, num_vars + 1):
        lits.append(i)
        lits.append(i * -1)
    

    for i in range(0, len(clauses)):
        j = 0
        while j < len(lits):
            if lits[j] not in clauses[i]:
                lits.remove(lits[j])

            j += 1

    if verbose:
        print("GET_PURE_LITS(): Returning:", lits)

    return lits

def strip_clauses(clauses, lits, verbose):

    new_clauses = [[lit for lit in c] for c in clauses]

    j = 0

    for i in range(len(new_clauses)):
        while j < len(new_clauses[i]):
            if new_clauses[i][j] in lits:
                new_clauses[i].remove(new_clauses[i][j])

            j += 1

    if verbose:
        print("STRIP_CLAUSES(): lits:",  lits)
        print("STRIP_CLAUSES(): new_clauses:", new_clauses)

    return new_clauses

# TODO: Record partial solution into solution field of Problem object.
def solve(problem):

    partial: list = []
    truth_values = [[None for lit in c if lit != 0] for c in problem.clauses]
    current_var = 0
    verbose = problem.verbose
    
    if verbose:
        print("\n\nLIT_ELIM SOLVE(): Attempting to satisfy the problem...")
        print("=======================================================================")

    pure_lits = get_pure_literals(problem.clauses, problem.num_vars, problem.verbose)
    new_clauses = strip_clauses(problem.clauses, pure_lits, problem.verbose)

    is_sat = r_solve(truth_values, partial, problem.num_vars, current_var, new_clauses, problem.verbose)

    if verbose:
        print("LIT_ELIM SOLVE(): Returning", is_sat)
        print("=======================================================================")
    return is_sat


def r_solve(initial_t_vals, initial_partial, num_vars, current_var, clauses, verbose):
        
    t_vals = [[t_val for t_val in c] for c in initial_t_vals]
    partial = [partial for partial in initial_partial]
    result = None

    # Base Case
    if current_var >= num_vars:

        print("current_var:", current_var, " num_vars:", num_vars)

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
        t_vals = update_truthtable(initial_t_vals, partial, current_var, clauses, verbose)
        result = clause_check(t_vals, verbose)

        # If True, send this result right back up
        if result == True:

            if verbose: 
                print("\na =", a)
                print("clauses =", clauses)
                print("partial assignment: ", partial)
                print("t_vals: ", t_vals)
                print()
                print("LIT_ELIM SOLVE(): Solution:", partial)
    
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
                 
