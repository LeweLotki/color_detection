import cv2 
import numpy as np 
import random

points = []
def detection(list, array):
    temp = []
    for val in list:
        if array[val[0],val[1],0] < 50 and array[val[0],val[1],1] < 50 and array[val[0],val[1],2] > 220:
            temp.extend([[val[0],val[1]]])
    list.clear()
    list.extend(temp)
    
def resultant(list):
    result = 0 
    all_x = 0
    all_y = 0
    lenght = len(list)
    if lenght == 1:
        result = list[0]
    elif lenght > 1:
        for val in list:
            all_x += val[0]
            all_y += val[1]
        all_x = int(all_x/lenght)
        all_y = int(all_y/lenght)
        result = [all_x,all_y]
    
    return result
    
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
   
if (cap.isOpened()== False):  
  print("Error opening video  file")
ret, frame = cap.read()  
n =  int((frame.shape[0]*frame.shape[1])**0.5)

while(cap.isOpened()): 
    m = 0
    ret, frame = cap.read()

    while m < n:
        x = random.randint(0, frame.shape[0]-1)
        y = random.randint(0, frame.shape[1]-1)
        points.extend([[x,y]])
        m += 1
    # print(points)    
    detection(points, frame) 

    if ret == True: 
        if len(points) > 0:
            aim = resultant(points)  
            frame[aim[0] - 20 : aim[0] + 20, aim[1] - 20 : aim[1] + 20 ,:] = (0,0,0)
        points.clear()
        cv2.imshow('Frame', frame) 

        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break

    else:  
        break
   
cap.release() 

cv2.destroyAllWindows() 
