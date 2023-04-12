# Sprint x Report (3/3/2023 - 4/2/2023)

## What's New (User Facing)
 * Added 5-second batching to data preprocessing in order to artificially increase the amount of data we are using to build a predictive model.
 * Added a method for creating a config file for setting properties for building models.
 * Added a method for updating the config class based on the config file.
 * Wrote a guide on using Kamiak to train models and use them to make predictions.
 * Wrote a script that can be ran on Kamiak as an example for our client.

## Work Summary (Developer Facing)
After the poor accuracy results of our previously built models, our client recommended that we split the training data into 5-second batches of power and coherence, 
rather than the power and coherence of an entire file.
We spent time making duplicate methods in our preprocessing module that can build models using this method. 
We also started working on integrating Kamiak into our software. Initially we tried using Kamiak to perform data preprocessing,
but Kamiak runs on Linux, and the Plexon DLL we use to read .pl2 files only runs on windows. 
As a result, we can only use Kamkiak to build models using data that has been preprocessed locally and make predictions on those models.
We ran accuracy tests using Kamiak. These runs executed quickly, which will be pleasing to our client.
We implemented a function that finds config attributes and saves them to a file, and another function that sets config parameters based on the previously built file. This will make editing config parameters in the future easier for our client.

## Unfinished Work
We finished the 5-second batching for the binary preprocessing, but did not have time to include this feature to the continuous preprocessor due to time constraints set by midterm exams.
Additionally, one issue we encountered is that the feature header needed for the 5-second batched features is thousands of items long, so a new header algorithm needs to be designed to conveniently label each feature in the pandas dataframe.
We also did not split Power and Coherence data by control and experiement for the continuous preprocessing. This is due to the assigned team member taking time to finish other issues for this sprint instead.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/70
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/72
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/73
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/75
 
 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint:
 
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/74 This issue was not finished due to time contraints.
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/68 We prioritized other issues over this one this sprint.
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/71 This issue was not finished due to time constraints.
 * https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/issues/67 This issue was not finished due to the team deciding they needed to reevaluate the goal of the issue.

## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * [API_Controller.py] https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/blob/API_Controller/pythonProject/API%20Controller.py
 * [Preprocessing_Module_Binary_Classifier.py] https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/blob/Local_Logic_Module/pythonProject/Preprocessing_Module_Binary_Classifier.py
 * [kamiak_testAccuracy] https://github.com/WSUCptSCapstone-Fall2022Spring2023/psychology-matlabml/tree/Kamiak_Logic_Module/kamiak_testAccuracy
 
## Retrospective Summary
Here's what went well:
  * We covered a lot of ground regarding using Kamiak and getting closer to completing our project.
 
Here's what we'd like to improve:
   * We found that communication between team members fell behind this sprint. We want to finish strong during our upcoming final sprint.
  
Here are changes we plan to implement in the next sprint:
   * We would like to make more scripts for sending code files to be run on Kamiak.
   * We want to finish our preprocessing modules and make a variety of models for testing.
   * Clean up unused files, as well as include robust commenting to files that we intend on presenting to our client.