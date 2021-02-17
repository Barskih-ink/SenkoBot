import cv2 as cv
import numpy as np

screenshot = cv.imread('Senko.png', cv.IMREAD_UNCHANGED)
searchface = cv.imread('Senkoface.png', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(screenshot, searchface, cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result) 

print('Координата: %s' % str(max_loc))
print('Ебаната: %s' % max_val)

ebanata = 0.3
if max_val >= ebanata:
    print('Вот она! Туточки!')
    face_w = searchface.shape[1]
    face_h = searchface.shape[0]

    
    top_left = max_loc
    bottom_right = (top_left[0] + face_w, top_left[1] + face_h)

 
    cv.rectangle(screenshot, top_left, bottom_right, 
                    color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

  
    cv.imwrite('result.jpg', screenshot)

else:
    print('Тут нету Сенко!')
