# Sprint x Report (10/10/22 - 11/9/2022)

## What's New (User Facing)
 * LFP Data can be accessed using Python
 * LFP Data can be processed into Power values
 * LFP Data can be processed into Coherence values
 * Began using Lasso on a small dataset to make predictions on control vs experiment groups

## Work Summary (Developer Facing)
We started this sprint by converting the provided MatLab code to Python to get a better understanding behind the algorithms developed by our client and the previous capstone team.
Once we decided we had enough understanding of these algorithms, we switched to making our own code in Python.
This switch was also made because the MatLab code does not translate well to Python since the it is written functionally, whereas we want to take an object-oriented approach.
The biggest achievement our team made this sprint was figuring out how to access and use the LFP data provided by our client.
Initially we struggled to access the data because it was given to us in .pl2 files. These can only be viewed by software like PlexUtil
or opened with functions like those found in the Plexon Python SDK. We learned how to use the Plexon SDK and get file info into a Python program.
We could access the data, but we realized we didn't understand it well enough to know how to use it in a Lasso predictor.
We reached out to our client who taught us how to read the data. We also did our own research looking into the provided MatLab code and SDK documentation.
Our client requested that we begin with creating a model that predicts on control vs experiment groups
so that we can develop the skills needed to work on long term goal of building a model that makes predictions on continuous variables.
Once we understood the data more clearly we developed a prototype algorithm for processing the data into power and coherence values,
along with predicting on control vs experiment groups using a small dataset.

## Unfinished Work
We did not finish creating the control vs experiment binary predictor. We will finish this next sprint so that in the following semester we will have the experience necessary to tackle the continuous predictor our client wants.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/26
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/13
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/20
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/19
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/18
 
 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint:
 
 * All of the below issues were closed for the same reason. As discussed in the work summary,
 * we started this sprint by translating the provided MatLab code to Python in order
 * to understand the algorithms designed by our client and the previous capstone team, but 
 * changed our focus to writing new Python code once we had sufficient understanding of
 * the previous work.
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/17
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/16
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/15
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/14
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/12
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/11
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/9
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/8
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/7

## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * A-D Lasso Predictor.py https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/blob/main/pythonProject/A-D%20Lasso%20Predictor.py
 * Print_pl2.py https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/blob/main/pythonProject/Print_pl2.py
 
## Retrospective Summary
Here's what went well:
  * We finished the tasks we wanted to complete this sprint (accessing and processing the data).
  * Good communication between team members.
 
Here's what we'd like to improve:
   * Turn in documents on time.
   * Utilize GitHub tools better to improve our workflow (use tags and milestones for example).
  
Here are changes we plan to implement in the next sprint:
   * Including issues in milestones.
   * Tagging issues.
   * Including branches that relate to modules instead of team members. This will allow for each team member to work on different modules easier.
   * Add test cases for code.