# Ashley Hart
# UVA Summer Research Project
# DPLL-SAT Solver Miniproject

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

# Updates truth value set under a given assignment.
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
        print("UPDATE_TRUTHTABLE: Original t_vals:", truth_values)
        print("UPDATE_TRUTHTABLE: partial:",partial)
        print("UPDATE_TRUTHTABLE: var = ",var)
        print("UPDATE_TRUTHTABLE: New t_vals:", truth_values)

    return new_vals
            
def reduce_t_vals(clauses, partial, t_vals, verbose):

    new_vals = []
    temp = []

    for i in range(0, len(clauses)):
            for j in range(0, len(clauses[i])):
                    if clauses[i][j] > 0:
                            temp.append(partial[abs(clauses[i][j]) - 1])
                    elif clauses[i][j]:
                            temp.append(not partial[abs(clauses[i][j]) - 1])

            new_vals.append(temp)
            temp = []

    if verbose:
        print("REDUCE_T_VALS(): Given clauses:", clauses)
        print("REDUCE_T_VALS(): new_vals: ", new_vals)

    return new_vals    


# Reduce clauses based on presence of pure literals. 
# Returns a reduced clause set. If no reductions are possible, 
# the original data will be returned.
def strip_clauses(clauses, pure_lit, partial, verbose):

    new_clauses = [[lit for lit in c] for c in clauses]

    # Strip clauses

    for c in clauses:
        if pure_lit in c:
            if len(clauses) == 1:
                new_clauses = []
            else:
                new_clauses.remove(c)

    # clauses = new_clauses
   
    if verbose:
        print("STRIP_CLAUSES(): pure literal:",  pure_lit)
        print("STRIP_CLAUSES(): new_clauses:", new_clauses)
        print("STRIP_CLAUSES(): new partial:",  partial)

    return new_clauses


# Attempt to solve with a pure literal elimination optimization.
def solve(problem):

    partial: list = []
    vars: list = []
    truth_values = [[None for lit in c if lit != 0] for c in problem.clauses]
    current_var = 0
    verbose = problem.verbose

    
    if verbose:
        print("\n\nLIT_ELIM SOLVE(): Attempting to satisfy the problem...")
        print("=======================================================================")

    # Set up partial assignment.
    for i in range(0, problem.num_vars):
        partial.append(None)

    for i in range(0, problem.num_vars):
        vars.append(i + 1)
    
    is_sat = r_solve(truth_values, partial, problem.num_vars, current_var, vars, problem.clauses, problem.verbose)

    if verbose:
        print("LIT_ELIM SOLVE(): Returning", is_sat)
        print("=======================================================================")

    return is_sat

def pure_literal_elimination(clauses, vars, partial, verbose):

    # Attempt to reduce before we try to choose assignments.
    pure_lits = get_pure_literals(clauses, vars, partial, verbose)

    new_clauses = [[lit for lit in c] for c in clauses]

    while pure_lits:
        curr_lit = pure_lits[0]
        # If a pure literal is found, do the following:
        if pure_lits != []:

            # Reduce clause set
            new_clauses = strip_clauses(new_clauses, curr_lit, partial, verbose)

            # Update partial based on pure literals.
            for p in pure_lits:
                if p > 0:
                    partial[abs(p) - 1] = True
                else: 
                    partial[abs(p) - 1] = False
        
        del pure_lits[0]
        pure_lits = get_pure_literals(new_clauses, vars, partial, verbose)

    return new_clauses

# Scan the clauses and return a list of pure literals.
def get_pure_literals(clauses, vars, partial, verbose):
    lits = []
    pure = []

    # Scan clauses and toss in every literal.
    for c in clauses:
        for lit in c:
            if lit not in lits:
                lits.append(lit)

    # Check for purity and add to pure list
    for l in lits:
        index = vars.index(abs(l))
        if (l * -1) not in lits and partial[index] == None:
            pure.append(l)

    if verbose:
        print("GET_PURE_LITS(): given literals: ", lits)
        print("GET_PURE_LITS(): pure literals: ", pure)

    return pure

# Handles pure literal elimination and moves on to recursive selection where the process will repeat.
# Returns True if SAT or False if all options are exhausted.
def r_solve(initial_t_vals, initial_partial, num_vars, current_var, vars, clauses, verbose):
        
    t_vals = [[t_val for t_val in c] for c in initial_t_vals]
    partial = [partial for partial in initial_partial]
    # new_clauses = clauses
    result = None

    if verbose: 
        print()
        print("PURE LITERAL ELIMINATION!")
        print("============================")

    
    # # Attempt to reduce before we try to choose assignments.
    # pure_lits = get_pure_literals(clauses, vars, partial, verbose)

    new_clauses = pure_literal_elimination(clauses, vars, partial, verbose)

    
    # Reduce clause set and update partial for every pure lit we have. 
    # If we get an empty list back, return True.
    if new_clauses == []:
        if verbose:
            print("EMPTY SET PRODUCED - TERMINATING EARLY!")
    
        return True

    # Edit size of truth values
    t_vals = reduce_t_vals(new_clauses, partial, t_vals, verbose)

    # Base Case - activated if we have a complete assignment.
    if None not in partial:

        if verbose:
            print("\nBase Case - complete assignment recieved.")

        return clause_check(t_vals, verbose)


    # Scan the partial assignment left to right and try to
    # assign values to any remaining unassigned variables.
    for i in range(0, len(partial)):
        if partial[i] == None:

            # We will try to push true and false onto this for every variable.     
            for a in [True, False]:

                partial[i] = a

                if verbose:
                    print("CHOOSING RECURSIVELY!")
                    print("============================")
                    print("a =", a)
                    print("partial assignment: ", partial)
                    print("t_vals before modification: ", t_vals)

                # Define new truth values under partial assignment w/ potentially reduced clauses.
                t_vals = update_truthtable(t_vals, partial, current_var, new_clauses, verbose)
                result = clause_check(t_vals, verbose)

                # If True, send this result right back up.
                if result == True:

                    if verbose: 
                        print("\na =", a)
                        print("new_clauses =", new_clauses)
                        print("partial assignment: ", partial)
                        print("t_vals: ", t_vals)
                        print("\nLIT_ELIM SOLVE(): Solution:", partial)
            
                    return True
                # If False, dont waste anymore time on this branch.
                elif result == False:

                    if verbose:
                        print("Backing up...") 

                    partial[i] = None
                    continue

                # If None, descend into another call.
                else: 
                    if verbose:
                        print("Going down...")

                    if r_solve(t_vals, partial, num_vars, current_var + 1, vars, new_clauses, verbose) is True:
                        return True

                    # Try other option. Don't waste time updating values if we've 
                    elif a != False:
                        partial[i] = None

    return False
                 
