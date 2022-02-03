
# CTRL+K then CTRL+C adds the # in VS for selected lines. CTRL+K then CTRL+U removes the # in VS for selected lines.

# sys.path is a built-in variable within the sys module. It contains a list of directories that the interpreter will search in for the required module. 

#When a module(a module is a python file) is imported within a Python file,
#the interpreter first searches for the specified module among its built-in modules.
#If not found it looks through the list of directories(a directory is a folder that contains related modules) defined by sys.path.
#first string returned by path is always empty this is to indicate the interpreter to check in the current directory.

from src.utils.common_utils import read_config
from src.utils.data_management import get_data
from src.utils.model import create_model

import argparse

def training(config_path):
    config = read_config(config_path)

    validation_datasize = config ["params"]["validation_datasize"]
    (X_train, y_train),(X_valid, y_valid), (X_test, y_test)= get_data(validation_datasize)

    #print(config)

    LOSS_FUNCTION= config ["params"]["loss_function"]
    OPTIMIZER= config ["params"]["optimizer"]
    METRICS= config ["params"]["metrices"]
    NUM_CLASSES=config ["params"]["no_classes"]

    model= create_model(LOSS_FUNCTION,OPTIMIZER,METRICS,NUM_CLASSES)

    EPOCHS = config ["params"]["epochs"]
    VALIDATION_SET = (X_valid, y_valid)

    history = model.fit(X_train, y_train, epochs=EPOCHS,
                        validation_data=VALIDATION_SET)

if __name__ == '__main__':

    args=argparse.ArgumentParser()

    args.add_argument('-c', '--config',default="config.yaml")

    parsed_args = args.parse_args()

    training(config_path=parsed_args.config)