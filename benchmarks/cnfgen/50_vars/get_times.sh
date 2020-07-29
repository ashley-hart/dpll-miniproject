#!/bin/bash

# You will need to change the righthand side
# of this assignment to point to minisat's
# executable (or whichever SAT solver you want)
# SAT_SOLVER=code/solver.py

# Loop through all the files in the current directory
# with a .cnf extension; give the current file the name "f"
for f in *.cnf; do
	echo $f
done
