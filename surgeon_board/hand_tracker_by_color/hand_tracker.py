import cv2
import numpy as np
import sys
import color_tracker
from surgeon_board.hand_tracker_by_color.hand_tracker_constants import HSV_UPPER_FILE_PATH, HSV_LOWER_FILE_PATH, \
    KERNEL_FILE_PATH


def tracker_callback():
    debug_image = tracker.get_debug_image()
    cv2.imshow("hand tracking", debug_image)

    key = cv2.waitKey(1)
    if key == 27:
        tracker.stop_tracking()
        webcam.release_camera()
        cv2.destroyAllWindows()


try:
    hsv_lower = np.load(HSV_LOWER_FILE_PATH)
    hsv_upper = np.load(HSV_UPPER_FILE_PATH)
    kernel = np.load(KERNEL_FILE_PATH)
except FileNotFoundError:
    print("[*] At first you need to run the Hand Tracker Setup!")
    sys.exit(1)

webcam = color_tracker.WebCamera(video_src=0)
webcam.start_camera()
tracker = color_tracker.ColorTracker(camera=webcam, max_nb_of_points=10)

tracker.set_tracking_callback(tracking_callback=tracker_callback)
tracker.track(hsv_lower_value=hsv_lower, hsv_upper_value=hsv_upper, min_contour_area=100, min_track_point_distance=0)
