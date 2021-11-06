import cv2
import glob
import numpy as np

# imdir = r'E:\=====KULIAH=====\Semester 5\Kecerdasan Buatan E\Tugas Besar\Foto\Dataset\Daun_Belimbing_Wuluh\\'
# ext = ['jpg']

# files = []
# [files.extend(glob.glob(imdir + '*.jpg'))]

# images = [cv2.imread(file)for file in files]

# i = 1
# for image in images:
#     im_adj = cv2.addWeighted(image, 1.5, np.zeros(image.shape, image.dtype), 0, -100)
#     if i<10:
#         im_name = r'E:\=====KULIAH=====\Semester 5\Kecerdasan Buatan E\Tugas Besar\Foto\Dataset\Daun_Belimbing_Wuluh_contras\00'+ str(i) + '.jpg'
#     else : 
#         im_name = r'E:\=====KULIAH=====\Semester 5\Kecerdasan Buatan E\Tugas Besar\Foto\Dataset\Daun_Belimbing_Wuluh_contras\0'+ str(i) + '.jpg'
#     cv2.imwrite(im_name,im_adj)

#     i+=1

imdir = r'E:\=====KULIAH=====\Semester 5\Kecerdasan Buatan E\Tugas Besar\Foto\Dataset\jeruk nipis\\'
ext = ['jpg']

files = []
[files.extend(glob.glob(imdir + '*.jpg'))]

images = [cv2.imread(file)for file in files]

i = 1
for image in images:
    im_adj = cv2.addWeighted(image, 1.5, np.zeros(image.shape, image.dtype), 0, -100)
    if i<10:
        im_name = r'E:\=====KULIAH=====\Semester 5\Kecerdasan Buatan E\Tugas Besar\Foto\Dataset\jeruk_nipis_contras\00'+ str(i) + '.jpg'
    else : 
        im_name = r'E:\=====KULIAH=====\Semester 5\Kecerdasan Buatan E\Tugas Besar\Foto\Dataset\jeruk_nipis_contras\0'+ str(i) + '.jpg'
    cv2.imwrite(im_name,im_adj)

    i+=1