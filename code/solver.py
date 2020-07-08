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

 
    # Controls which solving approches will be used.
    def solve(self):

        recur_SAT: bool = False
        up_SAT: bool = False
        le_SAT: bool = False
        dpll_SAT: bool = False
        dpll_w_SAT: bool = False

        if self.verbose:
            print("\nSOLVER: Attempting to solve " + self.filename)
            print("=======================================================================")

        if self.verbose: 
            if self.flag == "":
                print("flag: NO FLAG GIVEN")
            else:
                print("flag: *" + self.flag + "*")

        # If no flag is given solver defaults to DPLL.
        if self.flag == "":
            self.flag = "--dpll"

        # Use recursive approach.
        if self.flag == "--recursive" or self.flag == "-r":
            if self.verbose: 
                print("--recursive flag recieved")

            recur_SAT = recursive.solve(self.problem)

            if self.silent:
                if recur_SAT == False: 
                    print("Recursive approach failed to find a solution.")
                else:
                    print("Recursive approach found a solution.")

        # Use unit propagation approach.
        elif self.flag == "--unit-prop" or self.flag == "-u":
            if self.verbose:
                print("--unit-prop flag received")

            up_SAT = unit_prop.solve(self.problem)

            if self.silent:
                if up_SAT == False: 
                    print("Unit propagation approach failed to find a solution.")
                else: 
                    print("Unit propagation approach found a solution.")

        # Use pure literal elimination approach. 
        elif self.flag == "--lit-elim" or self.flag == "-l":
            if self.verbose:
                print("--lit-elim flag receieved")

            le_SAT = lit_elim.solve(self.problem)

            if self.silent:
                if le_SAT == False: 
                    print("Pure literal elimination approach failed to find a solution.")
                else: 
                    print("Pure literal elimination approach found a solution.")

        # Use DPLL algorithm approach.
        elif self.flag == "--dpll" or self.flag == "-d":
            if self.verbose:
                print("--dpll flag recieved")

            dpll_SAT = dpll.solve(self.problem)

            if self.silent:
                if dpll_SAT == False: 
                    print("DPLL approach failed to find a solution.")
                else: 
                    print("DPLL approach found a solution.")

        # Use DPLL with watchlist approach.
        elif self.flag == "--dpll-w" or self.flag == "-dw":
            if self.verbose:
                print("--dpll-w flag recieved")

            dpll_w_SAT = dpll_watchlist.solve(self.problem)

            if self.silent:
                if dpll_w_SAT == False: 
                    print("DPLL w/ watchlist approach failed to find a solution.")
                else: 
                    print("DPLL w/ watchlist approach found a solution.")

        # Use everything.        
        elif self.flag == "--all" or self.flag == "-a":
            if self.verbose:
                print("--all flag recieved")
                print("Using all of the methods.")

            recur_SAT = recursive.solve(self.problem)
            up_SAT = unit_prop.solve(self.problem)
            le_SAT = lit_elim.solve(self.problem)
            dpll_SAT = dpll.solve(self.problem)
            dpll_w_SAT = dpll_watchlist.solve(self.problem)

            if self.silent:
                if recur_SAT == False: 
                    print("Recursive approach failed to find a solution.")
                else: 
                    print("Recursive approach found a solution.")

                if up_SAT == False: 
                    print("Unit propagation approach failed to find a solution.")
                else: 
                    print("Unit propagation approach found a solution.")
                
                if le_SAT == False:
                    print("Pure literal elimination approach failed to find a solution.")
                else:
                    print("Pure literal elimination approach found a solution.")

                if dpll_SAT == False: 
                    print("DPLL approach failed to find a solution.")
                else: 
                    print("DPLL approach found a solution.")

                if dpll_w_SAT == False: 
                    print("DPLL w/ watchlist approach failed to find a solution.")
                else: 
                    print("DPLL w/ watchlist approach found a solution.")
        else:
            flag_input = str(self.flag)
            print("Given flag: *" + flag_input + "*")
            print("Flag not recognized. Please verify your input.")    


def main():

    flag = ""
    verbose = False
    silent = False

    # Process command line arguments
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    elif len(sys.argv) == 3:
        filename = sys.argv[1]
        if sys.argv[2] == "--verbose" or sys.argv[2] == "-v":
            verbose = True
            flag = ""
        elif sys.argv[2] == "--silent" or sys.argv[2] == "-s":
            silent = True
            flag = ""
        else:
            flag = sys.argv[2]
    elif len(sys.argv) == 4:
        filename = sys.argv[1]
        flag = sys.argv[2]
        
        if sys.argv[3] == "--verbose" or sys.argv[3] == "-v":
            verbose = True
        elif sys.argv[2] == "--silent" or sys.argv[2] == "-s":
            silent = True
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

    # Attempt to solve the problem
    start = time.time()
    s.solve()
    end = time.time()
    solve_time = str(round((end-start),5))
    # solve_time = str(end-start)
    print("solving took: "+solve_time+" seconds")

    if verbose:
        print("SOLVER(): Terminating process.")

if __name__ == "__main__":
    main()

