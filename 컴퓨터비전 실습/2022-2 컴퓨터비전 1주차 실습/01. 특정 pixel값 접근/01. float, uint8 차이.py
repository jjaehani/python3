 import cv2
import numpy as np

img01 = np.zeros((200, 20)) ## 200x200 크기의 0으로 채워진 이미지를 생성
img02 = np.ones((20, 20)) ## 200x200 크기의 1으로 채워진 이미지를 생성

img03 = np.zeros((20, 20), dtype=np.uint8) ## 200x200 크기의 0으로 채워진 이미지를 생성
img04 = np.ones((20, 20), dtype=np.uint8) ## 200x200 크기의 1으로 채워진 이미지를 생성
img05 = np.full((20, 20), 255, dtype=np.uint8) ## 200x200 크기의 255으로 채워진 이미지를 생성

print(img01.dtype)
print(img03.dtype)

cv2.imshow("img01", img01)
cv2.imshow("img02", img02)
cv2.imshow("img03", img03)
cv2.imshow("img04", img04)
cv2.imshow("img05", img05)

cv2.waitKey() ## cv2 윈도우를 대기
cv2.destroyAllWindows() ## 모든 윈도우를 종료