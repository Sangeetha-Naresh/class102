import cv2

def takesnapshot():
    videocaptureobj=cv2.VideoCapture(0)
    result=True
    while result:
        ret,frame=videocaptureobj.read()
        cv2.imwrite("newpicture1.jpg",frame)
        result=False

    videocaptureobj.release()
    cv2.destroyAllWindows()

takesnapshot()

