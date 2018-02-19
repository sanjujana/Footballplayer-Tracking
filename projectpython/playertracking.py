## Import necessary packages
import numpy as np
import cv2

## Inputting the video from File or Webcam
cap = cv2.VideoCapture('C:\\New folder\\finalvideo.mp4')
##cap = cv2.VideoCapture(0)


while True:
    

    ## Read the video frame by frame
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    ## Colour limit of Red
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    
    ## Colour limit of Yellow
    lower_yellow = np.array([20, 150, 150])
    upper_yellow = np.array([30, 255, 255])
    
    ## Colour limit of Blue
    lower_blue = np.array([110,100,100])
    upper_blue = np.array([130,255,255])

    ## Mask of frame for different colour
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_yello = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_yellow = mask_yello+mask_blue

    ## Result after masking the video frame by frame                     
##    res_r = cv2.bitwise_and(frame , frame , mask = mask_red)
##    res_y = cv2.bitwise_and(frame , frame , mask = mask_yello)

    ## Erosion & Dilation for Red
    kernel_r = np.ones((10,5),np.uint8)
    erosion_r = cv2.erode(mask_red, kernel_r, iterations = 1)
    dilation_r = cv2.dilate(mask_red, kernel_r, iterations = 4)
    
    ## Erosion & dilation for Yellow
    kernel_y = np.ones((12,5),np.uint8)
    erosion_y = cv2.erode(mask_yello, kernel_y, iterations = 1)
    dilation_y = cv2.dilate(mask_yello, kernel_y, iterations = 4)

##    img_r = cv2.cvtColor(res_r , cv2.COLOR_BGR2GRAY)
##    img_y = cv2.cvtColor(res_y , cv2.COLOR_BGR2GRAY)

    ## Countours for getting the edge of the player
    _, contours1 ,_ = cv2.findContours(dilation_r, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    _, contours2 ,_ = cv2.findContours(dilation_y, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    ## Draw rectangle covering the Red player
    for cnt in contours1:
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        img1 = cv2.drawContours(frame , [box] , 0 , [0,255,0] , 2)
        
    ## Draw rectangle covering the Yellow player    
    for cnt in contours2:
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        img1 = cv2.drawContours(frame , [box] , 0 , [255,255,255] , 2)

    ## Putting the text here
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame , 'Automatically PLAYER detection' , (500,80) , font , 1.5 , (0,255,255) , 3 , cv2.LINE_AA )
        
    ## Output image (Show thw video by showing images frame by frame)
    cv2.imshow('frame',frame)
##    cv2.imshow('HSV',hsv)
##    cv2.imshow('mask_red',mask_red)
##    cv2.imshow('mask_yellow',mask_yellow)
##    cv2.imshow('res_r',res_r)
##    cv2.imshow('res_y',res_y)
##    cv2.imshow('erosion_r',erosion_r)
##    cv2.imshow('dilation_r',dilation_r)
##    cv2.imshow('erosion_y',erosion_y)
##    cv2.imshow('dilation_y',dilation_y)
    

    if( cv2.waitKey(1) & 0xFF == ord('q')):
        break



cv2.destroyAllWindows()
cap.release()

    
