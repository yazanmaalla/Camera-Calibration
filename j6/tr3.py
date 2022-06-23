
import numpy as np
import cv2 as cv
from glob import glob
from matplotlib import pyplot as plt


im_undistorted=cv.undistort(im, mtx, dist)
plt.subplot(121)
plt.imshow(im)
plt.subplot(122)
plt.imshow(im_undistorted)
plt.show()


mtx = [[668.39932471,  0.  , 415.39552918],[  0.,  668.89129305 , 315.51394373] , [ 0. ,  0. ,1. ]]

dist= [[ 3.90733780e-01 ,-2.05823806e+00, -6.56241185e-05 , 3.17232551e-03 , 3.43659802e+00]]
img_paths=glob('*.jpg') #get paths of all all images
for path in img_paths:
    im=cv.imread(path)
   im_undistorted=cv.undistort(im, mtx, dist)
   plt.subplot(121)
    plt.imshow(im)
   plt.subplot(122)
   plt.imshow(im_undistorted)
    plt.show()
    cv.waitKey(0)




cv.waitKey(0)
cv.destroyAllWindows()
