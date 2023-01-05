import cv2

#read file
img = cv2.imread('saif.jpg',0)# -1 for no change, 1 for color, 0 for gray scale
print(img)

cv2.imshow('image', img)#
k = cv2.waitKey(0) #delay
if k == 27: #press esc to quit
    cv2.destroyAllWindows()
elif k==ord('s'): #save and quit with press of s
    #write file
    cv2.imwrite('saifedited.jpg', img)
    cv2.destroyAllWindows()