# Sprint x Report (2/3/2023 - 3/2/2023)

## What's New (User Facing)
 * Data preprocessing for binary model that predicts on whether a rodent is room air or vapor
 * Building a lasso model that predicts on whether a rodent is room air or vapor
 * Data preprocessing for continuous model that predicts alcohol consumption over the course of an experiment session
 * Building a lasso model that predicts alcohol consumption over the course of an experiment session

## Work Summary (Developer Facing)
During this sprint our team finished the data preprocessing and model building for the two tasks assigned to us 
while our client continues to prepare the data for our primary task. We have files prepared that preprocess data 
for the binary and continuous predictors they requested, as well as files that build models using that data. 
Additionally, we began running stochastic testing on our models. We found their accuracy to be lacking, and after 
consulting our client we concluded that we most likely need more data to improve the accuracy. This conclusion 
was reinforced by the fact that our client is in the process of preparing more data for us. We also began testing
lambda values across a series of model fits to determine what the best lambda value could be.

## Unfinished Work
We did not get the chance to set up the API file that interfaces with our preprocessing and logic modules.
We did not set up the continous predictor's preprocessing to have the functionality to process data from only
control males, control females, experiment males, and experiment females. Currently it only splits based on sex.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/56
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/59
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/61
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/55
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/53
 
 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint:
 
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/67  This issue was not finished due to time constraints.
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/68  This issue was not finished due to time constraints.

## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * LocalLogicModule.py   https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/blob/main/pythonProject/LocalLogicModule.py
 * Preprocessing_Module_Binary_Classifier.py   https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/blob/main/pythonProject/Preprocessing_Module_Binary_Classifier.py
 * Preprocessing_Module_Continuous_Classifier.py   https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/blob/main/pythonProject/Preprocessing_Module_Continuous_Classifier.py
 
## Retrospective Summary
Here's what went well:
  * We made good progress on multiple modules.
  * We began predicting on data and collecting accuracies of our models.
 
Here's what we'd like to improve:
   * Create GitHub issues for new tasks when they arise, not when we are finished with our current task.
   * Attach issues to milestones!
  
Here are changes we plan to implement in the next sprint:
   * Write the API module.
   * Include test more test cases.
   * Perform more stochastic testing once we receive more data from our client.