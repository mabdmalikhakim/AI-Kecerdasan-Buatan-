import cv2
import glob
import numpy as np

imdir = r'E:\=====KULIAH=====\Semester 5\Kecerdasan Buatan E\Tugas Besar\Foto\Dataset\Daun_Belimbing_Wuluh\\'
ext = ['jpg']

files = []
[files.extend(glob.glob(imdir + '*.jpg'))]

images = [cv2.imread(file)for file in files]

i = 1
for image in images:
    im_edge = cv2.Canny(image,100,200)
    if i<10:
        im_name = r'E:\=====KULIAH=====\Semester 5\Kecerdasan Buatan E\Tugas Besar\Foto\Dataset\Daun_Belimbing_Wuluh_edge\00'+ str(i) + '.jpg'
    else : 
        im_name = r'E:\=====KULIAH=====\Semester 5\Kecerdasan Buatan E\Tugas Besar\Foto\Dataset\Daun_Belimbing_Wuluh_edge\00'+ str(i) + '.jpg'
    cv2.imwrite(im_name,im_edge)

    i+=1

# imdir = 'Dataset\jeruk nipis\\'

# files = []
# [files.extend(glob.glob(imdir + '*.jpg'))]

# images = [cv2.imread(file)for file in files]

# i = 1
# for image in images:
#     im_edge = cv2.Canny(image,100,200)
#     if i<10:
#         im_name = r'E:\=====KULIAH=====\Semester 5\Kecerdasan Buatan E\Tugas Besar\Foto\Dataset\jeruk_nipis_edge\00'+ str(i) + '.jpg'
#     else : 
#         im_name = r'E:\=====KULIAH=====\Semester 5\Kecerdasan Buatan E\Tugas Besar\Foto\Dataset\jeruk_nipis_edge\0'+ str(i) + '.jpg'
#     print(images)

#     i+=1



