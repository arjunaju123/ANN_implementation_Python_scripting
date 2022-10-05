import tensorflow as tf
import os
import time
import numpy as np

def get_timestamp(name):

    timestamp = time.asctime().replace(" ","_").replace(":","_") #replace the spaces and special character : from the timestamp
    unique_name= f"{name}_at_{timestamp}"
    return unique_name

def get_callbacks(config,X_train):

    logs=config["logs"]
    
    unique_dir_name=get_timestamp("tb_logs")
    TENSORBOARD_ROOT_LOG_DIR = os.path.join(config["log_dir"],config["TENSORBOARD_ROOT_LOG_DIR"],unique_dir_name)

    os.makedirs(TENSORBOARD_ROOT_LOG_DIR,exist_ok=True) # exist_ok => If exists the log directory will be overwritten

    tensorboard_cb= tf.keras.callbacks.TensorBoard(logs_dir=TENSORBOARD_ROOT_LOG_DIR)

    file_writer = tf.summary.create_file_writer(logdir=TENSORBOARD_ROOT_LOG_DIR)

    with file_writer.as_default():

        images = np.reshape(X_train[10:30],(-1,28,28,1))
        tf.summary.image("20 handwritten digit samples",images,max_outputs=25,step=0)

    params = config["params"]

    early_stopping_cb= tf.keras.callbacks.EarlyStopping(patience=params["patience"],restore_best_weights=params["restore_best_weights"])

    #If the system crashes in between the training of an epoch using this callbacks it saves the last best epoch weights and we can resume the trainig using those weights.
    # It acts a back up and we dont have to start training all over again from first epoch.
    
    artifacts=config["artifacts"]
    CKPT_dir = os.path.join(artifacts["artifacts_dir"],artifacts["CHECKPOINT_DIR"])#Here no unique name is required because we want to save only best weights file every time.
    os.makedirs(CKPT_dir,exist_ok=True) 

    CKPT_path=os.path.join(CKPT_dir,"model_ckpt.h5")  #This is stored in checkpoint directory so create it first

    checkpointing_cb=tf.keras.callbacks.ModelCheckpoint(CKPT_path,save_best_only=True)

    return[tensorboard_cb,early_stopping_cb,checkpointing_cb]
