# ANN_implementation_Python_scripting

ANN implementation using Python scripting

## IMPORTANT COMMANDS

[Conda environment commands](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

## IMPORTANT LINKS

[5 Reasons To Use YAML Files In Your Machine Learning Projects](https://towardsdatascience.com/5-reasons-to-use-yaml-files-in-your-machine-learning-projects-d4c7b9650f27)

[Command line argument processing using argparse](https://www.youtube.com/watch?v=OxpBMNalsDM)

[A Practical Guide to Using Setup.py](https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/)

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

* pip install -e .

The . here refers to the current working directory, which I assume to be the directory
where the setup.py can be found. The -e flag specifies that we want to install
in editable mode, which means
that when we edit the files in our package we do not need to re-install the
package before the changes come into effect. You will need to either restart
python or reload the package though!

When you edit information in the setup.py itself you will need to re-install
the package in most cases, and also if you add new (sub)packages.
When in doubt, it can never hurt to re-install. Just run pip install -e . again.

## A module is defined as:

1. either a Python file that is, a file on disk that ends in .py and contains valid Python (syntax errors, for example, will stop you from being able to import a file)

2. or a directory (aka folder) which contains Python files.
for a directory to become a module, it must contain a special file called __init_.py

## Pycharm settings setup 
### Commands used

1. conda create --prefix ./envs python=3.7 -y
2. source activate ./envs 
(conda activate ./envs) doesnt work

3. settings << Project interpreter << Add << Conda environment <<Existing environment << choose interpreter from files (here it is in envs folder inside project folder)
4. settings << tools << terminal << select shell path as C:\Program Files\Git\bin\bash.exe