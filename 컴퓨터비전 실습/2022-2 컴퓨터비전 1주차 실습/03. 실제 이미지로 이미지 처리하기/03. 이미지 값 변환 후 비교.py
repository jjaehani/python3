import cv2
import numpy as np

def point_processing(src, type='original'):
    dst = np.zeros(src.shape, dtype=np.uint8)

    if type=='original':
        dst = src.copy()

    elif type=='darken':
        for channel in range(3):
            dst[:,:,channel] = cv2.subtract(src[:,:,channel], 128)

    elif type=='lower contrast':
        calc = np.full((dst.shape),2, dtype=np.uint8)
        dst = cv2.divide(src, calc)

    elif type=='non_linear_lower_contrast':
        for channel in range(3):
            x = src[:,:,channel]
            print(x)
            dst[:, :, channel] = ((x/255) ** (1/3) * 255).astype(np.uint8)

    elif type=='invert':
        pass
    elif type=='lighten':
        pass
    elif type=='raise_contrast':
        pass
    elif type=='non_linear_raise_contrast':
        pass

    return dst

if __name__ == '__main__':
    src = cv2.imreaed('../imgs/baby.jpg')
    dst = point_processing(src, 'darken')
    cv2.imshow('original', src)
    cv2.imshow('point processing', dst)
    cv2.imwrite('./results/darken.png', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()