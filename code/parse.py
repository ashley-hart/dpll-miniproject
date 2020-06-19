# Ashley Hart
# Summer 2020

import sys
import collections # remove 

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
    
    def __init__(self, filename, flag):
        self.filename = filename

    def get_clauses(self):
        return self.clauses
    
    def get_num_variables(self):
        return int(self.num_variables)
    
    def get_num_clauses(self):
        return int(self.num_clauses)

    def get_flag(self):
        return self.flag

    def parse_file(self):
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

                    for i in range(0, len(tokens)):
                        tokens[i] = int(tokens[i])

                    self.clauses.append(tokens)
                    clause_number += 1
                # TODO: Figure out how to trigger this code
                else:
                    print("ERROR: Formatting error!")

            if p_flag == 0:
                print("ERROR: Problem line \"p\" missing or out of place. Check file formmatting.")
      

    def pretty_print(self):
        print("p " + self.format_type + " " + self.num_variables + " " + self.num_clauses)
        for value in self.clauses:
            for num in value:
                if int(num) != 0:
                    print(num, " ", end="")
                else:
                    print(num, end="")
            print()


# def main():
# 
# flag = ""

# # Argument checking
# if len(sys.argv) == 2:
#     print("Valid input parameters recieved.")
#     filename = sys.argv[1]
# elif len(sys.argv) == 3:
#     print("Potential operational flag detected.")
#     filename = sys.argv[1]
#     flag = sys.argv[2]
# else:
#     print("Invalid input detected.")
#     print("Please adhere to the following format: \"solver.py filename --optional_flag\"")
#     sys.exit("Terminating process.")

# p = Parser(filename, flag)
# p.parse_file()
# p.pretty_print()



# if __name__ == "__main__":
#     main()