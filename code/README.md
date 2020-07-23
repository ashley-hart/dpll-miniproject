## Running The Code 

### solver.py 
  At this time, this is the "start" of the overall program. It takes up to two command line arguments, a required filename and an
  optional method flag which will restrict the solver to the corresponding SAT solving method. If no flag is given, four SAT solving techniques will be attempted:
  simple recursion, unit propogation, literal elimination and DPLL.
  
  Here is a sample of how this code should be executed:
  
  `user@System python3 parser.py dimacs_file.cnf --flag_name --verbose`
  
  The supported flags are as follows:
  
      * --recursive
      * --unit_prop 
      * --lit_elim  
      * --dpll 
      * --dpll-w
      * --all
    
   Please use these flags in place of `--flag_name` in the sample above.
   Also, bear in mind that `dimacs_file.cnf` can be any cnf or txt file. However, it will be rejected if it does not adhere to the DIMACS-CNF format.
   
   The debug flag are `--verbose` or `-v`. 
   Please note that the following form of input is also valid.
   
   `user@System python3 parser.py dimacs_file.cnf --verbose`
    
   IMPORTANT: As of June 26th, additional flags were added to improve user-friendliness:
   
      * -r --> shorthand for --recursive
      * -u --> shorthand for --unit-prop 
      * -l --> shorthand for --lit_elim
      * -d --> shorthand for --dpll
      * -dw --> shorthand for --dpll-w
      * -a --> shorthand for --all
      * -v --> shorthand for --verbose
   
### sat_solver.py 
  Searches for and returns whether or not a satisfiying assignment was found for the given problem. This solver is built on top of a recursive backtracking algorithim that can     be optimized. By default, the solver will use every optimization it has availible to solve the problem. Flags for unit propagation and pure literal elimination will enable      those specific optimizations and run them alongside the recursive solver. 

### problem.py
   Contains all data pertaining to the problem and handles file parsing upon initialization. More information to come.
   This class replaces parser.py.

### dpll_watchlist.py
   This is the dpll algorithim optimized with a watchlist implementation.
    
---
    
   Feedback is greatly appreciated as I am looking to learn and improve as much as I can.
   As always, feel free to reach out with any questions as well.
   
---
 
#### Adding type annotations
 
Python does not enforce a strict type system like Java does. This allows you to do some tricky things
at runtime, but it also allows you to shoot yourself in the foot and create a lot of confusion. It's
possible to annotate your Python programs with types, and then check your program using a separate tool 
called `mypy` before executing your code. This will tell you if the type checker spotted any errors,
which you can choose to ignore if you want, because when you actually run, e.g., `python3 parser.py foo.cnf`, 
the annotations are just thrown away. (But still, don't ignore the type errors :))

To install `mypy`, from within an Ubuntu terminal run `sudo apt install python3-pip` and then
`pip3 install mypy`. Now to type check my example (partially) annotated program in this directory,
run `mypy annotated-parser.py`. You should see three errors, with messages about which line the
error is on in the file and why this is considered a type error.

---

#### Visualizing graphs via DOT files

[DOT](https://en.wikipedia.org/wiki/DOT_(graph_description_language)) is a graph description language.
We will try to visualize the progress of the SAT solver by emitting a succession of different DOT files;
these will describe different trees. To be able to visualize a DOT file, you will need to download 
the `graphviz` library in an Ubuntu terminal by running the command `sudo apt install graphviz`.

A simple, undirected graph can written in the DOT language like this:

```
graph {
    a -- b -- c;
    b -- d;
}
```

You can save this text in a file named `test.dot`.
To make a PNG so you can visualize this graph, within an Ubuntu terminal run: `dot -Tpng test.dot -o test.png`.
Now you can open the PNG file either on your Windows desktop, or via the command `eog test.png` in Ubunutu
(I'm not sure if Linux-in-Windows will correctly visualize this if you run it straight from the terminal).

