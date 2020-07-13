# Ashley Hart
# UVA Summer Research Project
# DPLL-SAT Solver Miniproject

import time
import dpll
import dpll_watchlist
import lit_elim
import recursive
import sys 
import unit_prop
import sat_solver
from problem import Problem

class Solver:

    num_variables = -1
    num_clauses = -1
    clauses = []
    flag = ""
    problem = None
    silent = None
    verbose = None

    # Data collection variables. 
    branch_count = 0
    time = 0

    def __init__(self, filename, flag, silent, problem):
        self.filename = filename
        self.flag = flag
        self.silent = silent
        self.problem = problem
        self.verbose = problem.verbose

    def solve(self):
        dpll_w_SAT: bool = False

        # Determines if we do a clause reduction per call.
        do_CR = None 
        do_UP = None
        do_PLE = None

        # If no flag is given solver defaults to DPLL.
        if self.flag == "":
            self.flag = "--dpll"

        # Use recursive approach.
        if self.flag == "--recursive" or self.flag == "-r":
            if self.verbose: 
                print("--recursive flag recieved")
            do_CR = True
            do_UP = False
            do_PLE = False
        # Use unit propagation approach.
        elif self.flag == "--unit-prop" or self.flag == "-u":
            if self.verbose:
                print("--unit-prop flag received")

            do_CR = True
            do_UP = True
            do_PLE = False

        # Use pure literal elimination approach. 
        elif self.flag == "--lit-elim" or self.flag == "-l":
            if self.verbose:
                print("--lit-elim flag receieved")

            do_CR = True
            do_UP = False
            do_PLE = True

        # Use DPLL algorithm approach.
        elif self.flag == "--dpll" or self.flag == "-d":
            if self.verbose:
                print("--dpll flag recieved")

            do_CR = True
            do_UP = True
            do_PLE = True

        # Use DPLL with watchlist approach.
        elif self.flag == "--dpll-w" or self.flag == "-dw":
            if self.verbose:
                print("--dpll-w flag recieved")

            return dpll_watchlist.solve(self.problem)

            # if self.silent:
            #     if dpll_w_SAT == False: 
            #         print("DPLL w/ watchlist approach failed to find a solution.")
            #     else: 
            #         print("DPLL w/ watchlist approach found a solution.")
        else:
            flag_input = str(self.flag)
            print("Given flag: *" + flag_input + "*")
            print("Flag not recognized. Please verify your input.")    

        return sat_solver.solve(self.problem, do_CR, do_UP, do_PLE)


def main():

    flag = ""
    verbose = False
    silent = True

    # Process command line arguments
    # Silence enabled by default
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    elif len(sys.argv) == 3:
        filename = sys.argv[1]
        if sys.argv[2] == "--verbose" or sys.argv[2] == "-v":
            verbose = True
            silent = False
            flag = ""
        elif sys.argv[2] == "--silent" or sys.argv[2] == "-s":
            # silent = True
            flag = ""
        else:
            flag = sys.argv[2]
    elif len(sys.argv) == 4:
        filename = sys.argv[1]
        flag = sys.argv[2]    
        if sys.argv[3] == "--verbose" or sys.argv[3] == "-v":
            verbose = True
            silent = False
        elif sys.argv[2] == "--silent" or sys.argv[2] == "-s":
            pass
        else:
            pass
    else:
        print("Invalid input detected.")
        print("Please adhere to the following format: \"solver.py filename opt:verbose\" ")
        sys.exit("Terminating process.")

    problem = Problem(filename, verbose)
    s = Solver(filename, flag, silent, problem)
    
    if verbose:
        problem.pretty_print()

    # Attempt to solve the problem and track how long it takes
    start = time.time()
    is_SAT = s.solve()
    end = time.time()
    solve_time = str(round((end-start), 5))

    result = ""

    if is_SAT:
        result = "SAT"
    else:
        result = "UNSAT"
    print("[SAT_SOLVER]: " + result)
    print("[SAT_SOLVER]: Solving took " + solve_time + " seconds")

    if verbose:
        print("[SAT_SOLVER]: Terminating process")

if __name__ == "__main__":
    main()

