# Ashley Hart
# UVA Summer Research Project
# DPLL-SAT Solver Miniproject

import sys 

# 6/4/2020 - CNF is currently the only supported input format.
# NOTE: Get it working, then optimize it.  

class Solver:

    def __init__(self, filename):
        self.filename = filename


    def printFilename(self):
        print(self.filename)

    # My intention for this function is to have it be the "Sorting Hat" of this class.
    # It will evaluate the file and see which method will be best. 
    # NOTE: This funtion will need to support flags from the command line. These flags will 
    # determine what the solver does. Default flag will be ""
    #
    # --recursive -> attempt with backtracking
    # --unit-prop -> attempt with unit propogation
    # --lit-elim -> attempt with literal elimination
    # --dpll -> attempt with dpll
    def solve(self, flag):
        print("Attempting to solve " + self.filename)
        print(flag)

        if flag == "--recursive":
           print("--recursive flag recieved")

        if flag == "--unit-prop":
            print("--unit-prop flag received")

        if flag == "--lit-elim":
            print("--lit-elim flag receieved")

        if flag == "--dpll":
            print("--dpll flag recieved")

# (6/11) This main will be used for testing purposes for now.
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
        print(flag)
    else:
        print("Invalid input detected.")
        print("Please adhere to the following format: \"solver.py filename\"")
        sys.exit("Terminating process.")

    s = Solver(filename)
    # s. checkFile()

    s.solve(flag)

if __name__ == "__main__":
    main()
