import cv2
import numpy
img = cv2.imread('color_text.jpg')
new_img = numpy.zeros(img.shape, dtype='uint8')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (7, 7), 0)
img = cv2.Canny(img, 20, 4)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE,)



cv2.drawContours(new_img, con[0:164], -1, (255, 0, 0), 1)
cv2.drawContours(new_img, con[164:380], -1, (0, 0, 255), 1)
cv2.drawContours(new_img, con[385:-1], -1, (0, 255, 0), 1)

cv2.imshow('result', new_img)
# print(img.shape)

cv2.waitKey(0)




# cap = cv2.VideoCapture('vidio\istockphoto-1480289037-640_adpp_is.mp4')
# cap.set(3, 500)
# cap.set(4, 800)
# while True:
#     success, img = cap.read()
#     kernel = numpy.ones((1, 1), numpy.uint8)
#     img = cv2.Canny(img, 100, 100)
#     img = cv2.dilate(img, kernel, iterations=2)
#     img = cv2.erode(img, kernel, iterations=10)
#
#     cv2.imshow('result', img)
#
#
#     if cv2.waitKey(200) & 0xFF == ord('q'):
#         break