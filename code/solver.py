# Ashley Hart
# UVA Summer Research Project
# DPLL-SAT Solver Miniproject

import sys 
import parse
import backtrack

# 6/4/2020 - CNF is currently the only supported input format.
# NOTE: Get it working, then optimize it.  

class Solver:

    num_variables = -1
    num_clauses = -1
    clauses = []
    flag = ""

    def __init__(self, filename):
        self.filename = filename

    def printFilename(self):
        print(self.filename)

    # My intention for this function is to have it be the "Sorting Hat" of this class.
    # Will return data for analysis.
    def solve(self):
        print("Attempting to solve " + self.filename)


        if self.flag is "":
            print("flag: NO FLAG GIVEN")
        else:
            print("flag: " + self.flag)

        if self.flag is "":
            print("Using all of the methods.")
            backtrack.solve(self.num_variables, self.num_clauses, self.clauses)

        # Disregard the following for now.
        elif self.flag is "--recursive":
           print("--recursive flag recieved")
        elif self.flag is "--unit-prop":
            print("--unit-prop flag received")
        elif self.flag is "--lit-elim":
            print("--lit-elim flag receieved")
        elif self.flag is "--dpll":
            print("--dpll flag recieved")
        else:
            print("Flag not recognized. Please verify your input.")

def main():

    flag = ""

    # Argument checking
    if len(sys.argv) == 2:
        print("Valid input parameters recieved.")
        filename = sys.argv[1]
    elif len(sys.argv) == 3:
        print("Potential operational flag detected.")
        filename = sys.argv[1]
        flag = sys.argv[2]
    else:
        print("Invalid input detected.")
        print("Please adhere to the following format: \"solver.py filename\"")
        sys.exit("Terminating process.")

    p = parse.Parse(filename, flag)
    p.parse_file()
    p.pretty_print()

    s = Solver(filename)

    s.clauses = p.get_clauses()
    s.num_clauses = p.get_num_clauses()
    s.num_variables = p.get_num_variables()
    s.flag = p.get_flag()

    s.solve()


if __name__ == "__main__":
    main()

