#Nguyen Thanh Nghia
#B1709551
#
#import
import cv2 as cv
import cv2
import numpy as np
import matplotlib.pyplot as plt

#doc anh
filename = 'iguana.png'
img_in = cv2.imread(filename)
#lam xam anh(neu anh dau vao la anh mau)
img_in_gray = cv.cvtColor(img_in, cv.COLOR_BGR2GRAY)
R = np.zeros(img_in_gray.shape) 

#1. tinh gradient cac ham Ix, Iy,
Ix =cv2.Sobel(img_in_gray, cv2.CV_64F, 1, 0, ksize = 3)
Iy =cv2.Sobel(img_in_gray, cv2.CV_64F, 0, 1, ksize = 3)

#2. Tinh gradient + Gausse cho Ix^2, Iy^2, IxIy
Ix_2 = cv2.GaussianBlur(np.multiply(Ix, Ix),(3,3),1) 
Iy_2 = cv2.GaussianBlur(np.multiply(Iy, Iy),(3,3),1)
IxIy = cv2.GaussianBlur(np.multiply(Ix, Iy),(3,3),1)

#3. Tinh Gausse cho Ix^2, Iy^2, IxIy

#4. Tinh M trace k = alpha(0.04~0.06)
k = 0.05
R = np.multiply(Ix_2,Iy_2)-np.square(IxIy)-k*np.square(Ix_2+Iy_2)

#img_in_gray = np.float32(img_in_gray)
#dst = cv.cornerHarris(img_in_gray,2,3,0.04)

#dst = cv.dilate(dst,None)

#img_in[dst>0.01*dst.max()]=[0,0,255]


#5. Phan nguong va non-maximum processor
corner_count = 0
max_Value = 0.005*R.max()
for row_n,row in enumerate(R):
    for col_n,col in enumerate(row):
        if col > max_Value:
            corner_count += 1
            img_in[row_n,col_n] = [0,255,255] 
        else: 
            pass

#hien thi anh
cv2.imshow('Haris corner', img_in)

#waiting
cv2.waitKey(5000)