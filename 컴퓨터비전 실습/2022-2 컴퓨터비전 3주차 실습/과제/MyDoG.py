import cv2
import numpy as np

def my_padding(src, filter):
    (h, w) = src.shape
    (h_pad, w_pad) = filter.shape
    h_pad = h_pad // 2
    w_pad = w_pad // 2
    padding_img = np.zeros((h+h_pad*2, w+w_pad*2))
    padding_img[h_pad:h+h_pad, w_pad:w+w_pad] = src
    return padding_img

# filter와 image를 입력받아 filtering수행
def my_filtering(src, filter):
    (h, w) = src.shape
    (m_h, m_w) = filter.shape
    pad_img = my_padding(src, filter)
    dst = np.zeros((h, w))
    for row in range(h):
        for col in range(w):
            dst[row, col] = np.sum(pad_img[row:row + m_h, col:col + m_w] * filter)
    return dst

def get_DoG_filter(fsize, sigma=1):
    y, x = np.mgrid[-(fsize//2):(fsize//2) + 1, -(fsize//2):(fsize//2)+1]

    DoG_x = (-x / sigma**2) * np.exp(-((x**2 + y**2) / (2*sigma**2)))
    DoG_y = (-y / sigma**2) * np.exp(-((x**2 + y**2) / (2*sigma**2)))

    return DoG_x, DoG_y


if __name__ == '__main__':
    src = cv2.imread("imgs/당근2.jpeg", cv2.IMREAD_GRAYSCALE)

    DoG_x, DoG_y = get_DoG_filter(fsize=3, sigma=1)
    dst_x = my_filtering(src, DoG_x)
    dst_y = my_filtering(src, DoG_y)

    dst = np.sqrt(dst_x**2 + dst_y**2)

    DoG_x_filter, DoG_y_filter = get_DoG_filter(fsize=256, sigma=30)
    DoG_x_ = ((DoG_x_filter - np.min(DoG_x_filter)) / np.max(DoG_x_filter - np.min(DoG_x_filter)) * 255).astype(np.uint8)
    DoG_y_ = ((DoG_y_filter - np.min(DoG_y_filter)) / np.max(DoG_y_filter - np.min(DoG_y_filter)) * 255).astype(
        np.uint8)

    cv2.imshow('dst_x', dst_x/255)
    cv2.imshow('dst_y', dst_y/255)
    cv2.imshow('dst', dst/255)

    cv2.imshow('DoG_x', DoG_x_)
    cv2.imshow('DoG_y', DoG_y_)
    cv2.waitKey()
    cv2.destroyAllWindows()