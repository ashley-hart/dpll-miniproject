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
        print("CLAUSE_CHECK(): Given t_vals", t_vals)
        print("CLAUSE_CHECK(): Returning", is_SAT)

    return is_SAT

# Create a t_val set based on clauses and the current assignment.
# Replaces update_t_vals() and reduce_t_vals().
def SAT_check(clauses, partial, verbose):
    t_vals = []
    temp = []

    for c in clauses:
        for lit in c:
            index = abs(lit) -1
            if partial[index] == True:
                if lit > 0:
                    temp.append(True)
                else:
                    temp.append(False)
            elif partial[index] == False:
                if lit > 0:
                    temp.append(False)
                else:
                    temp.append(True)
            else:
                temp.append(None)

        t_vals.append(temp)
        temp = []

    if verbose:
        print("Passing on:", t_vals)

    return clause_check(t_vals, verbose)

# Reduce the clause set based on the assigned value of a literal.
# Makes individual clauses "shorter." Used by unit propagation and recursive reduction.
def remove_literal(clauses, literal, partial, verbose):

    new_clauses = []
    temp = []
    can_reduce = True

    # Strip clauses
    for c in clauses:
        # If same assignment then remove clause
        if literal in c:
            continue

        if can_reduce == False:
            break

        for lit in c:
            # If opposing assignment, then remove literal
            if lit == (literal * -1):
                if len(c) == 1:
                    can_reduce = False

                    if verbose:
                        print("Unremovable unit clause detected.")

                    break
                continue
            else:
                temp.append(lit)

        new_clauses.append(temp)
        temp = []
   
    if verbose:
        print("RM_LITERAL(): Reduction based on:", literal)
        print("RM_LITERAL(): Returning", new_clauses)

    return (new_clauses, can_reduce)

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
def unit_propagation(clauses, vars, partial, do_UP, verbose):

    if not do_UP:
        return clauses

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


# Reduce a clause set based on the presence of a pure literal.
# Tries to remove clauses from the clause set. USed by pure literal elimination.
def reduce_clause_set(clauses, pure_lit, partial, verbose):

    for c in clauses:
        if pure_lit in c:
            if len(clauses) == 1:
                clauses = []
            else:
                clauses.remove(c)

    if verbose:
        print("REDUCE_CLAUSE_SET(): Reducing on pure literal",  pure_lit)
        print("REDUCE_CLAUSE_SET(): Returning:", clauses)

    return clauses

# Scan the clauses and return a list of pure literals.
def get_next_pure_lit(clauses, vars, partial, verbose):
    pure = []
    literals = []

    # NOTE: Remove the break statement to allow this function to grab every pure literal.
    # Scan clauses and toss in every literal.
    for c in clauses:
        for lit in c:
            if lit not in literals and partial[abs(lit) -1] == None:
                literals.append(lit)  

    # Check for purity and add to pure list
    for l in literals:
        index = vars.index(abs(l))
        if (l * -1) not in literals and partial[index] == None:
            pure.append(l)
            break

    if verbose:
        print("GET_PURE_LITS(): given literals: ", literals)
        print("GET_PURE_LITS(): pure literals: ", pure)

    return pure

# Perform pure literal eliminaiton. This function is currently slowing down
# the runtime in a major way. 
def ple(clauses, vars, partial, do_PLE, verbose):
    if not do_PLE:
        return clauses

    # Grab the next pure literal, if there is one.
    pure = get_next_pure_lit(clauses, vars, partial, verbose)

    # Operate as long as there are pure literals to get from the clauses.
    while pure:
        curr_lit = pure[0]

        # If a pure literal is found, reduce the clause set...
        i = 0
        while i < len(clauses):
            if curr_lit in clauses[i]:
                clauses.remove(clauses[i])
                i -= 1
            i += 1

        index = vars.index(abs(curr_lit))

        # ...and update the partial assignment
        if curr_lit > 0:
            partial[index] = True
        else:
            partial[index] = False

        # Remove this pure literal when we finish with it and grab the next one.
        del pure[0]
        pure = get_next_pure_lit(clauses, vars, partial, verbose)

    if verbose:
        print("PLE RETURNING:", clauses)
    return clauses

# Returns a 2-tuple: (reduced-clauses, reducible)
def clause_reduction(assignment, vars, i, partial, clauses, verbose):

    if assignment == True:
        literal = vars[i]
    else:
        literal = vars[i] * -1

    return remove_literal(clauses, literal, partial, verbose)


# Attemot to solve the problem.
def solve(problem, do_CR, do_UP, do_PLE):
    partial: list = []
    vars: list = []
    
    if problem.verbose:
        print("\n[SAT_SOLVER]: Attempting to satisfy the problem...")
        print("=======================================================================")

    # Set up vars list and partial assignment
    for i in range(0, problem.num_vars):
        vars.append(i + 1)
        partial.append(None)   

    is_sat = solve_helper(partial, 0, problem.clauses, vars, do_CR, do_UP, do_PLE, problem.verbose)

    if problem.verbose:
        print("[SAT_SOLVER]: Returning", is_sat)
        print("=======================================================================")

    return is_sat


def solve_helper(initial_partial, curr_var, clauses, vars, do_CR, do_UP, do_PLE, verbose):
    result = None
    partial = [p for p in initial_partial]
    curr_clauses = [[lit for lit in c] for c in clauses]

    if verbose:
        print("\nNEW CALL")
        print("=============================================================")
        print("partial:", initial_partial)
        print("clauses:", clauses)

    if do_PLE:
        if verbose:
            print("PURE LITERAL ELIMINATION")
            print("===========================")
            print("Given clauses:", clauses)

        clauses = ple(clauses, vars, initial_partial, do_PLE, verbose)

        if clauses == []:
            if verbose:
                print("PLE RETURNING TRUE EARLY!")
                print("partial:", initial_partial)
            return True

        if verbose:
            print("PLE PRODUCED CLAUSES:", clauses)
            print()    

    # Force a stop if we have a complete assignment.
    if None not in initial_partial:
        if verbose:
            print("BASE CASE - Complete assignment reached.")
        return SAT_check(clauses, initial_partial, verbose)

    # Try to find a satisfying solution for every variable that has not been given a fixed value.
    for i in range(0, len(initial_partial)):
        if initial_partial[i] == None:
            for a in [True, False]:

                # Update partial assignment
                partial[i] = a

                if verbose:
                    print() 
                    print("assignment =", a)
                    print("clauses =", curr_clauses)
                    print("partial assignment: ", partial)

                # If enabled, attempt to reduce the clauses with every change to the assignment
                if do_CR:
                    if verbose:
                        print("\nCLAUSE REDUCTION!")
                        print("============================")
                        print("partial:", partial)

                    # Try to reduce clauses with current assignment.
                    # retval is a 2-tuple. The 0th index holds the reduced clauses
                    # and the 1st holds a boolean that lets us know if we successfully
                    # reduced the clause set.
                    retval = clause_reduction(a, vars, i, partial, clauses, verbose)

                    # If we did not reduce the clause set, discard this assignment and move on. 
                    # Continuing down this path won't be productive.
                    if retval[1] == False:
                        continue

                    # If we did reduce the clause set, set curr_clauses to the reduced clause set. 
                    curr_clauses = retval[0]

                result = SAT_check(curr_clauses, partial, verbose)

                # If True or False, return right away.
                if result == True:
                    if verbose:
                        print("[SAT_SOLVER]: Solution:", partial)

                    return True
                elif result == False:
                    if verbose:
                        print("Backing up...") 

                    return False
                # If None, try to change course.
                else: 
                    if verbose:
                        print("Going down...")

                    # Go deeper with another call, if we get True then return True.
                    if solve_helper(partial, curr_var + 1, curr_clauses, vars, do_CR, do_UP, do_PLE,  verbose):
                        return True
                    # Otherwise try the other assignment option. 
                    elif a != False:
                        partial[i] = None
                        curr_clauses = [[lit for lit in c] for c in clauses]
            
    return False
