import os

DATA_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
HSV_LOWER_FILE_PATH = os.path.join(DATA_PATH, "hsv_lower.npy")
HSV_UPPER_FILE_PATH = os.path.join(DATA_PATH, "hsv_upper.npy")
KERNEL_FILE_PATH = os.path.join(DATA_PATH, "kernel.npy")
