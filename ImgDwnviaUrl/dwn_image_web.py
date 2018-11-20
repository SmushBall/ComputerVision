# Author : Deepak Kumar Singh
# Date: 09/Aug/2018
# This program downloads images from thr web using python module urllib

from urllib.request import Request, urlopen
import cv2
import numpy as np
import os

def store_raw_images():
    neg_images_link = Request ('https://www.pexels.com/search/watches/', headers={'User-Agent': 'Mozilla/5.0'})
    neg_image_urls = urlopen(neg_images_link).read().decode()
    print(neg_image_urls)
    pic_num = 1
    
    if not os.path.exists('neg_img'):
        os.makedirs('neg_img')
        print("Making directory")
        
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1

            print("success")
            
        except Exception as e:
            print(str(e))  



store_raw_images()
