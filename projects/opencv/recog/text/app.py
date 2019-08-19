import cv2

image = cv2.imread('photo.jpg', cv2.IMREAD_UNCHANGED)
# resized = image
resized = cv2.resize(image, (800, 600))

resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
resized = cv2.GaussianBlur(resized, (5, 5), 0) #уменьшить резкость

resized = cv2.Canny(resized, 75, 200) #контуры объектов на изображении

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
resized = cv2.morphologyEx(resized, cv2.MORPH_CLOSE, kernel)

# контуры в изображении
cnts = cv2.findContours(resized.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
# общее число контуров
total = 0

# цикл по контурам
for c in cnts:
	# аппроксимируем (сглаживаем) контур
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)

	# если у контура 4 вершины, предполагаем, что это книга
	if len(approx) == 4:
		cv2.drawContours(resized, [approx], -1, (0, 255, 0), 4)
		total += 1

cv2.imshow('Resize image', resized)

cv2.waitKey(0)
cv2.destroyAllWindows()


# cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
 
# # loop over the contours
# for c in cnts:
# 	# approximate the contour
# 	peri = cv2.arcLength(c, True)
# 	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
 
# 	# if our approximated contour has four points, then we
# 	# can assume that we have found our screen
# 	if len(approx) == 4:
# 		screenCnt = approx
# 		break
 
# # show the contour (outline) of the piece of paper
# print("STEP 2: Find contours of paper")
# cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
# cv2.imshow("Outline", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# from __future__ import print_function
# from wand.image import Image
# with Image(filename='sample_doc.pdf') as img:
#     print('width =', img.width)
#     print('height =', img.height)
#     print('pages = ', len(img.sequence))
#     print('resolution = ', img.resolution)
# with img.convert('png') as converted:
#      converted.save(filename='sample_doc.png')
