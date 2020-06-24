## UVA SUMMER RESEARCH PROGRESS LOG
### Ashley Hart

### WEEK 1
#### June 1st, 2020
- Orientation and planning day
- Recieved open-ended project outline

#### June 2nd, 2020
- Familiarized myself with Git Markup Language
- Read 1.1 - 1.3 and 2.1 - 2.6 of Intro to Logic course
- Familiarized myself some more with Python
- Found external resources to learn about satisfiability

#### June 3rd, 2020
- Forwarded Slack link to everyone
- Met with Dr. Dwyer and UVA PhD students
- Reviewed [this talk](https://www.youtube.com/watch?v=d76e4hV1iJY&t) on YouTube
- Meeting with Mitch --> gained deeper understanding of SAT, CNF, Python and Minisat

#### June 4th, 2020
 - Began solver.py -> setting up parser for CNF file I/O
 - Reviewed notes from meeting with Mitch
 - Wrote out propositional formulae + created a log of them for future testing
 - Gained understanding of CNF file formatting
 
#### June 5th, 2020
  - Created more propositional formulae + pushed pdf to repo
  - solver.py work --> CNF file parsing
  
 ### WEEK 2
 #### June 8th, 2020
  - Looked into [this](https://sahandsaba.com/understanding-sat-by-implementing-a-simple-sat-solver-in-python.html)
  - Meeting with Dr. Dwyer
  - Further project planning
  
   #### June 9th, 2020
  - Worked on parser program, developing better ideas
  - Further project planning
  
  #### June 10th, 2020
   - No work today in support of the #ShutDownAcademia initiative and Black Lives Matter
   
  #### June 11, 2020
   - Meeting with Mitch
   - Parser code, parser code, parser code
   - Experimenting with data structures in Python for clause operations
   - Uploaded a parser prototype
   
   #### June 12th, 2020
   - Meeting with Soneya
   - Connecting solver.py to parser.py
   - Studied SAT solving techniques
   
   ### WEEK 3
   #### June 14th, 2020
   - Set up new PC to be main workstation
   - [This](https://www.cs.ubc.ca/~hutter/EARG.shtml/earg/stack/WS06-11-005.pdf) caught my eye.
   - Perhaps I can use the paper linked above in my final presentation when I cover the backtracking approach.
   - TODO: Print this paper! Even if I can not use it, its still really interesting!
   
   #### June 15th, 2020
   - Tentative goal for this week: A functional backtracking solution.
   - Meeting w/ Dr. Dwyer
   - Began planning backtracking solution
   
   #### June 16th, 2020
   - Further planning for backtracking implementation
   - Note: Having a working copy of your clauses will prevent data from being overwritten
   - For debugging - write function that prints all working clauses as they are
   - For debugging - add a function that takes a clause and quickly returns T/F if sat/unsat
   - Keep in mind: What do you want every node to represenT? What differentiates one node from the other? --> literal assignments 
   
   #### June 17th, 2020
   - Meeting with Mitch
   - ~~Code day! Yay! Work on backtracking solution.~~
   - Worked on a few handwritten solutions. 
   - I have a better idea of how my code needs to work. 
   - Began a cleaner attempt at my prototype.

   #### June 18th, 2020
   - Code? Code. 
   - Note: the function that checks the clause set under a set of assignmens is critical. Take the time to figure it out.
   - Note: Base case will check clause set under assignments, then add the assignment set to the "valid" set if the expression is SAT. 
   - For debugging - What do you do if your problem line has the wrong amount of variables and/or clauses? Need to add my own   safeguards.
   - Meeting with Soneya
   
   #### June 19th, 2020 
   - Consider a different approach for SAT checking.
   - Trying to figure out why my values won't update.
   - Pushed up current code for anyone who wants to see if they can find the error.
   - Redesigning code to find one solution. --> reviewed Dr. Dwyer's suggestion 
   - Still trying to figure out how I can check that a set of clauses is satisfied with code.
   - Looking through [this](https://sahandsaba.com/understanding-sat-by-implementing-a-simple-sat-solver-in-python.html) again  
   
   ### WEEK 4
   #### June 22nd, 2020
   - Got stuck, rewriting recursive solution...
   - Meeting with Matt
   - Worked things through with Matt and on paper
   - Began working on a new recursive solution
   
   #### June 23rd, 2020
   - Follow up meeting with Matt, very helpful
   - Developed new solution
   - Added verbose tag for debugging, still a WIP
   - Updated documentation,
   - Worked on recursive solution some more
   
   #### June 24th, 2020
   - Meeting with Mitch
   - Cleaning and debugginf recursive solution.
   - Started implementing problem object
   - Compiled more test cases
   - Leadership Alliance Workshop today
   
   #### June 25th, 2020
   - TODO: Begin unit propogation
   - Meeting with Soneya
 
