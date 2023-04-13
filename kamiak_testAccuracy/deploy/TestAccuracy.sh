#!/bin/bash
#SBATCH --job-name=TestAccuracy
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=12
#SBATCH --mem-per-cpu=8G
#SBATCH --time=02:00:00

export PYTHON_VERSION="3.9.5"
export PROJECT_NAME="kamiak_testaccuracy"
export PROJECT_PATH="/home/$(whoami)/$PROJECT_NAME"
export VENV_PATH="$PROJECT_PATH/.env"
export INPUT_DATA_FILE="FemaleData.xlsx"

module load python3/$PYTHON_VERSION # Load in python3.9.5 and set it to the globally used version of Python
python3 -m venv $VENV_PATH # Create a virtual environment in .env
source $VENV_PATH/bin/activate # Activate the virtual environment
export PATH=$VENV_PATH/bin:$PATH # Add virtual environment executables to the path
pip install -r "$PROJECT_PATH/requirements-$PYTHON_VERSION.txt" # Install all required pips from requirements file
cd $PROJECT_PATH/src # cd into where Python files are stored
python LocalLogicModule.py $PROJECT_PATH/data/$INPUT_DATA_FILE # run the Python script

# to run, `sbatch deploy/TestAccuracy.sh`