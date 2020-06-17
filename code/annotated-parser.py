# Ashley Hart
# Summer 2020

import sys
import collections

class Parser:

    format_type: str = ""
    num_variables: int = -1
    num_clauses: int = -1
    # Mitch note: the clauses data structure
    # has been changed to an array of arrays,
    # so you'll have to add types to the following
    clauses = {} 
    flag: str = ""
    
    def __init__(self, filename, flag) -> None:
        self.filename: str = filename

    def get_clauses(self): # clauses is not currently typed
        return self.clauses
    
    def get_num_variables(self) -> int:
        return self.num_variables
    
    def get_num_clauses(self) -> int:
        return self.num_clauses

    def get_flag(self) -> str:
        return self.flag

    def parse_file(self) -> None:
        
        p_flag: bool = False
        clause_number: int = 0

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
                    p_flag = True
                    self.format_type = tokens[1]
                    self.num_clauses = tokens[2]
                    self.num_variables = tokens[3]
                # Parse clauses iff problem line has been found
                elif int(first_token) and p_flag == True:
                    
                    # Valid clause termination check
                    if int(tokens[len(tokens) - 1]) != 0:
                        print("ERROR: Invalid clause termination, file is invalid!")
                        print("Invalid line: " + line, end="")
                        exit("Please ensure that all clauses are terminated with a 0.")

                    self.clauses[clause_number] = tokens
                    clause_number += 1
                # TODO: Figure out how to trigger this code
                else:
                    print("ERROR: Formatting error!")

            if p_flag == False:
                print("ERROR: Problem line \"p\" missing or out of place. Check file formmatting.")

            

    def pretty_print(self):
        print("p " + self.format_type + " " + self.num_variables + " " + self.num_clauses)

        for value in self.clauses.values():
            for num in value:
                if int(num) != 0:
                    print(num + " ", end="")
                else:
                    print(num, end="")
            print()


def main():

    flag: str = ""

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
        print("Please adhere to the following format: \"solver.py filename --optional_flag\"")
        sys.exit("Terminating process.")

    p = Parser(filename, flag)
    p.parse_file()
    p.pretty_print()



if __name__ == "__main__":
    main()
