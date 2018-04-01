import numpy as np
#import matplotlib.pyplot as plt
from scipy.misc import imfilter, imread
from skimage import color, data, restoration
from scipy.signal import convolve2d as conv2

def main():
  image = imread("/Users/gsamaras/Downloads/boat.tif")
  #plt.imshow(arr, cmap='gray')
  #plt.show()
  #blurred_arr = imfilter(arr, "blur")
  psf = np.ones((5, 5)) / 25
  image = conv2(image, psf, 'same')
  image += 0.1 * image.std() * np.random.standard_normal(image.shape)

  deconvolved = restoration.wiener(image, psf, 1, clip=False)
  #print deconvolved
  plt.imshow(deconvolved, cmap='gray')
  plt.show()
  #print image

if __name__ == "__main__":
    main()
