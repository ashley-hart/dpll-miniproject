# Ashley Hart
# UVA Summer Research Project
# DPLL-SAT Solver Miniproject

'''
This is a cleaner implementation of DPLL that uses a watchlist to update values.
'''

import copy

def init_watchlist(literals, clauses, verbose):

    if verbose:
        print("\nINIT_WL(): This function will initialize the watchlist.")
        print("literals:", literals)
        print("clauses:", clauses)

    wl = []

    for i in range(len(literals)):
        wl.append([])

    for i in range(len(clauses)):

        if verbose:
            print("literals.index(clauses[",i,"][0]):", literals.index(clauses[i][0]))

        wl[literals.index(clauses[i][0])].append(clauses[i])

    return wl


def update_watchlist(watchlist, literals, variables, assignment, false_literal, curr_var, clauses, verbose):

    new_wl = copy.deepcopy(watchlist)
    changed = False

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
        print("assignment[",curr_var,"] =",assignment[curr_var])

    # Continue while we still have clauses looking at false_literal
    while new_wl[fl_index]:

        print("WORKING ROW = ", new_wl[fl_index])

        # For every clause in the sublist, try to "move" it somewhere else.
        clause = new_wl[fl_index][0]

        for lit in clause:

            # If we see a variable assigned to None or the negation of our 
            # false literal then we move the clause and record the change.
            # Should gloss over first index bc it shouldn't prompt an update.
            if assignment[abs(lit) - 1] == None or lit == false_literal * -1:

                del new_wl[fl_index][0]
                new_wl[literals.index(lit)].append(clause)
                changed = True

                if verbose:
                    print("Moved", clause, "to watchlist[",(literals.index(lit)),"]...")
                    print("NEW ROW: ", new_wl[literals.index(lit)])
                    # print("curr watchlist:", new_wl)

                break

        # If we cannot do this for any clause then we return False
        if not changed: 
            if verbose:
                print("UPDATE_WL(): Was unable to update watchlist under given assignment.")
                print("watchlist:", watchlist)
                print("literals:", literals)
                print("false literal:", false_literal)
                print("assignment:", assignment)
            return ([], False)

    return (new_wl, changed)


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

    watchlist = init_watchlist(literals, problem.clauses, problem.verbose)

    if problem.verbose:
        print("variables:", variables)
        print("literals:", literals)
        print("watchlist:", watchlist)
        print("assignment:", assignment)

    result = dpll(watchlist, problem.clauses, assignment, literals, variables, 0, problem.verbose)

    if problem.verbose:
        print("Final result:", result)

    return result


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
            else: 
                if lit > 0:
                    temp.append(False)
                if lit < 0:
                    temp.append(True)
        t_vals.append(temp)
        temp = []
    
    return (assignment, clause_check(t_vals, verbose))


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


def dpll(watchlist, clauses, assignment, literals, variables, curr_var,  verbose):

    # TODO: Reimplement unit propagation
    # TODO: Reimplement pure literal elimination
    # TODO: Adjust the recursive engine to update the watchlist after every assignment.

    false_literal: int = 0

    if curr_var >= len(variables):
        if verbose:
            print("Base Case")

        return (assignment, SAT_check(clauses, assignment, verbose))


    for a in [True, False]:

        assignment[curr_var] = a

        if a == True:
            false_literal = variables[curr_var] * -1
        else:
            false_literal = variables[curr_var]

        data = update_watchlist(watchlist, literals, variables, assignment, false_literal, curr_var, clauses, verbose)
        updated_wl = data[1]

        result = SAT_check(clauses, assignment, verbose)

        if verbose:
            print("assignment:", assignment)
            print("false_literal:", false_literal)
            print("SAT_check results:", result)
            
        if result[1] == True:
            return (assignment, True)
        elif updated_wl:
            data = dpll(watchlist, clauses, assignment, literals, variables, curr_var + 1, verbose)

            if data[1] == True:
                return (assignment, True)


    assignment[curr_var] = None

    return ([], False)


