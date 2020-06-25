# Ashley Hart
# UVA Summer Research Project
# DPLL-SAT Solver Miniproject

import sys 
import parse
import recursive
import unit_prop

# 6/4/2020 - CNF is currently the only supported input format.
# NOTE: Get it working, then optimize it.  

class Solver:

    num_variables = -1
    num_clauses = -1
    clauses = []
    flag = ""

    verbose = None

    def __init__(self, filename):
        self.filename = filename

    def printFilename(self):
        print(self.filename)

    # My intention for this function is to have it be the "Sorting Hat" of this class.
    # Will return data for analysis.
    def solve(self):

        recur_SAT: bool = False
        up_SAT: bool = False
        le_SAT: bool = False
        dpll_SAT: bool = False

        if(self.verbose):
            print("\nSOLVER: Attempting to solve " + self.filename)
            print("=======================================================================")

        if self.verbose: 
            if self.flag is "":
                print("flag: NO FLAG GIVEN")
            else:
                print("flag: " + self.flag)

        if self.flag is "":

            if self.verbose:
                print("Using all of the methods.")

            recur_SAT = recursive.solve(self.num_variables, self.num_clauses, self.clauses, self.verbose)
            up_SAT = unit_prop.solve(self.num_variables, self.num_clauses, self.clauses, self.verbose)

            if recur_SAT is False:
                print("Recursive approach failed to find a solution.")
            else:
                print("Recursive approach found a solution.")

        # Disregard the following for now.
        elif self.flag is "--recursive":

            if self.verbose:
                print("--recursive flag recieved")

            recur_SAT = recursive.solve(self.num_variables, self.num_clauses, self.clauses, self.verbose)
            
        elif self.flag is "--unit-prop":
            if self.verbose:
                print("--unit-prop flag received")

            up_SAT = unit_prop.solve(self.num_variables, self.num_clauses, self.clauses, self.verbose)

        # Disregard for now...
        elif self.flag is "--lit-elim":
            if self.verbose:
                print("--lit-elim flag receieved")
        elif self.flag is "--dpll":
            if self.verbose:
                print("--dpll flag recieved")
        else:
            print("Flag not recognized. Please verify your input.")


def main():

    flag = ""
    verbose = False

    # Argument checking
    if len(sys.argv) == 2:
        print("Valid input parameters recieved.")
        filename = sys.argv[1]

    elif len(sys.argv) == 3:
        print("Potential operational/debug flag detected.")
        filename = sys.argv[1]

        if sys.argv[2] == "verbose":
            verbose = True
            flag = ""
        else:
            flag = sys.argv[2]

    elif len(sys.argv) == 4:
        print("Potential debug flag detected.")
        filename = sys.argv[1]
        flag = sys.argv[2]
        
        if sys.argv[3] == "verbose":
            verbose = True

    else:
        print("Invalid input detected.")
        print("Please adhere to the following format: \"solver.py filename opt:verbose\" ")
        sys.exit("Terminating process.")


    # TODO: Clean up this main function with the Problem object

    p = parse.Parse(filename, flag, verbose)
    p.parse_file()


    s = Solver(filename)

    s.clauses = p.get_clauses()
    s.num_clauses = p.get_num_clauses()
    s.num_variables = p.get_num_variables()
    s.flag = p.get_flag()
    s.verbose = p.get_verbose()

    print("verbose = ", verbose)
    if verbose:
        p.pretty_print()
        print("flag = ", s.flag)



    s.solve()

    if verbose:
        print("SOLVER(): Terminating process.")


if __name__ == "__main__":
    main()

