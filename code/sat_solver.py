# Ashley Hart
# Developed under the advisement of Dr. Matthew Dwyer, Mitchell Gerrard and Soneya Binta Houssain
# at the University of Virginia
# SAT Solver - Master Version

'''
This is my implementation of a SAT solver. Optimizations such as
unit propagation, pure literal elimination and more can be triggered
from the command line.

By default, the solver operates on a recursion based DPLL algorithim.

Many thanks to Mitchell for his guidance during the development of this code.
'''

import sys

# Returns all unit clauses that have yet to be satisfied.
def get_unit_clauses(formula, verbose):
    unit_clauses = [c for c in formula if len(c) == 1]
    
    if verbose:
        print("GET_UNIT_CLAUSES(): Returning:", unit_clauses)

    return unit_clauses

# Grabs and returns a set of pure literals. 
def get_pure_lits(clauses, verbose):
    pure_literals = []
    flat_list = [item for sublist in clauses for item in sublist]
    list_of_literals = list(set(flat_list))

    for l in list_of_literals:
        if (not(negate(l) in list_of_literals)):
            pure_literals.append(l)

    if verbose:
        print("GET_PLS(): Returning:", pure_literals)

    return pure_literals

# Negates a given literal.
def negate(l):
    return l*(-1)

# Given some literal, reduce the clause set in the following ways:
#   - If l appears in a clause, remove the clause
#   - If neg(l) appears in a clause, remove neg(l)
def clause_reduction(literal, formula):

    if literal == 0:
        return formula

    new_formula = []

    for clause in formula:
        if literal in clause:
            continue
        elif negate(literal) in clause:
            new_clause = [lit for lit in clause if lit != negate(literal)]
            new_formula.append(new_clause)
        else: 
            new_formula.append(clause)
    
    return new_formula

# Perfrom unit propagation. Utilizes helper functions
def unit_propagation(literal, formula):
    return clause_reduction(literal, formula)

# Perform pure literal eliminaiton. This function is currently slowing down
# the runtime in a major way. 
def ple(literal, formula):
    return clause_reduction(literal, formula)

def get_literal(formula):
    flat_list = [item for sublist in formula for item in sublist]

    if flat_list:
        return flat_list[0]
    else:
        return 0

# Attempt to solve the problem.
def solve(problem, do_UP, do_PLE):
    # Support recursion depth for larger benchmarks
    sys.setrecursionlimit(10**6) 

    if problem.verbose:
        print("\n[SAT_SOLVER]: Attempting to satisfy the problem...")
        print("=======================================================================")

    is_sat = solve_helper(problem.formula, do_UP, do_PLE, problem.verbose)

    if problem.verbose:
        print("[SAT_SOLVER]: Returning", is_sat)
        print("=======================================================================")

    return is_sat

def solve_helper(formula, do_UP, do_PLE, verbose):

    # Base Cases
    if len(formula) == 0:
        return True
    if [] in formula:
        return False

    if do_UP:
        unit_clauses = get_unit_clauses(formula, verbose)

        for l in unit_clauses:
            formula = unit_propagation(l, formula)

        if verbose:
            print("UNIT PROPAGATION")
            print("Reduced formula:", formula)

    if do_PLE:
        pure_literals = get_pure_lits(formula, verbose)

        for l in pure_literals:
            formula = ple(l, formula)

        if verbose:
            print("PURE LITERAL ELIMINATION")
            print("Reduced formula:", formula)
   
    literal = get_literal(formula)

    return (solve_helper(clause_reduction(literal, formula), do_UP, do_PLE, verbose) or 
            solve_helper(clause_reduction(negate(literal), formula), do_UP, do_PLE, verbose))
            