import numpy as np
import cv2 as cv
frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture('.\Videos\DSC_4811.mp4')
size = (frameWidth, frameHeight)
fgbg = cv.createBackgroundSubtractorMOG2()
feature_params = dict(maxCorners=1,qualityLevel=.6,minDistance=25,blockSize=9)
result = cv.VideoWriter('output.avi', 
                         cv.VideoWriter_fourcc(*'MJPG'),
                         10, size)
while True:
    ret, oframe = cap.read()
    if oframe is None:
        break
    oframe = cv.resize(oframe, (frameWidth, frameHeight))

    mask = fgbg.apply(oframe)
    frame = cv.morphologyEx(mask,cv.MORPH_OPEN,np.ones((5,5),np.uint8))

    ball = cv.goodFeaturesToTrack(frame,**feature_params)
    if ball is not None:
        x,y = ball[0][0]
        cv.circle(oframe,(int(x),int(y)),8,(180,180,0),2)

    cv.imshow("Track", oframe)
    result.write(oframe)

    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break

result.release()