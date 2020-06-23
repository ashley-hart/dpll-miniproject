# Ashley Hart
# Summer 2020

import sys
import os 

# TODO: Add a methon that returns true or false for the Bash Script

# Make a note of this on paper so you dont forget how objects work in Python
# clauses = parse.for_the_memes()
# def for_the_memes():
#     print(":D")

class Parse:
    format_type = ""
    num_variables = -1
    num_clauses = -1
    clauses = []
    flag = ""

    verbose = None
    
    def __init__(self, filename, flag, verbose):
        self.filename = filename
        self.verbose = verbose

    def get_clauses(self):
        return self.clauses
    
    def get_num_variables(self):
        return int(self.num_variables)
    
    def get_num_clauses(self):
        return int(self.num_clauses)

    def get_flag(self):
        return self.flag

    def get_verbose(self):
        return self.verbose

    def parse_file(self):

        if self.verbose:
            print("\nPARSE_FILE(): Attempting to parse: ", self.filename)
            print("=======================================================================")
            print("cat " + self.filename +"\n")
            os.system("cat " + self.filename)
            print()


        p_flag = 0
        clause_number = 0

        with open(self.filename, 'r') as f:

            for line in f:
                # Skip comment lines
                if line[0] == 'c':
                    continue

                tokens = line.split()
                
                # Empty line check, might be unneccesary
                if len(tokens) != 0:
                    first_token = tokens[0]
                else:
                    continue

                # Parse problem line
                if first_token == 'p':
                    p_flag = 1
                    self.format_type = tokens[1]
                    self.num_clauses = tokens[2]
                    self.num_variables = tokens[3]
                # Parse clauses iff problem line has been found
                elif int(first_token) and p_flag == 1:
                    
                    # Valid clause termination check
                    if int(tokens[len(tokens) - 1]) != 0:
                        print("ERROR: Invalid clause termination, file is invalid!")
                        print("Invalid line: " + line, end="")
                        exit("Please ensure that all clauses are terminated with a 0.")

                    # After we know the 0 is there, take it off
                    tokens.pop()

                    for i in range(0, len(tokens)):
                        tokens[i] = int(tokens[i])

                    self.clauses.append(tokens)
                    clause_number += 1
                # TODO: Figure out how to trigger this code
                else:
                    print("ERROR: Formatting error!")

            if p_flag == 0:
                print("ERROR: Problem line \"p\" missing or out of place. Check file formatting.")

            if self.verbose:
                print("PARSE_FILE(): Finished parsing: ", self.filename)
                print("=======================================================================")

            
      

    def pretty_print(self):
        print("p " + self.format_type + " " + self.num_variables + " " + self.num_clauses)
        for value in self.clauses:
            for num in value:
                if int(num) != 0:
                    print(num, " ", end="")
                else:
                    print(num, end="")
            print()
