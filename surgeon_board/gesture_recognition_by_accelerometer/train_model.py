import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping, CSVLogger, TensorBoard, ReduceLROnPlateau

from surgeon_board.gesture_recognition_by_accelerometer import models
from surgeon_board.gesture_recognition_by_accelerometer.gesture_recognition_constants import INPUT_DATA_DIM, \
    OUTPUT_DATA_DIM, TIMESTEPS, BATCH_SIZE, EPOCHS, VALIDATION_SPLIT, VERBOSITY, TEST_DATA_FOLDER_PATH, \
    CSV_LOG_FILE_PATH, ACCURACY_PLOT_FILE_PATH, LOSS_PLOT_FILE_PATH, MODEL_VISUALIZATION_FILE_PATH

# input
X_train = []
# labels
y_train = []

# Create model
model = models.create_model_v1(INPUT_DATA_DIM, TIMESTEPS, OUTPUT_DATA_DIM)

# Create callbacks
early_stopping_callback = EarlyStopping(monitor="val_loss", patience=20, verbose=0, mode="auto")
csv_logger_callback = CSVLogger(CSV_LOG_FILE_PATH)
tensorboard_callback = TensorBoard(log_dir=TEST_DATA_FOLDER_PATH, histogram_freq=0, write_graph=True, write_images=True)
reduce_learning_rate_callback = ReduceLROnPlateau(monitor="val_loss", factor=0.2, patience=5, min_lr=0.001)

# Start training
history = model.fit(X_train, y_train, batch_size=BATCH_SIZE,
                    validation_split=VALIDATION_SPLIT,
                    callbacks=[early_stopping_callback, csv_logger_callback, tensorboard_callback,
                               reduce_learning_rate_callback],
                    nb_epoch=EPOCHS,
                    verbose=VERBOSITY)

# Visualize model & Training
models.save_model_plot(model, MODEL_VISUALIZATION_FILE_PATH)

plt.title('Model loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid()
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.legend()
plt.savefig(LOSS_PLOT_FILE_PATH)

plt.title('Model accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.grid()
plt.plot(history.history['acc'], label='acc')
plt.plot(history.history['val_acc'], label='val_acc')
plt.legend()
plt.savefig(ACCURACY_PLOT_FILE_PATH)
