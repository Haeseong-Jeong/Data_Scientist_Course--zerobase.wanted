﻿import numpy as np
import cv2


# 부분 영상 추출
img1 = cv2.imread('HappyFish.jpg')

img2 = img1[40:120, 30:150]  # numpy.ndarray의 슬라이싱
img3 = img1[40:120, 30:150].copy()

img2.fill(0)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()

# 부분 영상 처리
img = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

img_face = img[200:400, 200:400]  # 얼굴 영역
cv2.add(img_face, 50, img_face)   # 밝기 조절

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
