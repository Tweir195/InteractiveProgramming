
import cv2
import numpy as np
import math

"""capturing video from camera"""
cap = cv2.VideoCapture(0)
frame_num = 0
cx = 0
cy = 0
path = []
clearpath = []

while(True):
    #capture frame by frame
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #find specific color
    lower_white = np.array([[0, 0, 230]])
    upper_white = np.array([180, 25, 255])
    lower_color = np.array([0,80,50])
    upper_color = np.array([20,100,100])
    lower_red = np.array([150,150,50])
    upper_red = np.array([180,255,150])


    mask1 = cv2.inRange(hsv, np.array([0, 150, 100]), np.array([1, 255, 255]));
    mask2 = cv2.inRange(hsv, np.array([178, 150, 100]), np.array([180, 255, 255]));
    mask = mask1 | mask2

    # Attempting Green
    # mask = cv2.inRange(hsv, np.array([50,100,100]), np.array([65,255,255]))

    mask = cv2.bilateralFilter(mask, 10, 40, 40)
    mask = cv2.blur(mask,(5,5))

    res = cv2.bitwise_and(frame,frame,mask=mask)
    mask = cv2.blur(mask,(20,20))
    # Getting a contour and the center of the contour
    im2,contours,hierarchy = cv2.findContours(mask, 1, 2)
    try:
        if frame_num > 0 or frame_num == 0:
            cnt = contours[0]
            M = cv2.moments(cnt)
            # print(M['m10']/M['m00'])
            cx = int(M['m10']/M['m00'])
            # print(cx)
            cy = int(M['m01']/M['m00'])
            # print(cy)
            frame_num = 0
            path.append((cx, cy))
            # if diffx > 100 or diffy > 100:
            #     print('too far')
            # else:
        cv2.circle(res, (cx, cy), 2, (0, 255, 0), -1)
    except IndexError:
        """"""

    # TODO: Add if statements to make sure that any outliers
    # would be removed from the list or ignored when drawing
    # the linewidth
    if len(path) == 1:
        clearpath.append(path[0])
    elif len(path) > 2:
        pair = path[-2]
        # print(pair, pair[0], cx, pair[1], cy)
        diffx = abs(cx-pair[0])
        diffy = abs(cy-pair[1])
        distance = math.sqrt(diffx**2+diffy**2)
        if distance<10:
            clearpath.append(pair)

    for i in range(len(clearpath)):
        if len(clearpath) < 1:
            break
        # elif math.sqrt(diffx**2+diffy**2) > 30:
            # break
        elif i < (len(clearpath)-1):
            cv2.line(res, clearpath[i], clearpath[i+1], (255,0,0), 3)

    print(path)
    print(clearpath)
    frame_num += 1
    # cnts = cv2.findContours(res, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #display the resulting frame
    cv2.imshow('frame',frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('res',res)
    # cv2.imshow('counto', )
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#when finshed, release the capture
cap.release()
cv2.destroyAllWindows()
"""playing video from file
cap = cv2.VideoCapture('test.avi')

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.waitKey(25)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
"""
