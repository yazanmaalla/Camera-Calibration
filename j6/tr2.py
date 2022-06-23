import numpy as np
import cv2 as cv
from glob import glob
from matplotlib import pyplot as plt

#im=cv.imread('j6 (1).jpg')

#ret , corners	=	cv.findChessboardCorners(im, (7,10))
#print (corners.shape) 
#print( corners[0])
#corners=corners.reshape(-1,2)
#print (corners.shape)
#print (corners[0])

#im_left_vis=im.copy()
#cv.drawChessboardCorners(im_left_vis, (7,10), corners, ret) 
#plt.imshow(im_left_vis)
#plt.show()
 
x,y=np.meshgrid(range(7),range(10))
x= 1.75*x
y=1.75*y
#print ("x:\n",x)
#print ("y:\n",y)

world_points=np.hstack((x.reshape(70,1),y.reshape(70,1),np.zeros((70,1)))).astype(np.float32)
#print (world_points)

#print (corners[0],'->',world_points[0])
#print (corners[35],'->',world_points[35])


_3d_points=[]
_2d_points=[]

img_paths=glob('*.jpg') #get paths of all all images
for path in img_paths:
    im=cv.imread(path)
    ret, corners = cv.findChessboardCorners(im, (7,10))
    
    if ret: #add points only if checkerboard was correctly detected:
        _2d_points.append(corners) #append current 2D points
        _3d_points.append(world_points) #3D points are always the same


ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(_3d_points, _2d_points, (im.shape[1],im.shape[0]),None ,None)
#print ("Ret:",ret)
print ("Mtx:",mtx," ---------------> [",mtx.shape,"]")
print ("Dist:",dist," ----------> [",dist.shape,"]")
#print ("rvecs:",rvecs," -----------------> [",rvecs[0].shape,"]")
#print ("tvecs:",tvecs," ---------------------> [",tvecs[0].shape,"]")



cv.waitKey(0)
cv.destroyAllWindows()
 