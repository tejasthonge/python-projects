'''
Dependancy :pip3 install opencv-python
'''

import cv2

#cofigurable parametors
source = "6-image-resizer\Chart_10MB.jpg"  #wher is image
destenetion = "newImg.png"  #where we want the save genareted image
scale_percent = 50

img = cv2.imread(source, cv2.IMREAD_UNCHANGED)
img2 = cv2.imread("6-image-resizer\BAW.jpeg", cv2.IMREAD_UNCHANGED)

#by which the image is resized
#callcuate the  50 percent of its origanl dimetion
new_weidth = int(img.shape[1] * scale_percent/100)
new_height = int(img.shape[0] * scale_percent/100)

 # Reside image
cv2.imshow("title",img2)   #the imshow method show the image in screen
cv2.waitKey(0)


output = cv2.resize(img,(new_weidth,new_height))
cv2.imwrite(destenetion,output)