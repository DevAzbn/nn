import numpy as np
import cv2

image = cv2.imread('photo.jpg', cv2.IMREAD_UNCHANGED)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#преобразование в чб изображение
blur = cv2.GaussianBlur(gray, (0, 0), 5)# небольшое размытие для сглажеввания шумов
resized = cv2.resize(blur, (320, 240))# преобразование изображения к размеру 320*240

cv2.imshow("Resize image", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()