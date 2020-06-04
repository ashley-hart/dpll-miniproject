# Ashley Hart
# UVA Summer Research Project
# DPLL-SAT Solver Miniproject

import sys 

# 6/4/2020 - CNF is currently the only supported input format.

class Solver:

    def __init__(self, filename):
        self.filename = filename


    def printFilename(self):
        print(self.filename)

    # Ensures that the file is in proper CNF format
    def checkFile(self):
        p_flag = 0

        with open(self.filename, 'r') as f:
            print(f.name)

            for lines in f:
                l = lines

                first_char = l[0]
                print("first_char = " + first_char)
                
                # Ensures the file has a 'p' line that determines the input format
                if first_char == 'p':
                    p_flag = 1

                    if "cnf" in l: 
                        print("cnf substring found in p-line")
    
        if p_flag != 1:
            print("Line header \"p\" not detected. Please revise file formmating.")
            print("Terminating process.")


def main():

    # Argument checking
    if len(sys.argv) == 2:
        print("Valid input parameters recieved.")
        filename = sys.argv[1]
    else:
        print("Invalid input detected.")
        print("Please adhere to the following format: \"solver.py filename\"")
        sys.exit("Terminating process.")

    s = Solver(filename)
    s. checkFile()

if __name__ == "__main__":
    main()
