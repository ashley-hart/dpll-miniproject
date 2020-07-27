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
   - Cleaning and debugging recursive solution.
   - Started implementing problem object
   - Compiled more test cases
   - Leadership Alliance Workshop today
   
   #### June 25th, 2020
   - Began unit propagation with reading and paper work
   - Meeting with Soneya
   
   #### June 26th, 2020
   - Unit propagation code planning
   - Trying to figure out how I need to change my recursive function to support modified clauses...
   - Began implementation framework --> base on recursive.py
   
   ### WEEK 5
   #### June 29th, 2020
   - Pure literal elmination, paperwork and reading
   - Meeting with Matt
   - Outline code and figure out where new logic needs to go -> base on recursive.py
   
   #### June 30th, 2020
   - Coded up a protoype for pure literal elimination, added to repo
   - Updated verbose flag: "verbose" --> "--verbose"
   - Midpoint check-in with Dr. Crenshaw
   - Working to integrate pure literal elimination logic with recursive SAT solver.
   - Leadership Alliance Workshop today
   
   #### July 1st, 2020
   - Meeting with Matt and PhD students
   - Meeting with Mitch - ask about Python visuals for SAT solver & data collection
   - Review deadlines for conference materials
   - Integrated recursive, unit-propagation and lit-elim logic for DPLL  
 
   #### July 2nd, 2020
   - Futher code testing
   - Reviewed script Mitch sent over
   - Meeting with Soneya - watchlist tutorial
   
   #### July 3rd, 2020
   - GOAL: Made significant progress on/completed DPLL prototype -- Done!
   - Holiday
   
   ### WEEK 6
   #### July 6th, 2020
   - Developing dpll_watchlist.py --> ran into a bug with quinn.cnf (infinite loop in update_watchlist)
   - Read into data collection with Python and Bash scripting
   - Start drafting titles and abstracts for conference.
   - Meeting with Matt
   
   #### July 7th, 2020
   - Reworked the watchlist logic, added unit prop. and lit elim.
   - Sent Matt a list of titles.
   - Followed up with Dr. Crenshaw.
   - Code & verbose output clean up
   - Set up benchmarks
   
   
   #### July 8th, 2020
   - DEADLINE FOR TITLE SUBMISSION.
   - Ph.D. Student Meeting @ 9AM
   - Meeting with Mitch @ 12PM
   - Set up UVA portal for heavier code testing.
   - TEST! TEST! TEST!
   
   #### July 9th, 2020
   - Meeting with Soneya @ 4PM
   - Squashed bugs & code cleanup.
   - Worked on abstract.
   - Found more CNF files.
   - Sent abstracts out for feedback.
   - Registered for virtual LANS
   
   #### July 10th, 2020
   - Meeting with Matt @ 11AM --> demonstrated code
   - Set up a sheet to log times for each implemntation.
   - Runtime enchancements made to dpll_watchlist.py
   - Revised abstract
   
  ### WEEK 7
  #### July 13th, 2020
  - ABSTRACT DUE TODAY --> SUBMITTED
  - Meeting with Matt @ 3PM --> got ideas for slides 
  - Made unit propagation and literal elimination exhaustive
  - Refactored code --> created master solver with control system
  
  #### July 14th, 2020
  - Finish refactoring, do more data collection.
  - Looked into what's slowing down the literal elimination implementation
  - Added unit prop. and lit elim. to watchlist solver --> improve this
  - Collected data and made a spreadsheet, developed visuals.
  - Optimizations are actually slower than basic recursive version. MUST FIX!
  
  #### July 15th, 2020
  - Ph.D. Student Meeting @ 9AM
  - Meeting with Mitch @ 12PM
  - Start thinking about your slide deck
  - I believe I stopped the issue where the recursive solver would terminate prematurely.
  - Spent most of today trying to figure out why PLE is so SLOW. No breakthroughs yet.
  - Removed old method of keeping up with truth values. New way is cleaner and faster.
  - Did some clean up.
  - Leadership Alliance workshop @ 3PM
  
  #### July 16th, 2020
  - Spent most of today trying to speed up unit propagation, still needs work.
  - Data is showing the desired trends on some large testcases, but not so much elsewhere. 
  - Began drafting presentation.
  - UVA Virtual Recruitment Fair @ 3P
  
  #### July 17th, 2020
  - Meeting with Soneya @ 10AM
  - Meeting with Matt @ 11AM
  - Went over the presentation script
  - Data collection & graph analysis --> data looks better, still some irregularities.
  - Got useful visuals from Matt for the presentation
  - (TODO) Improve argument processing w/ Python's argsparse library
  
  ### WEEK 8
  #### July 20, 2020
  - Meeting with Matt @ 3PM
  - Produced first version of presentation slides
  - Trying to optimize code for PLE procedure --> too many list comprehensions
  - Changed SAT_check() to make clause_check() obsolete
  - Considering a full rewrite of the solver. 
  
  #### July 21, 2020
  - Added script to notes on PowerPoint slides.
  - Prepared slides and data for Wednesday's presentation
  - Practiced the talk.
  
  #### July 22nd, 2020
  - Gave practice talk at Wednesday morning meeting. 
  - Meeting with Mitch
  - Mitch and I are unsure of further reductions, putting data struture optimizations on hold.
  - Fixed issue with clause reductions.
  - Made some pigeonhole principle benchmarks with cnfgen tool.
  
  #### July 23rd, 2020
  - Produced a new data set
  - Meeting with Soneya @4PM
  - Leadershp Alliance Virtual Recuitment Fairs
  - PLE is still bottlenecking...
  
  #### July 24th, 2020
  - Trying to get an idea of public README.md
  - Attended Harvard's Recruitment Fair
  - Looked into generator expressions --> they *might* improve the runtime...
  - Practiced the talk --> going with the data we have for now, trying to learn more about PLE and Python to improve my code.
  
  ### WEEK 9
  #### July 27th, 2020
  - Reworked logic based on Mitch's DPLL implementation and algorithim pseudocode
  - Repository made public 
  - Began process of updating README files
  - Meeting with Matt @3PM --> very cool lecture on 
  - Submitted slides as a PDF to Ramy
  
 #### July 28th, 2020
   - (TODO) Compile data on a mix of SAT/UNSAT Benchmarks
   - (TODO) Examine times on Mitch's DPLL implementation
   - Dry run of breakout room @ 4PM w/ Ramy
