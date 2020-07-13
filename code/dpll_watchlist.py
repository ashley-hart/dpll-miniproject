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

# Solve the problem with DPLL implemented with a watchlist.
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

    new_wl = [[lit for lit in c] for c in watchlist]

    # TODO: ADD UNIT PROPAGATION
    # TODO: ADD PURE LITERAL ELIMINATION

    for a in [True, False]:
        assignment[curr_var] = a

        if a == True:
            false_literal = variables[curr_var] * -1
        else:
            false_literal = abs(variables[curr_var])

        if verbose:
            print("false_literal:", false_literal)
            print("assignment:", assignment)
            print("curr_var:", curr_var)

        update_watchlist(new_wl, literals, variables, assignment, false_literal, curr_var, clauses, verbose)

        if new_wl[literals.index(false_literal)] != []:
            assignment[curr_var] = None
            continue

        if None not in assignment:
            return True

        if dpll(new_wl, clauses, assignment, literals, variables, curr_var + 1,  verbose):
            return True

        assignment[curr_var] = None
        new_wl = [[lit for lit in c] for c in watchlist]

    return False
                