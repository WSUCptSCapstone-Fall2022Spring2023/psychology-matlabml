# Sprint 7 Report (4/2/23 - 5/2/23)

## What's New (User Facing)
 * Added a filter for room air and vapor rats for continuous preprocessing.
 * Added the capability for saving and loading models.
 * Added warmstarting when building multiple models.
 * Multiple preprocessed dataframes can be inputted when building a model.
 * Beautified mains for LocalLogicModule.py and the Preprocessing Modules for client use.
 * Added a document for how to use our software.

## Work Summary (Developer Facing)
We finally updated continuous preprocessing module to allow users to filter their data by room air and vapor air. Additionally, we added warmstarting during model construction. This helps speed model building when a user is building multiple models. We also included the capability for multiple dataframes to be loaded in when building model so that 
data does not have to be re-preprocessed.

## Unfinished Work
We did not improve the batching header for X-second batches. This was mainly because the X-second batches did not
increase accuracy substantially, so we decided not to pursue that feature anymore.
We also did not set up the API Module so that we had one file that can run processes from all other modules.
This was because we realized that keeping each file self-contained would make them more accessible to our client.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/68
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/85
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/71

 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint:
 
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/74 This issue was no longer deemed important
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/67 This issue was no longer deemed necessary

## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * [Load_Data.py](https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/blob/main/pythonProject/Load_Data.py)
 * [LocalLogicModule.py](https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/blob/main/pythonProject/LocalLogicModule.py)
 * [Preprocessing_Module_Continuous_Classifier](https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/blob/main/pythonProject/Preprocessing_Module_Continuous_Classifier.py)
 * [Preprocessing_Module_Binary_Classifier](https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/blob/main/pythonProject/Preprocessing_Module_Binary_Classifier.py)
 
## Retrospective Summary
Here's what went well:
  * Good communication between clients and peers
  * Documentation
  * Buidling models has become significantly faster.
 
Here's what we'd like to improve:
   * Speed of data preprocessing
   * Updating GitHub with issues