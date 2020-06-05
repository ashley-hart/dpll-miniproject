# dpll_miniproject
A miniproject building a SAT solver and exploring its extension and performance.

The following schedule is just a rough sketch.  Work will spill across the boundaries of the weeks to fill up the entire project duration based on our interests, what parts are more or less challenging, and other factors.  

### Getting started
   - ~~account setup~~  
   - ~~github account~~  
   - ~~set up a private repository for your summer project~~   
   - ~~invite Matt, Mitch, and Sonya to be contributors~~   
   - ~~create a README.md to document your progress~~ 
   - ~~slack~~
 - ~~ssh keys~~   
   - ~~explore how this works on Windows 10~~
   - ~~getting comfortable with `portal.cs.virginia.edu` and CentOS modules~~
     - `module avail` : to find out what modules are available
     - `module show` : to find out what is in a module
     - `module load` : to load a module so that you can use it
     - modify your `.bashrc` to add `module load ...`' commands

### Propositional logic and satisfiability
   - A nice interactive [Introduction to Logic](http://intrologic.stanford.edu/public/index.php); we will reference concepts from the following book chapters 
     - [introduction*](http://intrologic.stanford.edu/chapters/chapter_01.html) 
     - [propositional logic*](http://intrologic.stanford.edu/chapters/chapter_02.html) 
     - [propositional analysis*](http://intrologic.stanford.edu/chapters/chapter_03.html) 
     - [satisfiability and DPLL*](http://intrologic.stanford.edu/extras/satisfiability.html) 
   - The [Boolean satisfiability problem*](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem) wiki page has lots of useful information
   - You don't need to read all of this immediately and plan to reread parts as needed; that's normal 
   -  **NOTE: All reading materials marked with an '*' have been looked at at least once**

### Programs to check for satisfiability
   - ~~An incomplete list of [SAT solvers](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem#Offline_SAT_solvers)~~
   - You will be exploring satisfiability experimentally by running solvers; it will be best to use `portal.cs.virginia.edu` since it is fast and has lots of memory 
     - ~~download, install and run [MiniSat](http://minisat.se/). assuming you are logged into your node in uva's portal, executing the following commands will build a minisat executable within `minisat/simp` (this builds a version of minisat extended with a simplification library):~~
     ```
     wget http://minisat.se/downloads/minisat-2.2.0.tar.gz
     tar zxvf minisat-2.2.0.tar.gz
     cd minisat/
     MROOT=`pwd` make -C simp
     ```
     (now to actually execute `minisat`, you will need to either be within `minisat/simp` to call it, or you need to give its absolute path, e.g., `/u/mjg6v/minisat/simp/minisat`; run `minisat --help` to see a list of this program's options)
     - download, install and run [CryptoMiniSat](https://msoos.github.io/cryptominisat_web/). assuming you are logged into your node in uva's portal, executing the following commands will build a cryptominisat executable within `cryptominisat-5.7.1/build`:
     ```
     module load gcc-7.1.0
     wget https://github.com/msoos/cryptominisat/archive/5.7.1.tar.gz
     tar xvf 5.7.1.tar.gz
     cd cryptominisat-5.7.1/
     mkdir build && cd build
     cmake ..
     make
     ```
     (now to actually execute `cryptominisat5_simple`, you will need to either be within `cryptominisat-5.7.1/build` to call it, or you need to give its absolute path, e.g., `/u/mjg6v/cryptominisat-5.7.1/build/cryptominisat5_simple`; run `cryptominisat5_simple -h` to see a list of this program's options)

### Writing your own formulae 
- ~~write some propositional formulae~~
  - create formula that are satisfiable, unsatisfiable, valid, and invalid
  - think about what you expect the answer to be --> truth tables & unit propagation
- ~~translate your formulae to [CNF](https://en.wikipedia.org/wiki/Conjunctive_normal_form)~~
  - this will be easy for simple formula, but it can get tedious for large formula
- ~~translate your CNF formulae to [DIMACS-CNF](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem#SAT_problem_format) format~~
  - this will not be very readable
- ~~install the [BC](http://users.ics.aalto.fi/tjunttil/bcsat/) translator~~
  - how do your translations compare to the one's produced by BC?
- run the DIMAC-CNF formula through a SAT solver
  - what's the result?
  - does this match what you expected?

### Some formulae are harder to check than others
- ~~download [CNF benchmarks](http://sat-race-2019.ciirc.cvut.cz/index.php?cat=downloads)~~  
- write a python program that: 
  - runs each benchmark on a set of solvers
  - reports their results and their execution time
  - think of ways of sorting the benchmarks into easy and hard sets based on some criteria
- use your program to select a benchmark of 100 "easy" problems

### SAT solving by hand
- recursive definition --> with backtracking?
- representing assignments
- checking consistency of a set of literals
- checking emptyness of a set of literals

### Parsing
- what is parsing? -> reading and using data from files in code
- parsing CNF files --> touched on this with Mitch
- (WIP) write a Python program named solver.py to accept or reject a CNF file 

### Writing your first SAT solver
- extend the above program to implement a recursive SAT solver with a command line option "--recursive"
- record and print statistics, e.g., # of two-way branches
- compare the time performance of "solver.py --recursive" to other solvers on your "easy" benchmark

### Unit propogation
- a motivating example of unit propogation
- extend solver.py to include unit propogation with the command line option "--unit-prop"
- compare stats against previous implementation

### Pure literal elimination
- Note to self: READ UP ON THIS!
- a motivating example of pure literal elimination
- extend solver.py to include pure literal elimination with the command line option "--lit-elim"
- compare stats against previous implementation

### DPLL
- why this name? --> named after four contributors
- the two above observations allow the recursive implementation to be *much* faster
- extend solver.py to enable *both* unit propogation and pure literal elimination with the command line option "--dpll"
- make the "--dpll" option the default if no other options are given
- compare stats against last week's recursive implementation
- compare the time performance of "solver.py --dpll" against other solvers on your "easy" benchmark

### Literal selection heuristics
- a motivating example of how literal selection can make a difference
- extend solver.py to include some different heuristics with appropriately named command line options
- compare stats against previous implementation

### Conflict clause learning
- a motivating example of conflict clause learning
- extend solver.py to include pure conflict-directed clause learning (CDCL) with the command line option "--cdcl"
- compare stats against previous implementation

### What makes it take so long
- we know that solver time varies and not just based on the size of a formula
- experiment, across a range of benchmarks, to produce similarly sized pairs of formula that have very different performance
- profile solver.py to understand where it spends its time on such pairs of formula, e.g., using [Scalene](https://github.com/emeryberger/scalene)
