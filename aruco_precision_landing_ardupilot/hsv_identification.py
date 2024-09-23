import cv2
import numpy as np

max_value_H = 255  # OpenCV uses 0-180 for Hue
max_value = 255
window_capture_name = "Video Capture"
window_detection_name = "Object Detection"

low_hue = 0
low_saturation = 0
low_value = 0
high_hue = max_value_H
high_saturation = max_value
high_value = max_value

def on_low_H_thresh_trackbar(val):
    global low_hue
    low_hue = val
    cv2.setTrackbarPos("Low H", window_detection_name, low_hue)

def on_high_H_thresh_trackbar(val):
    global high_hue
    high_hue = val
    cv2.setTrackbarPos("High H", window_detection_name, high_hue)

def on_low_S_thresh_trackbar(val):
    global low_saturation
    low_saturation = val
    cv2.setTrackbarPos("Low S", window_detection_name, low_saturation)

def on_high_S_thresh_trackbar(val):
    global high_saturation
    high_saturation = val
    cv2.setTrackbarPos("High S", window_detection_name, high_saturation)

def on_low_V_thresh_trackbar(val):
    global low_value
    low_value = val
    cv2.setTrackbarPos("Low V", window_detection_name, low_value)

def on_high_V_thresh_trackbar(val):
    global high_value
    high_value = val
    cv2.setTrackbarPos("High V", window_detection_name, high_value)

def main():
    cap = cv2.VideoCapture("/dev/video2")
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FPS, 10)

    cv2.namedWindow(window_capture_name)
    cv2.namedWindow(window_detection_name)

    cv2.createTrackbar("Low H", window_detection_name, low_hue, max_value_H, on_low_H_thresh_trackbar)
    cv2.createTrackbar("High H", window_detection_name, high_hue, max_value_H, on_high_H_thresh_trackbar)
    cv2.createTrackbar("Low S", window_detection_name, low_saturation, max_value, on_low_S_thresh_trackbar)
    cv2.createTrackbar("High S", window_detection_name, high_saturation, max_value, on_high_S_thresh_trackbar)
    cv2.createTrackbar("Low V", window_detection_name, low_value, max_value, on_low_V_thresh_trackbar)
    cv2.createTrackbar("High V", window_detection_name, high_value, max_value, on_high_V_thresh_trackbar)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame_threshold = cv2.inRange(frame_HSV, (low_hue, low_saturation, low_value), (high_hue, high_saturation, high_value))

        cv2.imshow(window_capture_name, frame)
        cv2.imshow(window_detection_name, frame_threshold)
        cv2.resizeWindow(window_capture_name, 480, 320)

        key = cv2.waitKey(30)
        if key == ord('q') or key == 27:  # 'q' or ESC key
            break

    print(f"ColorRange range;\nrange.lower_bound.ch1 = {int(low_hue / max_value_H * 255.0)};\nrange.lower_bound.ch2 = {low_saturation};\nrange.lower_bound.ch3 = {low_value};\n\n")
    print(f"range.upper_bound.ch1 = {int(high_hue / max_value_H * 255.0)};\nrange.upper_bound.ch2 = {high_saturation};\nrange.upper_bound.ch3 = {high_value};\n\n")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
