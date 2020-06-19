# # Ashley Hart
# # UVA Summer Research Project
# # DPLL-SAT Solver Miniproject

import sys
import solver 
import parse
 
# TIMEOUT = -1 --> will use after solution is written and tested

# The idea with this is that if we never ever see a positive (aka) true integer, then the clause is unsatisfed.
# IMPORTANT: This is terribly broken. Will rewrite.
def check_clause_sat(base_clauses):

    is_sat: bool = False

    # If AT LEAST ONE literal in the clause is true then we set is_sat to true (by disjunction)
    # but this isn't good enough.
    for clause in base_clauses:
        for literal in clause:
            if literal >= 0:
                is_sat = True

    return is_sat

# Updates literals with a set of assignments, passes it on to be checked by 
# check_clause_sat()
def sat_check(clauses, assignments):

    # Make a copy to avoid corruption.
    new_clauses = clauses.copy()

    # For every integer in an assignment array, update all corresponding
    # literals by multiplying it by -1 or 1.
    for i in range (1, (len(assignments) + 1)):
        for clause in new_clauses:
            for literal in clause:

                if (literal is i) or (literal is (i * -1)):
                    literal = literal * assignments[i - 1]
              
        i += 1


    # Use these to see if the two sets of clauses have changed.
    '''
    print("BASE CLAUSES():")
    for r in clauses:
        for c in r:
            if c != 0:
                print(c, " ", end="")
            else:
                print(c, end="")
        print()

    print("NEW CLAUSES(): ")
    print("assignments = ", assignments)
    for r in new_clauses:
        for c in r:
            if c != 0:
                print(c, " ", end="")
            else:
                print(c, end="")
        print()

     '''   

    # check_clause_sat(new_clauses)


# Wrapper function
def solve(num_vars, num_clauses, base_clauses):

    clauses: list = base_clauses
    literals: list = [] 
    assignments: list = []
    SAT_set: list = []

    i = 1

    # The zero ('0') assignment means that a value has not been assigned yet.
    # -1 is false and 1 is true
    while i < num_vars:
        literals.append(i)
        assignments.append(0)
        i += 1

    # Controls number of iterations 
    limit: int = len(literals)

    # IMPORTANT: This is here for testing purposes only! 
    # There is an issue with this function as it does not update literals.
    sat_check(base_clauses, [1,-1, 1])

    # Get solution set
    SAT_set = solve_main(num_vars, num_clauses, clauses, 0, assignments, limit, SAT_set)

    # As of now, this just prints every combination of literals
    for sols in SAT_set:
        print(sols)



# Recursive function -
# IMPORTANT: This fucntion is currently set up to find too many solutions 
def solve_main(num_vars, num_clauses, clauses, curr_index, assignments, limit, SAT_set):

    # Base case
    #   - Check clause results with given assignments
    #   - Add assignments to solutions list if sat, reject if unsat 
    if curr_index is limit:

        if check_clause_sat(clauses) is True:
            SAT_set.append(assignments)

        return SAT_set

    # Generate moves
    t_branch = assignments.copy()
    t_branch[curr_index] = 1

    f_branch = assignments.copy()
    f_branch[curr_index] = -1

    # Change states via two-way branching. (Will need to count how many times we do this later.)
    # See if either branch has come up with any solutions and add them
    SAT_set = solve_main(num_vars, num_clauses, clauses, curr_index + 1, t_branch, limit, SAT_set)
    SAT_set = solve_main(num_vars, num_clauses, clauses, curr_index + 1, f_branch, limit, SAT_set)

    # Return all the solutions we've found
    return SAT_set
