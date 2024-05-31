import cv2

def test_camera(index):
    cap = cv2.VideoCapture(index)
    if cap is None or not cap.isOpened():
        print('Warning: unable to open video source: ', index)
    else:
        print('Success: able to open video source: ', index)
        cap.release()

for i in range(10):
    test_camera(i)
