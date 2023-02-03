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

if __name__ == '__main__':
    src = np.array([[0, 0, 0, 0, 0],
                   [15, 16, 0, 0, 0],
                   [10, 11, 12, 13, 14],
                   [5, 6, 7, 8, 9],
                   [0, 1, 2, 3, 4]], dtype=np.uint8)

    kernel = np.ones((3, 3), np.float32)/9

    dst = my_filtering(src, kernel)

    print("Input:\n {}".format(src))
    print("Output:\n {}".format(dst))