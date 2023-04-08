#import
import cv2
import numpy as np

#path
path = r'D:\TGMT\test.png'

img_in = cv2.imread(path)

#tinh toan 10 lan
for i in range(1):
    #tinh gradient theo Gx
    for i in range(0, m-1):
        for j in range(0, n-2):
            Gx[i, j] = img_in[i, j+1] - img_in[i, j]
    
    #tinh gradient theo Gy
    for i in range(0, m-2):
        for j in range(0, n-1):
            Gy[i, j] = img_in[i+1, j] - img_in[i, j]
    
    #tinh nang luong E
    E = abs(Gx) + abs(Gy)
    
    #tinh M(i, j) copy hang dau cua E qua M
    M[0] = E[0]
    
    for i in range(1, m):
        M[i, 0] = E[i, 0] + min(M[i-1, 0], M[i-1, 1])
    for i in range(1, n-1):
        M[i, j] = E[i, j] + min(M[i-1, j-1], M[i-1, j], M[i-1, j], M[i-1, j+1])
        
    M[i, n-1] = E[i, n-1] + min(M[i-1, n-2], M[i-1, n-1])
    
    #Xet chon ra phan tu cot co gia tri nho nhat
    j = np.agrmin[n-1, j]
    seam[n-1] = j
    
    #xoa seam
    for i in range(0, m):
        img_out = np.zeros(m, n-1)
        for i in range(0, m):
            for i in range(0, seam[i]):
                img_out[i, j] = img_in[i, j]
                for j in range(seam[i]+1, n):
                    img_out[i, j-1] = img_in[i, j]
    img_in = img_out
    
#in anh dau vao
cv2.imshow('image', img_in)
#in anh nang luong E
cv2.imshow('image', E)
#in seam

#in anh sau khi xoa seam
cv2.imshow('cut seam', img_out)

#waiting
cv2.waitKey(5000)