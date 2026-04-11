import cv2

# Webcam start
cam = cv2.VideoCapture(0)

# Frame capture
status, image = cam.read()

if status:
    # Image save
    cv2.imwrite("ammar.jpg", image)
    print("Picture captured successfully")
else:
    print("Picture not captured")

# Camera release
cam.release()




