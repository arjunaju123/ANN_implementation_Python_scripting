import tensorflow as tf
import time #To create unique file name
import os #To save the model
import pandas as pd
import matplotlib.pyplot as plt

def create_model(LOSS_FUNCTION,OPTIMIZER,METRICS,NUM_CLASSES):

    LAYERS = [tf.keras.layers.Flatten(input_shape=[28, 28], name="inputLayer"),
          tf.keras.layers.Dense(300, activation="relu", name="hiddenLayer1"),
          tf.keras.layers.Dense(100, activation="relu", name="hiddenLayer2"),
          tf.keras.layers.Dense(NUM_CLASSES, activation="softmax", name="outputLayer")]

    model_clf = tf.keras.models.Sequential(LAYERS)

    model_clf.summary()

    # LOSS_FUNCTION = "sparse_categorical_crossentropy" # use => tf.losses.sparse_categorical_crossentropy
    # OPTIMIZER = "SGD" # or use with custom learning rate=> tf.keras.optimizers.SGD(0.02)
    # METRICS = ["accuracy"]

    model_clf.compile(loss=LOSS_FUNCTION,
                optimizer=OPTIMIZER,
                metrics=METRICS)

    return model_clf # =>untrained model

def get_unique_filename(filename):
    unique_filename=time.strftime(f"%Y%m%d-%H%M%S_{filename}")
    return unique_filename

def save_model(model,model_name,model_dir):
    unique_filename=get_unique_filename(model_name)
    path_to_model=os.path.join(model_dir,unique_filename)
    model.save(path_to_model)

    # Inside artifacts folder there will be model folder inside which the model will be saved each time with unique model name

def save_plot(loss_acc, plots_name,plots_dir_path):
    unique_filename = get_unique_filename(plots_name)
    path_to_plot = os.path.join(plots_dir_path, unique_filename)
    pd.DataFrame(loss_acc).plot(figsize=(10, 7))
    plt.grid(True)
    plt.savefig(path_to_plot)
