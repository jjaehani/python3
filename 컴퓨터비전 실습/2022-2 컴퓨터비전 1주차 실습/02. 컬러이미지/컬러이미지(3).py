import cv2
import numpy as np

src = np.zeros((300,300, 3), dtype=np.uint8)
# b = 255 g, r = 0
src[0:100, 0:100, 0] = 255
# g = 255 b, r = 0
src[0:100, 100:200, 1] = 255
# r = 255 b, g =0
src[0:100, 200:300, 2] = 255

# b + r
src[100:200, 0:100, 0] = 255
src[100:200, 0:100, 2] = 255
# b + g
src[100:200, 100:200, 0] = 255
src[100:200, 100:200, 1] = 255
# g + r
src[100:200, 200:300, 1] = 255
src[100:200, 200:300, 2] = 255

# b + g + r
src[200:, :100, 0] = 255
src[200:, :100, 1] = 255
src[200:300, 0:100, 2] = 255

# b/2 + g/2 + r/2
src[200:, 100:200, 0] = 128
src[200:, 100:200, 1] = 128
src[200:300, 100:200, 2] = 128

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()


print(src.shape)
print(src[0,0,0], src[0,0,1], src[0,0,2])
print(src[0,0])
print(src[0])
print(src)

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()