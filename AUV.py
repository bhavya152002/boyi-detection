import cv2 as cv
import numpy as np

lower_blue = np.array([100,60,100])
upper_blue = np.array([180,255,255])
lower_green = np.array([50, 20,90])
upper_green = np.array([80, 255, 255])
lower_red = np.array([60, 140,200])
upper_red = np.array([180, 255, 255])
while(1):
    frame = cv.imread('/home/bhavya/Pictures/task 1.png')
    image = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
   
    blue_mask = cv.inRange(image, lower_blue, upper_blue)
    green_mask = cv.inRange(image, lower_green, upper_green)
    red_mask = cv.inRange(image, lower_red, upper_red)

    contours, hierarchy = cv.findContours(blue_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv.contourArea(contour)
        if(area > 300):
            x, y, a, b = cv.boundingRect(contour)
            frame = cv.rectangle(frame, (x, y), (x + a, y + b), (180, 0, 0), 2)
            M = cv.moments(contour)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv.circle(image, (cx, cy), 6, (0, 255, 0), 5)
            cv.putText(frame, "blue color", (x, y), cv.FONT_HERSHEY_SIMPLEX, 1.0,(180, 0, 0))  

    contours, hierarchy = cv.findContours(green_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv.contourArea(contour)
        if(area > 300):
            x, y, a, b = cv.boundingRect(contour)
            frame = cv.rectangle(frame, (x, y), (x + a, y + b), (0, 255, 0), 2)
            cv.putText(frame, "green color", (x, y), cv.FONT_HERSHEY_SIMPLEX, 1.0,(0, 255, 0)) 

    contours, hierarchy = cv.findContours(red_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv.contourArea(contour)
        if(area > 300):
            x, y, a, b = cv.boundingRect(contour)
            frame = cv.rectangle(frame, (x, y), (x + a, y + b), (0, 0, 255), 2)
            cv.putText(frame, "red color", (x, y), cv.FONT_HERSHEY_SIMPLEX, 1.0,(0, 0, 255)) 


    
    cv.imshow("normal image", frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
