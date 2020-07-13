# Ashley Hart
# Developed under the advisement of Dr. Matthew Dwyer, Mitchell Gerrard and Soneya Binta Houssain
# at the University of Virginia
# SAT Solver - Master Version

'''
This is my implementation of a SAT solver. Optimizations such as
unit propagation, pure literal elimination and more can be triggered
from the command line.

By default, the solver operates on a recursion based DPLL algorithim.
'''

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
        # print("CLAUSE_CHECK(): Given", t_vals)
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
        print("UPDATE T_VALS(): Returning:", new_vals)

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
        print("REDUCE_T_VALS(): Returning: ", new_vals)

    return new_vals

# Returns all unit clauses that have yet to be satisfied.
def get_unit_clauses(clauses, vars, partial, verbose):
    unit_clauses = []
    
    for c in clauses:
        index = vars.index(abs(c[0]))
        if len(c) == 1 and partial[index] == None:
            unit_clauses.append(c)
    
    if verbose:
        print("GET_UNIT_CLAUSES(): Returning:", unit_clauses)

    return unit_clauses

# Reduces clauses based on a literal if possible.
# Returns reduced clauses.
def unit_prop_helper(clauses, literal, verbose):

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
            temp = [lit for lit in c]

        new_clauses.append(temp)
        temp = []
            
    if verbose:
        print("UP_HELPER(): Returning", new_clauses)

    return new_clauses

# Perfrom unit propagation. Utilizes helper functions
def unit_propagation(clauses, vars, partial, verbose):
    new_clauses = [[lit for lit in c] for c in clauses]

    # Shrink clauses based on a previous assignment with unit propagation
    unit_clauses = get_unit_clauses(new_clauses, vars, partial, verbose)

    while unit_clauses:
        c = unit_clauses[0]
        index = vars.index(abs(c[0]))
        new_clauses = unit_prop_helper(new_clauses, c[0], verbose)

        if c[0] > 0:
            partial[index] = True
        else:
            partial[index] = False

        del unit_clauses[0]

        unit_clauses = get_unit_clauses(new_clauses, vars, partial, verbose)

    return new_clauses

# Reduce the clause set based on the assigned value of a literal.
# Makes individual clauses "shorter." Used by unit propagation and recursive reduction.
def remove_literal(clauses, literal, partial, verbose):

    new_clauses = []
    temp = []

    # Strip clauses
    for c in clauses:
            # If same assignment then remove clause
        if literal in c:
            continue
        for lit in c:
            # If opposing assignment, then remove literal
            if lit == (literal * -1):
                continue
            else:
                temp.append(lit)

        new_clauses.append(temp)
        temp = []
   
    if verbose:
        print("RM_LITERAL(): Reduction based on:", literal)
        print("RM_LITERAL(): Returning", new_clauses)

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

# Reduce a clause set based on the presence of a pure literal.
# Tries to remove clauses from the clause set. USed by pure literal elimination.
def reduce_clause_set(clauses, pure_lit, partial, verbose):
    new_clauses = [[lit for lit in c] for c in clauses]

    for c in clauses:
        if pure_lit in c:
            if len(clauses) == 1:
                new_clauses = []
            else:
                new_clauses.remove(c)

    if verbose:
        print("REDUCE_CLAUSE_SET(): Reducing on pure literal",  pure_lit)
        print("REDUCE_CLAUSE_SET(): Returning:", new_clauses)

    return new_clauses


# Perform pure literal elimination.
def pure_literal_elimination(clauses, vars, partial, verbose):

    # Attempt to reduce before we try to choose assignments.
    pure_lits = get_pure_literals(clauses, vars, partial, verbose)

    new_clauses = [[lit for lit in c] for c in clauses]

    while pure_lits:
        curr_lit = pure_lits[0]
        # If a pure literal is found, do the following:
        if pure_lits != []:

            # Reduce clause set
            new_clauses = reduce_clause_set(new_clauses, curr_lit, partial, verbose)

            # Update partial based on pure literals.
            for p in pure_lits:
                if p > 0:
                    partial[abs(p) - 1] = True
                else: 
                    partial[abs(p) - 1] = False
        
        del pure_lits[0]
        pure_lits = get_pure_literals(new_clauses, vars, partial, verbose)

    return new_clauses

def solve(problem, do_CR, do_UP, do_PLE):
    truth_values = [[None for lit in c if lit != 0] for c in problem.clauses]
    partial: list = []
    vars: list = []
    
    if problem.verbose:
        print("\n[SAT_SOLVER]: Attempting to satisfy the problem...")
        print("=======================================================================")

    for i in range(0, problem.num_vars):
        vars.append(i + 1)

    # Set up partial assignment.
    for i in range(0, problem.num_vars):
        partial.append(None)

    is_sat = solve_helper(truth_values, partial, 0, problem.clauses, vars, do_CR, do_UP, do_PLE, problem.verbose)

    if problem.verbose:
        print("[SAT_SOLVER]: Returning", is_sat)
        print("=======================================================================")

    return is_sat


# Returns True if SAT or False if UNSAT
def solve_helper(initial_t_vals, initial_partial, current_var, clauses, vars, do_CR, do_UP, do_PLE, verbose):
        
    t_vals = [[t_val for t_val in c] for c in initial_t_vals]
    partial = [partial for partial in initial_partial]
    new_clauses = [[lit for lit in c] for c in clauses]
    result = None

    if verbose:
        print("\nNEW CALL")
        print("=============================================================")

    # If enabled, perform pure literal elimination
    if do_UP:
        if verbose:
            print("UNIT PROPAGATION")
            print("===========================")
        # Perform unit propagation
        new_clauses = unit_propagation(clauses, vars, partial, verbose)
        
        if [] in new_clauses:
            return False 
        
        if verbose:
            print()
    
    # If enabled, perform pure literal elimination
    if do_PLE:
        if verbose:
            print("PURE LITERAL ELIMINATION")
            print("===========================")
 
        new_clauses = pure_literal_elimination(new_clauses, vars, partial, verbose)

        if new_clauses == []:
            return True

        if verbose:
            print()

    # Match size of t-vals to new clauses
    t_vals = reduce_t_vals(new_clauses, partial, t_vals, verbose)
    reduced_clauses = [[lit for lit in c] for c in new_clauses]

    # Base Case - Activated if we have a complete assignment.
    if None not in partial:
        if verbose:
            print("\nBase Case - complete assignment recieved.")

        t_vals = reduce_t_vals(new_clauses, partial, t_vals, verbose)
        return clause_check(t_vals, verbose)

    # Scan the partial assignment left to right and recursively try to
    # assign values to any remaining unassigned variables.
    for i in range(0, len(partial)):
        if partial[i] == None:

            # We will try to push true and false onto this for every variable.     
            for a in [True, False]:

                partial[i] = a

                if a == True:
                    literal = vars[i]
                else:
                    literal = vars[i] * -1
     
                if do_CR:
                    # Try to reduce clauses with current assignment.
                    reduced_clauses = remove_literal(new_clauses, literal, partial, verbose)
                    t_vals = reduce_t_vals(reduced_clauses, partial, t_vals, verbose)

                if verbose:
                    print("\nCHOOSING RECURSIVELY!")
                    print("============================")
                    print("a =", a)
                    print("partial assignment: ", partial)
                    print("t_vals before modification: ", t_vals)
                    print("new_clauses: ", new_clauses)

                # Define new truth values under partial assignment w/ potentially reduced clauses.
                t_vals = update_truthtable(t_vals, partial, current_var, reduced_clauses, verbose)
                result = clause_check(t_vals, verbose)

                # If True, send this result right back up.
                if result == True:

                    if verbose: 
                        print("\na =", a)
                        print("new_clauses =", new_clauses)
                        print("partial assignment: ", partial)
                        print("t_vals: ", t_vals)
                        print("[SAT_SOLVER]: Solution:", partial)
            
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

                    if solve_helper(t_vals, partial, current_var + 1, reduced_clauses, vars, do_CR, do_UP, do_PLE,  verbose) is True:
                        return True

                    # Try other option. Don't waste time updating values if we've 
                    elif a != False:
                        partial[i] = None
                        reduced_clauses = [[lit for lit in c] for c in new_clauses]
    
    return False
                 