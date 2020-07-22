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

import sys

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
        print("CLAUSE_CHECK(): Returning", is_SAT)
        print("CLAUSE_CHECK(): Given", t_vals)

    return is_SAT

# Create a t_val set based on clauses and the current assignment.
# Replaces update_t_vals() and reduce_t_vals().
def SAT_check(clauses, partial, verbose):

    t_vals = [[True if (partial[abs(lit)-1] == True and lit > 0) else False if (partial[abs(lit)-1] == True and lit < 0)
    else True if (partial[abs(lit)-1] == False and lit < 0) else False if (partial[abs(lit)-1] == False and lit > 0) 
    else None for lit in c] for c in clauses]

    # This is an alternative version of this function that would (hopefully) eliminate
    # the need for clause_check()
    # is_SAT = True

    # for c in clauses:
    #     seen_True  = False
    #     seen_None = False
    #     for lit in c:
    #         if lit > 0:
    #             if partial[lit - 1] == True:
    #                 seen_True = True
    #                 continue
    #         elif lit < 0:
    #             if partial[abs(lit) - 1] == False:
    #                 seen_True = True
    #                 continue
    #         if partial[abs(lit) - 1] == None:
    #             seen_None = True
            
    #     if seen_True == False:
    #         if seen_None == True:
    #             is_SAT = None
    #         else:    
    #             is_SAT = False
    #         break

    return clause_check(t_vals, verbose)

# Reduce the clause set based on the assigned value of a literal.
# Makes individual clauses "shorter." Used by unit propagation and recursive reduction.
def remove_literal(clauses, literal, partial, verbose):
    
    new_clauses = [[lit for lit in c if (lit != literal*-1)] for c in clauses if literal not in c]
   
    if verbose:
        print("RM_LITERAL(): Reduction based on:", literal)
        print("RM_LITERAL(): Returning", new_clauses)

    return new_clauses

# Reduce a clause set based on the presence of a pure literal.
# Tries to remove clauses from the clause set. Used by pure literal elimination.
def reduce_clause_set(clauses, pure_lit, partial, verbose):

    reduced_clauses = [c for c in clauses if pure_lit not in c]

    if verbose:
        print("REDUCE_CLAUSE_SET(): Reducing on pure literal",  pure_lit)
        print("REDUCE_CLAUSE_SET(): Returning:", reduced_clauses)

    return reduced_clauses

# Returns all unit clauses that have yet to be satisfied.
def get_unit_clauses(clauses, verbose):
    unit_clauses = [c for c in clauses if len(c) == 1]
    
    if verbose:
        print("GET_UNIT_CLAUSES(): Returning:", unit_clauses)

    return unit_clauses

# Perfrom unit propagation. Utilizes helper functions
def unit_propagation(clauses, vars, partial, do_UP, verbose):
    if not do_UP:
        return clauses

    # Shrink clauses based on a previous assignment with unit propagation
    unit_clauses = get_unit_clauses(clauses, verbose)

    while unit_clauses:
        c = unit_clauses[0]
        clauses = remove_literal(clauses, c[0], partial, verbose)

        # ...and update the partial assignment
        index = vars.index(abs(c[0]))
        if c[0] > 0:
            partial[index] = True
        else:
            partial[index] = False

        del unit_clauses[0]
        unit_clauses = get_unit_clauses(clauses, verbose)

    if verbose:
        print("UP RETURNING:", clauses)
        print("UP PARTIAL:", partial)

    return clauses

# Grabs and returns a set of pure literals. 
def get_pure_lits(clauses, verbose):
    pure_literals = []
    flat_list = [item for sublist in clauses for item in sublist]
    list_of_literals = list(set(flat_list))

    for l in list_of_literals:
        if (not(negate(l) in list_of_literals)):
            pure_literals.append(l)

    if verbose:
        print("GET_PLS(): Clauses:", clauses)
        print("GET_PLS(): Returning:", pure_literals)

    return pure_literals

# Negates a given literal.
def negate(l):
    return l*(-1)
    
# Perform pure literal eliminaiton. This function is currently slowing down
# the runtime in a major way. 
def ple(clauses, vars, partial, do_PLE, verbose):
    if not do_PLE:
        return clauses

    # Grab the next pure literal, if there is one.
    pure = get_pure_lits(clauses, verbose)

    # Operate as long as there are pure literals to get from the clauses.
    while pure:
        curr_lit = pure[0]

        clauses = reduce_clause_set(clauses, curr_lit, partial, verbose)

        # ...and update the partial assignment
        index = vars.index(abs(curr_lit))
        if curr_lit > 0:
            partial[index] = True
        else:
            partial[index] = False

        # Remove this pure literal when we finish with it and grab the next one.
        del pure[0]
        # pure = get_pure_lits(clauses, verbose)

    if verbose:
        print("PLE RETURNING:", clauses)
        print("PLE adjusted partial to:", partial)
    return clauses

# Returns a reduced clause set based on a literal.
def clause_reduction(assignment, vars, i, partial, clauses, verbose):

    if assignment == True:
        literal = vars[i]
    else:
        literal = vars[i] * -1

    return remove_literal(clauses, literal, partial, verbose)

# Attempt to solve the problem.
def solve(problem, do_CR, do_UP, do_PLE):
    partial: list = []
    vars: list = []
    
    sys.setrecursionlimit(10**6) 

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
    partial = [p for p in initial_partial]
    result = None

    if verbose:
        print("\nNEW CALL")
        print("=============================================================")
        print("partial:", partial)
        print("clauses:", clauses)

    if verbose and do_UP:
        print("UNIT PROPAGATION")
        print("===========================")

    # Perform unit propagation
    clauses = unit_propagation(clauses, vars, partial, do_UP, verbose)

    if [] in clauses:
        if verbose:
            print("UP RETURNING FALSE EARLY!")
        return False 
    
    if verbose and do_PLE:
        print("PURE LITERAL ELIMINATION")
        print("===========================")
        print("Given clauses:", clauses)

    clauses = ple(clauses, vars, partial, do_PLE, verbose)

    if len(clauses) == 0:
        print("PLE RETURNING TRUE EARLY!")
        print("partial:", partial)
        print("clauses:", clauses)
        # if verbose:

        return True

    # Force a stop if we have a complete assignment.
    if None not in partial:
        if verbose:
            print("BASE CASE - Complete assignment reached.")
        return SAT_check(clauses, partial, verbose)
    
    curr_clauses = [[lit for lit in c] for c in clauses]

    # Try to find a satisfying solution for every variable that has not been given a fixed value.
    for i in range(0, len(partial)):
        if initial_partial[i] == None:
            for a in [True, False]:

                # Update partial assignment
                partial[i] = a

                if verbose:
                    print() 
                    print("clauses =", curr_clauses)
                    print("assignment =", a)
                    print("partial assignment: ", partial)

                # Try to reduce clauses with current assignment.
                curr_clauses = clause_reduction(a, vars, i, partial, curr_clauses, verbose)

                if [] in curr_clauses:
                    # print("Bad reduction, continuing on....")
                    continue

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
