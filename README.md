# ANN_implementation_Python_scripting

ANN implementation using Python scripting

## IMPORTANT COMMANDS

[Conda environment commands](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

## IMPORTANT LINKS

[5 Reasons To Use YAML Files In Your Machine Learning Projects](https://towardsdatascience.com/5-reasons-to-use-yaml-files-in-your-machine-learning-projects-d4c7b9650f27)

[Command line argument processing using argparse](https://www.youtube.com/watch?v=OxpBMNalsDM)

### CREATING ENVIRONMENT BY Specifying a location for an environment

You can control where a conda environment lives by providing a path to a target directory when creating the environment. For example, the following command will create a new environment in a subdirectory of the current working directory called envs:

```bash
conda create --prefix ./envs python=3.7 -y
```
./ means current working directory

Add this envs/ folder to gitignore 
Also add .vscode/ and idea/ to gitignore

### Activate environment 

You then activate an environment created with a prefix using the same command used to activate environments created by name:

```bash
conda activate ./envs
```
conda env list

It will show the list of environments including our current working environment with no name as we are now working in current working directory.

### Bash commands used

* mkdir -p src/utils

* touch src/__init_.py

* touch src/utils/__init_.py

* touch setup.py

* touch src/training.py

* touch src/utils/model.py src/utils/data_management.py src/utils/common_utils.py

* touch config.yaml

* pip install PyYAML

* python

  1. from src.utils.common_utils import read_config
  2. read_config("config.yaml") 
  3. exit()

* python src/training.py

## A module is defined as:

1. either a Python file that is, a file on disk that ends in .py and contains valid Python (syntax errors, for example, will stop you from being able to import a file)

2. or a directory (aka folder) which contains Python files.
for a directory to become a module, it must contain a special file called __init_.py