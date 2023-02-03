import cv2
import numpy as np

def my_filtering(src, kernel):
    (h, w) = src.shape
    (k_h, k_w) = kernel.shape
    pad_img = my_padding(src, kernel)
    dst = np.zeros((h, w)) #output

    for m in range(h):
        for n in range(w):
            sum = 0
            for k in range(k_h):
                for l in range(k_w):
                    sum += kernel[k, l] * pad_img[m + k, n + l]
             dst[m, n] = sum

    dst = (dst + 0.5).astype(np.uint8)
    return dst

#filter와 image를 입력받아 filtering 수행
def my_filtering(src, filter):
    (h, w) = src.shape
    (m_h, m_w) = filter.shape
    pad_img = my_padding(src, filter)
    dst = np.zeros((h, w))
    for row in range(h):
        for col in range(w):
            dst[row, col] = np.sum(pad_img[row:row + m_h, col:col + m_w] * filter)

    return dst