import cv2

if __name__ == '__main__':
    src = cv2.imread('imgs/threshold_test.png', cv2.IMREAD_GRAYSCALE)

    ret, dst = cv2.threshold(src, 150, 255, cv2.THRESH_BINARY)
    print('ret: ', ret)

    cv2.imshow('original', src)
    cv2.imshow('threshold', dst)

    cv2.waitKey()
    cv2.destroyAllWindows()