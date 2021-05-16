import cv2
import dropbox
import time
import random

stime=time.time()

def takesnapshot():
    number=random.randint(0,100)
    videocaptureobj=cv2.VideoCapture(0)
    result=True
    while result:
        ret,frame=videocaptureobj.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        stime=time.time()
        result=False
    return img_name
    print("Snapshot Taken!!")
    videocaptureobj.release()
    cv2.destroyAllWindows()

takesnapshot()
