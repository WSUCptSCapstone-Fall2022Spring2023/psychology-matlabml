# Sprint 3 Report (11/10/22 - 12/09/2022)

## What's New (User Facing)
 * We can build a model from data and calculate its accuracy!
 * We've tested an array of lambda values to find the most accurate one. Smaller lambdas have been shown to be more accurate.
 * The program can build a .csv file of power and coherence values along the six common frequency channels.

## Work Summary (Developer Facing)
During this sprint our team built the local logic module and preprocessing module for our project. 
In regards to the preprocessing module, we refactored the work done in the A-D Predictor file so that its algorithms are stored in classes contained in the preprocessing module.
The code in this module was refined to be more readable, efficient, and decoupled into class methods.
We also altered the data processing so that it split the power and coherence values based on the six common frequency channels.
Reviewing the previous Matlab code for insight on their approach to working with the data was very helpful and allowed us to create new appraoches using Python.
In regards to the logic module, we explored sklearn's lasso library and added functions for working with that library.
We also added functions to find the best lambda value for the model by testing the model's accuracy across multiple lambdas.

## Unfinished Work
We did not finish adding data cleaning to the preprocessing module due to time constraints. This will be addressed early in sprint 4.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/50
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/48
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/47
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/46
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/45
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/44
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/41
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/40
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/39
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/38
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/37
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/32
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/31
 
 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint:
 
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/49   Not completed due to time constraints
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/33   Ongoing issue that will be resolved in the future

## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * [LocalLogicModule.py] https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/blob/main/pythonProject/LocalLogicModule.py
 * [LocalLogicModuleTesting.py] https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/blob/main/TestEnvironment/LocalLogicModuleTesting.py
 * [A-D Lasso Predictor.py] https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/blob/Preprocessing_Module/pythonProject/A-D%20Lasso%20Predictor.py
 * [External_Data_Access_and_Preprocessing_Module.py] https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/blob/Preprocessing_Module/pythonProject/External_Data_Access_and_Preprocessing_Module.py
 * [test_External_Data_Access_and_Preprocessing_Module.py] https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/blob/Preprocessing_Module/pythonProject/Preprocessing%20Module%20Tests/test_External_Data_Access_and_Preprocessing_Module.py

## Retrospective Summary
Here's what went well:
  * Communication between team members
  * Amount of work completed / code committed to repo
  * Our demo with our client went well. They were pleased with our progress
  * Including issues and milestones
 
Here's what we'd like to improve:
   * More frequent pull requests
   * Linking issues to pull requests
  
Here are changes we plan to implement in the next sprint:
   * Linking issues to pull requests
   * Setting up more accurate sprint goals in terms what work will be completed