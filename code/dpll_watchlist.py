# Ashley Hart
# UVA Summer Research Project
# DPLL-SAT Solver Miniproject

'''
This is a cleaner implementation of DPLL that uses a watchlist to update values.
'''

import copy

# Setup watchlist
def init_watchlist(literals, clauses, verbose):

    if verbose:
        print("\nINIT_WL(): This function will initialize the watchlist.")
        print("literals:", literals)
        print("clauses:", clauses)

    wl = []

    for i in range(len(literals)):
        wl.append([])

    for i in range(len(clauses)):
        wl[literals.index(clauses[i][0])].append(clauses[i])

    return wl

# Returns False if it is impossible to update watclist under an assignment.
def update_watchlist(watchlist, literals, variables, assignment, false_literal, curr_var, clauses, verbose):

    # Find index of sublist we need to access.
    fl_index = literals.index(false_literal)

    if verbose:
        print("\nUPDATE_WL(): This function will update the watchlist.")
        print("initial watchlist:", watchlist)
        print("literals:", literals)
        print("false literal:", false_literal)
        print("false literal index:", fl_index)
        print("assignment:", assignment)
        print("curr_var:", curr_var)

    # Relocate all clauses watching false_literal.
    while watchlist[fl_index]:

        clause = watchlist[fl_index][0]
        changed = False

        for lit in clause:
            if assignment[abs(lit) - 1] == None or lit == false_literal * -1:

                if verbose:
                    print("Deleted: ", watchlist[fl_index][0])
                    print("Moved", clause, "to watchlist[",(literals.index(lit)),"]...")
                    print("Current watchlist:", watchlist)

                del watchlist[fl_index][0]
                watchlist[literals.index(lit)].append(clause)
                changed = True  
                break

        # If we cannot eliminate a clause that is watching false_literal, return False
        if not changed: 
            if verbose:
                print("ERROR - UPDATE_WL(): Was unable to update watchlist under given assignment.")
                print("watchlist:", watchlist)
                print("literals:", literals)
                print("variables:", variables)
                print("false literal:", false_literal)
                print("assignment:", assignment)
                print()
            return False

    return True

# Checks if truth values are SAT or UNSAT.
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

# Sets up the truth values and passes them to clause check.
def SAT_check(clauses, assignment, verbose):
    t_vals = []
    temp = []

    for c in clauses:
        for lit in c:
            if assignment[abs(lit) - 1] == True:
                if lit > 0:
                    temp.append(True)
                if lit < 0:
                    temp.append(False)
            elif assignment[abs(lit) - 1] == False: 
                if lit > 0:
                    temp.append(False)
                if lit < 0:
                    temp.append(True)
            else:
                temp.append(None)

        t_vals.append(temp)
        temp = []
    
    return clause_check(t_vals, verbose)


def solve(problem):

    literals = []
    variables = []
    assignment = []

    for c in problem.clauses:
        for lit in c:
            if abs(lit) not in variables:
                variables.append(abs(lit))
                assignment.append(None)

                if lit < 0:
                    literals.append(abs(lit))
                    literals.append(lit)
                else:
                    literals.append(abs(lit))
                    literals.append(lit * -1)

    literals.sort(key=abs)
    variables.sort()

    watchlist = init_watchlist(literals, problem.clauses, problem.verbose)

    if problem.verbose:
        print("variables:", variables)
        print("literals:", literals)
        print("watchlist:", watchlist)
        print("assignment:", assignment)

    result = dpll(watchlist, problem.clauses, assignment, literals, variables, 0, problem.verbose)

    if problem.verbose:
        print("Final result:", result)
        print("result:", result)

    return result


def dpll(watchlist, clauses, assignment, literals, variables, curr_var,  verbose):

    false_literal = 0

    # NOTE: Might be uneccessary.
    if curr_var == (len(variables)):
        return SAT_check(clauses,assignment, verbose)

    for a in [True, False]:
        assignment[curr_var] = a

        if a == True:
            false_literal = variables[curr_var] * -1
        else:
            false_literal = abs(variables[curr_var])


        result = SAT_check(clauses, assignment, verbose)

        if verbose:
            print("false_literal:", false_literal)
            print("assignment:", assignment)
            print("curr_var:", curr_var)

        # If we find a satisfiyng argument then we don't need to go any further
        if result == True:
            return True
        # If it is unknown if our assignment is SAT or UNSAT then we check if we can 
        # update our watchlist and try to make another call.
        elif result == None:
            # If we can update our watchlist then we still have a working assignment
            if update_watchlist(watchlist, literals, variables, assignment, false_literal, curr_var, clauses, verbose):
                if dpll(watchlist, clauses, assignment, literals, variables, curr_var + 1, verbose) is True:
                    return True
                else: 
                    assignment[curr_var] = None
        # If we know our assignment is UNSAT, try the other option before failing out.
        else:
            assignment[curr_var] = None

    return False
                

