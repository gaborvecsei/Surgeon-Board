from keras.layers import GRU, Activation, Dense
from keras.models import Sequential

from surgeon_board.gesture_recognition_by_accelerometer.gesture_recognition_constants import GRU_ACTIVATION, \
    DENSE_ACTIVATION, OPTIMIZER, LOSS_FUNCTION


def create_model_v1(input_data_dimension, time_steps, output_dim):
    model = Sequential()
    model.add(GRU(128, input_shape=(time_steps, input_data_dimension)))
    model.add(Activation(GRU_ACTIVATION))
    model.add(Dense(output_dim))
    model.add(Activation(DENSE_ACTIVATION))
    model.compile(loss=LOSS_FUNCTION, optimizer=OPTIMIZER, metrics=['accuracy'])
    return model
