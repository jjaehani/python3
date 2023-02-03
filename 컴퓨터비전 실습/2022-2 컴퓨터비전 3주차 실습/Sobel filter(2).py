import cv2
import numpy as np

def get_my_sobel():
    sobel_x = np.dot(np.array([[1], [2], [1]]), np.array([[-1, 0, 1]]))
    sobel_y = np.dot(np.array([[-1], [0], [1]]), np.array([[1, 2, 1]]))
    return sobel_x, sobel_y

if __name__ == '__main__':
    src = cv2.imread('imgs/edge_detection_img.png', cv2.IMREAD_GRAYSCALE)
    sobel_x, sobel_y = get_my_sobel()
    dst_x = my_filtering(src, sobel_x)
    dst_y = my_filtering(src, sobel_y)
    dst = np.hypot(dst_x, dst_y) #dst = np.sqrt(dst_x**2 + dst_y**2)

    #0 ~ 1 사이의 값으로 변경 후 0 ~ 255로 변경
    dst_x_Norm = ((dst_x - np.min(dst_x) )/np.max(dst_x - np.min(dst_x)) * 255 + 0.5).astype(np.uint8)
    dst_y_Norm = ((dst_y - np.min(dst_y) )/np.max(dst_y - np.min(dst_y)) * 255 + 0.5).astype(np.uint8)

    # 참고: 실수로 표현하는 경우 0 이하의 값은 전부 검은색, 1 이상의 값은 전부 흰색으로 나옴
    cv2.imshow('original', src)
    cv2.imshow('dst_x_Norm', dst_x_Norm)
    cv2.imshow('dst_y_Norm', dst_y_Norm)
    cv2.imshow('sobel', (dst+0.5).astype(np.uint8))

    cv2.waitKey()
    cv2.destroyAllWindows()

    sobX = cv2.Sobel(src, cv2.CV_64F, 1, 0, ksize=3)
    sobY = cv2.Sobel(src, cv2.CV_64F, 0, 1, ksize=3)
    cv2.imshow('sobX', sobX/255)
    cv2.imshow('sobY', sobY/255)