import color_tracker
import numpy as np
from surgeon_board.hand_tracker_by_color.hand_tracker_constants import HSV_LOWER_FILE_PATH, HSV_UPPER_FILE_PATH, KERNEL_FILE_PATH

webcam = color_tracker.WebCamera(video_src=0)
webcam.start_camera()

range_detector = color_tracker.HSVColorRangeDetector(webcam)
hsv_lower, hsv_upper, kernel = range_detector.detect()

np.save(HSV_LOWER_FILE_PATH, hsv_lower)
np.save(HSV_UPPER_FILE_PATH, hsv_upper)
np.save(KERNEL_FILE_PATH, kernel)

print("[*] Hand Tracker Setup finished")
