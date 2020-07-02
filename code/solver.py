# Ashley Hart
# UVA Summer Research Project
# DPLL-SAT Solver Miniproject

import dpll
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

    verbose = None

    # Data collection variables. 
    branch_count = 0
    time = 0

    def __init__(self, filename, flag, problem):
        self.filename = filename
        self.flag = flag
        self.problem = problem
        self.verbose = problem.verbose


    # My intention for this function is to have it be the "Sorting Hat" of this class.
    # Will return data for analysis.
    def solve(self):

        recur_SAT: bool = False
        up_SAT: bool = False
        le_SAT: bool = False
        dpll_SAT: bool = False

        if (self.verbose):
            print("\nSOLVER: Attempting to solve " + self.filename)
            print("=======================================================================")

        if self.verbose: 
            if self.flag == "":
                print("flag: NO FLAG GIVEN")
            else:
                print("flag: *" + self.flag + "*")

        # Attempt all four methods
        if self.flag == "":

            if self.verbose:
                print("Using all of the methods.")

            recur_SAT = recursive.solve(self.problem)
            up_SAT = unit_prop.solve(self.problem)
            le_SAT = lit_elim.solve(self.problem)
            dpll_SAT = dpll.solve(self.problem)

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

        # Use recursive approach
        elif self.flag == "--recursive" or self.flag == "-r":
            if self.verbose: 
                print("--recursive flag recieved")

            recur_SAT = recursive.solve(self.problem)

            if recur_SAT == False: 
                print("Recursive approach failed to find a solution.")
            else:
                print("Recursive approach found a solution.")

        # Use unit propagation approach
        elif self.flag == "--unit-prop" or self.flag == "-u":
            if self.verbose:
                print("--unit-prop flag received")

            up_SAT = unit_prop.solve(self.problem)

            if up_SAT == False: 
                print("Unit propagation approach failed to find a solution.")
            else: 
                print("Unit propagation approach found a solution.")

        # Use pure literal elimination approach        
        elif self.flag == "--lit-elim" or self.flag == "-l":
            if self.verbose:
                print("--lit-elim flag receieved")

            le_SAT = lit_elim.solve(self.problem)

            if le_SAT == False: 
                print("Pure literal elimination approach failed to find a solution.")
            else: 
                print("Pure literal elimination approach found a solution.")

        # Use DPLL algorithm approach
        elif self.flag == "--dpll" or self.flag == "-d":
            if self.verbose:
                print("--dpll flag recieved")

            dpll_SAT = dpll.solve(self.problem)

            if dpll_SAT == False: 
                print("DPLL approach failed to find a solution.")
            else: 
                print("DPLL approach found a solution.")
        else:
            print("*", self.flag, "*")
            print("Flag not recognized. Please verify your input.")    

    print()


def main():

    flag = ""
    verbose = False

    # Process command line arguments
    if len(sys.argv) == 2:
        print("Valid input parameters recieved.")
        filename = sys.argv[1]
    elif len(sys.argv) == 3:
        print("Potential operational/debug flag detected.")
        filename = sys.argv[1]

        if sys.argv[2] == "--verbose" or sys.argv[2] == "-v":
            verbose = True
            flag = ""
        else:
            flag = sys.argv[2]
    elif len(sys.argv) == 4:
        print("Potential debug flag detected.")
        filename = sys.argv[1]
        flag = sys.argv[2]
        
        if sys.argv[3] == "--verbose" or sys.argv[3] == "-v":
            verbose = True
    else:
        print("Invalid input detected.")
        print("Please adhere to the following format: \"solver.py filename opt:verbose\" ")
        sys.exit("Terminating process.")

    problem = Problem(filename, verbose)
    s = Solver(filename, flag, problem)
    
    if verbose:
        problem.pretty_print()

    # Attempt to solve the problem
    s.solve()

    if verbose:
        print("SOLVER(): Terminating process.")


if __name__ == "__main__":
    main()

