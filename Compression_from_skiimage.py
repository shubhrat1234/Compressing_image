from skimage.io import imread, imshow
from skimage.transform import rescale, resize, downscale_local_mean
from skimage.io import imsave
import matplotlib.pyplot as plt
import os
import numpy as np

img = imread('original.jpg')
target_size = 40000
size = os.path.getsize('original.jpg')
factor = 0.9
while(size>=40000):
    image_rescaled = rescale(img, factor, anti_aliasing=False)
    imsave('new.jpg', image_rescaled)
    print('factor {} image of size {}'.format(factor,size))
    factor = factor - 0.05
    size = os.path.getsize('new.jpg')

end_size = os.path.getsize('new.jpg')
print(end_size)
