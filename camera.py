<<<<<<< HEAD
=======
import cv2
import numpy as np
import keyboard


cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()
    gray_vid = cv2.cvtColor(frame, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Original',frame)
    edged_frame = cv2.Canny(frame,100,200)
    cv2.imshow('Edges',edged_frame)
    k= cv2.waitKey(5) & 0xFF
    if keyboard.is_pressed('q'):  # if key 'q' is pressed 
        print('You Pressed A Key!')
            
        cv2.imwrite('images/c1.png',frame)
        break  # finishing the loop
    
# Quit with 'Esc' key
    
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
>>>>>>> 0a0c9c069769c0f372876ea4b65c8f46e001acb4
