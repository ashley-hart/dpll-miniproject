# Ashley Hart
# UVA Summer Research Project
# DPLL-SAT Solver Miniproject

'''
This is a cleaner implementation of DPLL that uses a watchlist to update values.
'''

# watchlist = []

def init_watchlist(literals, clauses):
    print("This function will initialize the watchlist.")
    wl = []

    return wl

# IDEA: Return a 2-tuple, one with the new watchlist and another with a bool
# that indicates if any changes were made.
def update_watchlist(watchlist, literals, clauses):
    print("This function will update the watchlist.")
    new_wl = []
    changed = False

    return (new_wl, changed)

def solve(problem):
    print("This function takes the problem and set's up values for dpll().")
    # Set up literals.
    # Set up clauses.
    # Set up assignment list.
    # Initalize watchlist.

    # Replace False with dpll() call.
    is_SAT = False

    return is_SAT 


def dpll(watchlist, clauses, assignment, literals, curr_var, verbose):

    # TODO: Reimplement unit propagation
    # TODO: Reimplement pure literal elimination
    # TODO: Adjust the recursive engine to update the watchlist after every assignment.

    # Consider - How do we know that a clause set is satisfied under an assignment?
    # If we don't need to change any values in the watchlist, then we have a satifying solution.

    print("This function performs dpll and returns a 2-tuple: (bool: is_SAT, list: solution)")

    return False


