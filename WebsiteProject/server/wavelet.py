import numpy as np
import pywt
import cv2


def w2d(img, mode='haar', level=1):
    im_array = img

    # Datatype conversions
    # convert to grayscale

    im_array = cv2.cvtColor(im_array, cv2.COLOR_RGB2GRAY)

    # convert to float

    im_array = np.float32(im_array)
    im_array /= 255

    # compute coefficients
    coeffs = pywt.wavedec2(im_array, mode, level=level)

    # Process Coefficients

    coeffs_h = list(coeffs)
    coeffs_h[0] *= 0

    # reconstruction
    im_array_h = pywt.waverec2(coeffs_h, mode)
    im_array_h *= 255
    im_array_h = np.uint8(im_array_h)

    return im_array_h