# this is a project based on detection of rust iron portion
# you need to pass an argument stating the file name of the image.
# for simplicity keep the script and image in the same folder

import cv2
from sys import argv
import numpy as np
import os
import glob

count = 0

def rust_detect(file):
	A = cv2.imread(file)
	img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	
	# Range for lower red
	lower_red = np.array([0,70,70])
	upper_red = np.array([20,200,150])
	mask0 = cv2.inRange(img_hsv, lower_red, upper_red)
	
	# range for upper red
	lower_red = np.array([170,70,70])
	upper_red = np.array([180,200,150])
	mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
	
	# add both masks
	mask = mask0+mask1
	
	output_img = cv2.bitwise_and(img,img,mask=mask)
	
	gry = cv2.cvtColor(output_img,cv2.COLOR_BGR2GRAY)
	_,gry = cv2.threshold(gry,10,255,cv2.THRESH_BINARY)
	
	print("\n\n\n Number of pixels depicting rust \n >> %d"%(np.sum(gry)/255))
	cv2.imshow('image1',output_img)
	cv2.imshow('image2',img)
	cv2.waitKey(0)
	cv2.imwrite('output_image%d.jpg'%count,output_img)
	cv2.imwrite('image%d.jpg'%count,img)
	cv2.destroyAllWindows()
	os.system("cls")
	
	
	
os.system("color 0a")
os.system("cls")

print(""" Welcome to the rust detection software!! 
 The software detects the rusted portion of metal
 and calculates nuber of rust piels for 
 comparitive analysis.\n\n""")
print("**********************************************")

images = glob.glob("Images/*.jpg")

for path in images:
	count+=1
	rust_detect(path)

input("\n PRESS ENTER TO EXIT ")
