#!/bin/bash

# You will need to change the righthand side
# of this assignment to point to minisat's
# executable (or whichever SAT solver you want)
SAT_SOLVER=code/solver.py

# Create an empty file
>easy_benchmarks.txt

# Loop through all the files in the current directory
# with a .cnf extension; give the current file the name "f"
for f in benchmarks/sr2019/*/*.cnf; do
    # Stop the solver if it's still running
    # after 10 seconds
    echo $f
    timeout 10 python3 $SAT_SOLVER $f -l
    
    # The exit status is stored in a variable
    # named "?"...I don't know why
    exit_status=$?
    
    # An exit status of "0" means success
    if [[ $exit_status -eq 0 ]]; then
	# Append the name of the successful file
	# to the end of the "easy list"
	echo $f >> easy_benchmarks_le.txt
    fi
done 

for f in benchmarks/my-cnf/*.cnf; do
    # Stop the solver if it's still running
    # after 10 seconds
    echo $f
    timeout 10 python3 $SAT_SOLVER $f -l
    
    # The exit status is stored in a variable
    # named "?"...I don't know why
    exit_status=$?
    
    # An exit status of "0" means success
    if [[ $exit_status -eq 0 ]]; then
	# Append the name of the successful file
	# to the end of the "easy list"
	echo $f >> easy_benchmarks_le.txt
    fi
done

