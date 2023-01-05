import cv2
cap = cv2.VideoCapture(0);#Try -1,0 for find the camera and 2,3... for multiple camera

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xff == ord('c'):
        break;
cap.release()
cv2.destroyAllWindows()