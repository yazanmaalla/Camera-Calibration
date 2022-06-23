import numpy as np
import cv2 as cv
import glob

images = [cv2.imread(file) for file in glob.glob('*.png')]

cv.imshow('kk',image)