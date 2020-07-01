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


# Updates truth value set under a given assignment.
def update_truthtable(truth_values, partial, var, clauses, verbose):

    new_vals: list = []
    temp: list = []

    for i in range(0, len(clauses)):
        for j in range(0, len(clauses[i])):
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
        print("new t-vals", new_vals)

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


# Scan the clauses and return a list of pure literals.
def get_pure_literals(clauses, verbose):
    lits = []
    pure = []

    # Scan clauses and toss in every literal.
    for c in clauses:
        for lit in c:
            if lit not in lits:
                lits.append(lit)

    # Check for purity and add to pure list
    for l in lits:
        if (l * -1) not in lits:
            pure.append(l)

    if verbose:
        
        print("GET_PURE_LITS(): given literals: ", lits)
        print("GET_PURE_LITS(): pure literals: ", pure)

    return pure


# Reduce clauses based on presence of pure literals. 
# Returns a reduced clause set. If no reductions are possible, 
# the original data will be returned.
def strip_clauses(clauses, pure, partial, verbose):

    new_clauses = [[lit for lit in c] for c in clauses]

    # print("clauses: ", clauses)

    # Strip clauses
    for lit in pure:
        # print("lit =", lit)
        for c in clauses:
            # print(c)
            if lit in c:
                if len(clauses) == 1:
                    new_clauses = []
                else:
                    # print("Removing: ", c)
                    new_clauses.remove(c)
        clauses = new_clauses
   
    if verbose:
        print("STRIP_CLAUSES(): pure literals:",  pure)
        print("STRIP_CLAUSES(): new_clauses:", new_clauses)
        print("STRIP_CLAUSES(): new partial:",  partial)

    return new_clauses


# Attempt to solve with a pure literal elimination optimization.
def solve(problem):

    partial: list = []
    truth_values = [[None for lit in c if lit != 0] for c in problem.clauses]
    current_var = 0
    verbose = problem.verbose
    vars: list = []
    
    if verbose:
        print("\n\nDPLL SOLVE(): Attempting to satisfy the problem...")
        print("=======================================================================")

    for i in range(0, problem.num_vars):
        vars.append(i + 1)

    # Set up partial assignment.
    for i in range(0, problem.num_vars - 1):
        partial.append(None)

    is_sat = r_solve(truth_values, partial, current_var, problem.clauses, vars, problem.verbose)

    if verbose:
        print("DPLL SOLVE(): Returning", is_sat)
        print("=======================================================================")

    return is_sat


# Returns True if SAT or False if all options are exhausted.
def r_solve(initial_t_vals, initial_partial, current_var, clauses, vars, verbose):
        
    partial = [partial for partial in initial_partial]
    result = None
    new_clauses = clauses
    t_vals = [[t_val for t_val in c] for c in initial_t_vals]

    if verbose: 
        print()
        print("initial_partial: ", initial_partial)
        print("curr var: ", current_var)

   # Shrink clauses based on a previous assignment with unit propagation
    if current_var != 0:
        if verbose:    
                print("UNIT PROPOGATION!")
                print("============================")

        if partial[current_var - 1] == True:
                new_clauses = unit_propagation(clauses, (vars[current_var - 1]), verbose)
        elif partial[current_var - 1] == False:
                new_clauses = unit_propagation(clauses, (vars[current_var - 1] * -1), verbose)
        
    if [] in new_clauses:
        #     if verbose:
                print("EMPTY SET PRODUCED BY UNIT PROPAGATION! RETURNING FALSE!")

                return False 


    if verbose:
        print("new_clauses", new_clauses)
        print()    
        print("PURE LITERAL ELIMINATION!")
        print("============================")

    # Attempt to reduce before we try to choose assignments.
    pure_lits = get_pure_literals(clauses, verbose)

    # If a pure literal is found, do the following:
    if pure_lits != []:

        # Update partial based on pure literals.
        for p in pure_lits:
            if p > 0:
                partial[abs(p) - 1] = True
            else: 
                partial[abs(p) - 1] = False

        # Reduce clause set
        new_clauses = strip_clauses(clauses, pure_lits, partial, verbose)

        # Reduce clause set and update partial for every pure lit we have. 
        # If we get an empty list back, return True.
        if new_clauses == []:
            if verbose:
                print("EMPTY SET PRODUCED BY LITERAL ELIMINATION! RETURNING TRUE!")
        
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
                    print("new_clauses: ", new_clauses)

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
                        print()
                        print("DPLL SOLVE(): Solution:", partial)
            
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

                    if r_solve(t_vals, partial, current_var + 1, new_clauses, vars, verbose) is True:
                        return True

                    # Try other option. Don't waste time updating values if we've 
                    elif a != False:
                        partial[i] = None
    
    return False
                 
