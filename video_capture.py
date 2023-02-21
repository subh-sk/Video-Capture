import cv2
import datetime
import pyttsx3

filename=str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f'))+".mp4" #filename of recording video
print(filename)
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)#0 mean 1 camera that in your system. 1 mean 2 camera
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)

fourc=cv2.VideoWriter_fourcc('m','p','4','v')
writer = cv2.VideoWriter(filename,fourc,10.0,(1280,720))  #10.0 is resolution

recording=False


    

while True:
    ret,frame=cap.read()
    if ret:
        cv2.imshow("video",frame)
        if recording:
            writer.write(frame)
    key=cv2.waitKey(1)  #frame rate in millisecond
    if key== ord('q'):
        break
    elif key==ord('r'):
        recording= not recording
        print(f"Recording = {recording}")
        

cap.release()
writer.release()
cv2.destroyAllWindows()