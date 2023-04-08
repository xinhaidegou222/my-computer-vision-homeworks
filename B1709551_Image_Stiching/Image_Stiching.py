import cv2
image_paths=['21.png','22.png']
#path cho hinh anh dau vao
imgs = []
 
for i in range(len(image_paths)):
    imgs.append(cv2.imread(image_paths[i]))
    imgs[i]=cv2.resize(imgs[i],(0,0),fx=0.4,fy=0.4)
    #ham nay de kiem tra nhung hinh anh co kich thuoc qua to 
    #vi du sreen 1080- dua anh lon hon vao thi k the hien thi
#show ra nhung hinh anh dau vao
cv2.imshow('Anh dau vao 1',imgs[0])
cv2.imshow('Anh dau vao 2',imgs[1])


stitchy=cv2.Stitcher.create()
(dummy,output)=stitchy.stitch(imgs)
 
if dummy != cv2.STITCHER_OK:
    #kiem tra neu stitching thanh cong thi in ra thanh cong
    #hoac nguoc lai
    print('Stitching that bai!')
else:
    print('Stitching thanh cong!')
 
# final output
cv2.imshow('Ket qua',output)
 
cv2.waitKey(10000)