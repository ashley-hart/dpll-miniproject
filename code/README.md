## Running The Code 

### parser.py 
  At this time, this is the "start" of the overall program. It takes up to two command line arguments, a required filename and an
  optional method flag which will eventually restrict the solver to the corresponding SAT solving method.
  
  Here is a sample of how this code should be executed:
  
  `user@System python3 parser.py dimacs_file.cnf --flag_name`
  
  The flags that will eventually be supported are as follows:
  
      * --recursive
      * --unit_prop 
      * --lit_elim  
      * --dpll  
    
   Please use these flags in place of `--flag_name` in the sample above.
   Also, bear in mind that `dimacs_file.cnf` can be any file. However, it will be rejected if it does not adhere to the DIMACS-CNF format.
    
    
  ### solver.py
   *[Note] At this time solver.py is not intended to be called directly. I have included it in this directory so you can get an idea of 
   where I am headed. This message will disappear when more progress is made.*
   
   When given a flag, solver.py will only pass the data recived from parser.py to the code that handles that specific solution. If a flag is not specifed, the solver will 
   run the data against all four solution methods. The results will then be sent back to solver.py for analysis.
    
  --------------------------------------------------------------------------------------------------------------------------
    
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
