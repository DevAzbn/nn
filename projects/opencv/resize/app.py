import numpy as np
import cv2

image = cv2.imread('photo.jpg', cv2.IMREAD_UNCHANGED)
resized = image

# dim = (128, 128)

# resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
# # # resized = image
# resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
# max = np.absolute(resized).max()
# resized = resized / max
# resized = np.round(resized)

# # low_с = (200,200,200)
# # high_с = (255,255,255)
# # colored_img = cv2.inRange(resized, low_с, high_с)
# # cv2.imshow("Colored image", colored_img)

# (B, G, R, A) = cv2.split(resized)
# B = cv2.bitwise_and(B, B, mask=A)
# G = cv2.bitwise_and(G, G, mask=A)
# R = cv2.bitwise_and(R, R, mask=A)
# resized = cv2.merge([B, G, R, A])


# mask = cv2.imread('logo.png', 0)
# resized = cv2.inpaint(resized, mask, 100, cv2.INPAINT_TELEA)

# edges = cv2.Canny(resized, 50, 150, apertureSize = 3)
# resized = cv2.inpaint(resized, edges, 3, cv2.INPAINT_TELEA)

# alpha = 1.0
# beta = -100
# resized = alpha * resized + beta
# resized = np.clip(resized, 0, 255).astype(np.uint8)

# mask = np.zeros(resized.shape[:1], np.uint8)
# resized = cv2.inpaint(resized, mask, 3, cv2.INPAINT_TELEA)

# ret, thresh_img = cv2.threshold(resized, 180, 255, cv2.THRESH_BINARY_INV)#cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU
# cv2.imshow('grey image',thresh_img)
# # cv2.imwrite("result11.jpg", thresh_img)


# rows,cols,ch = resized.shape
# pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
# pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
# M = cv2.getPerspectiveTransform(pts1, pts2)
# resized = cv2.warpPerspective(resized, M, (600,600))


cv2.imshow("Resize image", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()