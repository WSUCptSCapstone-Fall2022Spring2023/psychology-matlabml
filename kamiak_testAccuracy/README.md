# Guide 

## Prerequisites

 - Ubuntu (preferable v18.04)
 - Python v3.9.5
 - Python dependencies installed by running `pip install -r requirements-3.9.5.txt`
 - SSH Authentication setup with Kamiak
 - :brain: & :computer:

## How to add files to kamiak
```bash
# In a bash terminal:
$ rsync -avz folder_to_upload your.name@kamiak.wsu.edu

# For example:
$ rsync -avz /mnt/c/Users/charl/Desktop/kamiak_test3 charles.nickerson@kamiak.wsu.edu
```

## How to run the lasso models on kamiak

1. SSH into kamiak using ssh `your.name@kamiak.wsu.edu`, ex. `charles.nickerson@kamiak.wsu.edu`
2. cd into uploaded folder, ex. `cd ~/kamiak_test3`
3. `sbatch TestAccuracy.sh` This will run the bash file which creates and activates a virtual environment with all of the required dependencies and runs the python scripts. Before running this bash file you should check the configurations in the bash script to see if they are to your specifications.

4. Get details of currently running jobs by running `squeue -u your.name`, ex. `squeue -u charles.nickerson`. Make note of the Job Number and the ID of the Node the job is currently running on, ex. `35343355` and `cn195` respectively.

5. SSH into the compute node by running "ssh NODE_ID", ex. `ssh cn195`

6. cd into the directory of your project, ex. `cd ~/kamiak_test3` and find the slurm file containing the Job Number found in Step 4, ex. `slurm-35343355.out`. Tail the output currently being appended to the outfile using the tail command, ex. `tail -f slurm-35343355.out`.