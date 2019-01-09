import cv2

image = cv2.imread("matrix-sunglasses.jpg")

#cv2.imshow("Original image", image)

#размер (высота, ширина, глубина)
print(type(image), image.shape)


# Нам надо сохранить соотношение сторон
# чтобы изображение не исказилось при уменьшении
# для этого считаем коэф. уменьшения стороны
final_wide = 300
r = float(final_wide) / image.shape[1]
dim = (final_wide, int(image.shape[0] * r))

# уменьшаем изображение до подготовленных размеров
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resize image", resized)



## вырежем участок изображения используя срезы
## мы же используем NumPy
#cropped = resized[30:130, 150:300]
#cv2.imshow("Cropped image", cropped)



## получим размеры изображения для поворота
## и вычислим центр изображения
#(h, w) = resized.shape[:2]
#center = (w / 2, h / 2)
## повернем изображение на 180 градусов
#M = cv2.getRotationMatrix2D(center, 180, 1.0)
#rotated = cv2.warpAffine(resized, M, (w, h))
#cv2.imshow("Rotated image", rotated)



#отразим изображение по горизонтали
#flip_image = cv2.flip(resized,1)
#cv2.imshow("Flip image", flip_image)
# запишем изображение на диск в формате png
#cv2.imwrite("flip.png", flip_image)



#На выходе мы получаем черно-белое изображение, где белым выделены пиксели, цвета которых попадали в диапазон а черным – с цветом вне требуемого
#low_red = (0,0,128)
#high_red = (255,255,255)
#colored_img = cv2.inRange(resized, low_red, high_red)
#cv2.imshow("Colored image", colored_img)





#resized_hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV) #Преобразуем в HSV
#resized_color_low = (25,0,0)
#resized_color_high = (50,50,50)
#only_hsv = cv2.inRange(resized_hsv, resized_color_low, resized_color_high)
#cv2.imshow('only_hsv', only_hsv)


#moments = cv2.moments(only_hsv, 1) # получим моменты 
#x_moment = moments['m01']
#y_moment = moments['m10']
#area = moments['m00']
#x = int(x_moment / area) # Получим координаты x,y кота
#y = int(y_moment / area) # и выведем текст на изображение
#cv2.putText(resized, "It!", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2) 
#cv2.imshow('area founded', resized)



cv2.waitKey(0)
cv2.destroyAllWindows()