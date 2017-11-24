# I don't like hardcoded values :P
# This should go to a json or a config file, but this is fine for now

import os

TIMESTEPS = 10
INPUT_DATA_DIM = 3
OUTPUT_DATA_DIM = 5

BATCH_SIZE = 32
EPOCHS = 120
VALIDATION_SPLIT = 0.1
VERBOSITY = 1

NB_HIDDEN_NEURONS = 128
GRU_ACTIVATION = "tanh"
DENSE_ACTIVATION = "softmax"
OPTIMIZER = "rmsprop"
LOSS_FUNCTION = "sparse_categorical_crossentropy"

DATA_FOLDER_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
MODEL_TRAINING_FOLDER_PATH = os.path.join(DATA_FOLDER_PATH, "model_training_data")
TENSORBOARD_LOGGER_FOLDER_PATH = os.path.join(MODEL_TRAINING_FOLDER_PATH, "tensorboard_logs")
CSV_LOG_FILE_PATH = os.path.join(MODEL_TRAINING_FOLDER_PATH, "training.csv")
TEST_DATA_FOLDER_PATH = os.path.join(DATA_FOLDER_PATH, "test_data")
TRAIN_DATA_FOLDER_PATH = os.path.join(DATA_FOLDER_PATH, "train_data")
ACCURACY_PLOT_FILE_PATH = os.path.join(MODEL_TRAINING_FOLDER_PATH, "training_accuracy.png")
LOSS_PLOT_FILE_PATH = os.path.join(MODEL_TRAINING_FOLDER_PATH, "training_loss.png")
MODEL_VISUALIZATION_FILE_PATH = os.path.join(MODEL_TRAINING_FOLDER_PATH, "model.png")
