import cv2
from ultralytics import YOLO
import os

model = YOLO('yolov8n.pt')
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
video_filename = 'test.mp4'

video_path = os.path.join(desktop_path, video_filename)

cap = cv2.VideoCapture(video_path)

ret = True

#read frames
while ret:
    ret, frame = cap.read()

    if ret:

        #detect objects
        #track objects
        results = model.track(frame, persist=True)

        #plot results
        frame_ = results[0].plot()

        #visualize
        cv2.imshow('frame', frame_)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

