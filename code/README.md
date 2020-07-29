## Running The Code 

### solver.py 
At this time, this is the "start" of the overall program. It takes up to two command line arguments, a required filename and an
optional method flag which will restrict the solver to the corresponding SAT solving method. If no flag is given, four SAT solving techniques will be attempted:

Here is a sample of how this code should be executed:
  
  `user@System python3 solver.py dimacs_file.cnf --flag_name --verbose`
  
The supported fucntional flags are as follows:
  
      * --recursive - a brute force SAT solving approach
      * --unit_prop - recursive solver with unit propagation
      * --lit_elim - recursive solver with unit propagation
      * --dpll - uses all of the above methods
      * --dpll-w - activates the watchlist implementation
    
Please use these flags in place of `--flag_name` in the sample above.
Also, bear in mind that `dimacs_file.cnf` can be any cnf or txt file. However, it will be rejected if it does not adhere to the DIMACS-CNF format.
   
The debug flag is `--verbose`. All output can be muted with the `--silence` flag.
Please note that the following form of input is also valid.
   
   `user@System python3 parser.py dimacs_file.cnf --verbose`
    
This solver also implements several additional flags for user friendliness:
   
      * -r --> shorthand for --recursive
      * -u --> shorthand for --unit-prop 
      * -l --> shorthand for --lit_elim
      * -d --> shorthand for --dpll
      * -dw --> shorthand for --dpll-w
      * -a --> shorthand for --all
      * -v --> shorthand for --verbose
      * -s --> shorthand for --silent
   
### sat_solver.py 
Searches for and returns whether or not a satisfiying assignment was found for the given problem. This solver is built on top of a recursive      backtracking algorithim that can be optimized. By default, the solver will use every optimization it has availible to solve the problem. Flags for unit propagation and pure literal elimination will enable those specific optimizations and run them alongside the recursive solver. 

### problem.py
Contains all data pertaining to the problem and handles file parsing upon initialization. Any information pertaining to the SAT problem can be gathered from this class. 

### dpll_watchlist.py
This is the dpll algorithim optimized with a watchlist implementation.
    
