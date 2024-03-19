import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not open camera")
    exit()

ret, frame = camera.read()

cv2.imshow('Frame', frame)

cv2.waitKey(0)

camera.release()
