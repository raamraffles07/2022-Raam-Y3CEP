# Development Log
> A successful final project is built slowly over many weeks not thrown together at the last minute. To incentivize good project pacing and to let your project mentor stay informed about the status of your work, each week you should add an entry to your log.md file in the development directory.

> Each entry should describe:

> - What goals you had set for the week and whether they were accomplished or not
> - What problems you encountered (if any) that prevented you from meeting your goals
> - What you plan to accomplish or attempt next week

> The development log will be graded for completion, detail, and honesty – not progress. It is much better to truthfully evaluate the work you completed in a week then lie to make the project sound further along then it really is. It is totally acceptable to have an entry that says you tried nothing and accomplished nothing. However if every week starts to say that, both yourself and your project mentor will be able to identify the issue before it becomes impossible to fix.

[Example of Good/Bad Changelist descriptions](https://google.github.io/eng-practices/review/developer/cl-descriptions.html)

## Week 5 (26 Jul - 1 Aug)

Finish Writing Proposal and Planning + Prior research for Project. Also update Development Log. 

--> This goal was completed succesfully, with the Proposal being completed and Submitted on the 1st of August. The development log was also updated successfully. 

## Week 6 (2 Aug - 8 Aug)

Start Implementing Student Record Tracking System

--> This goal was completed successfully. The Class "Student", as well as the user interface with the program, was coded successfully. Additionally, I was also able to do additional work this week, and start coding for sub-functions such as "Add Student". 

--> However, one challenge I am facing is that I am having trouble with importing functions from other files into the main user interface. Whenever the user selects a function they want, such as "Add Student", the program does not import this function from another file, but instead exits the program. This is something I spent very long (about 3 hours) trying to fix, but am still unable to do so. 

## Week 7 (9 Aug - 15 Aug)

Finish Implementing Student Record Tracking System

--> This week was super busy with WAs, Science RE submission, etc., so I was not able to work on the project as much. 
--> It greatly helped that I could do extra work last week.
--> The bug is unfortunately still unfixed. 

## Week 8 (16 Aug - 22 Aug)

--> After trying for about an hour, I was able to to fix the bug in importing functions from other files into the main user interface. 

--> I spent about 4 hours trying to code for several sub-functions including "Add Student", "Update Student Offence List", "Update Student Badge List". These functions are able to accurately read and present specific data in specific rows and columns in my csv file. However, I am facing a lot of difficulty in updating column values into a .csv file.  

--> I really tried to code for certain sub-functions like "Remove Student". However, even after about 3 hours of trying, I found great difficulty in finding ways, from both the Coursemology document, and online resources, to implement certain actions like removing entire rows from .csv files, and plan to work on them the following week. 

## Week 9 (23 Aug - 29 Aug)

--> This week was the wonder week, having spent about 16 hours on the project. I managed to finish almost all the sub-functions of my program and fixed all the bugs identified in my codes from last week. I am almost entirely done with the project. 

--> In essence, I am done with almost every aspect of my project. However, some of the outputs/print statments in specific sub-functions, such as the "Access Student Info" and "Access Logistics Info" look quite ugly, which I need to fix soon. Additionally, I have not fulfilled certain criteria of the OOP such as implementing "try and except" in my codes. I also aim to include additional sub-functions in the upcoming weeks. Overall, in the upcoming weeks, I would like to try to perfect the entire project, and also better orientate it with the goals/objectives set for this project.


## Week 10 (30 Aug - 5 Sep)

--> I started implementing the "Update Events Information" sub-function of my program, although it is not fully complete (almost completed). I also finished coding for the "Access Events information".

--> I spent most of the week touching up on my program and making the user-end experience of it smoother. I also identified a couple of loopholes, and managed to fix them.

--> One problem that popped up this week was, when I tried to run my maincode(), all the data in 'Dataset.csv' and 'Logistics.csv' were mysteriously erased. Interestingly, the data in 'Events.csv' was unaffected by this. I did not face this problem last week, and my code was running perfectly fine last week, so I was not sure as to why this occured. At first, I thought that the problem was in the lines of my sub-function that retrieved the datasets. However, upon further analysis and code alteration, I found out that the data in both my datasets were being erased right after maincode() was run, and even before the sub-functions of my code were called. I tried to fix this, but I was unable to do so. This is something I would like to work on next week.

## Sep Holiday (5 Sep - 10 Sep) **Submission date is 10 Sep**

--> I finished implementing the "Update Events Information", "Access Events information". Since I had additional time, I also implemented the "Update Attendance List" and "Access Absentee List of my codes". Most of this week was also spent on making my codes look nicer and neater.

--> I was unable to fix the error from Week 10, where the data in 'Dataset.csv' and 'Logistics.csv' were mysteriously erased everytime I ran maincode(). However, this is a very very minor issue, as all the data from both the datasets could be easily retrieved and saved again by reversing the change 
(Command + Z), before proceeding to provide inputs in the sub-functions. This isn't a big issue as this takes less than a seconds to do, and thus there is negligible chance of data in the datasets being lost. This is something I would like to improve on and fix after the final submission of my project.

--> I also implemented the Try-Except commands in my code, as i had not included them inside before. My entire program, where seniors in the CCA can easily access Student Information (Their Offences, Badges, Attendance and Broken Items), Logistics Information and Events Information, is now entirely complete.
