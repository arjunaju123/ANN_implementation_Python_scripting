# ANN_implementation_Python_scripting
ANN implementation using Python scripting

## IMPORTANT COMMANDS

[Conda environment management](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

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
