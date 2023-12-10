import os
import sys
import cv2

## vscode에서 열기 했던 폴더 경로가 기준으로 시작된다....
## 이미지 경로를 'cat.bmp'로서 사용하려면 ch02 폴더를 처음부터 열어야 한다.

# 절대경로로 이미지 띄우기 : img = cv2.imread(r'C:\Users\Sam\Documents\ds_study\OPEN_CV\ch02\cat.bmp')
# 절대경로를 직접 불러서 이미지 띄우기 : img_path = str(os.path.dirname(os.path.realpath(__file__))) + '\cat.bmp'
# opencv 폴더를 열고 작업시 : img = cv2.imread('./ch02/cat.bmp', cv2.IMREAD_GRAYSCALE)

img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed!')
    sys.exit()

#cv2.imwrite('cat.png', img)

cv2.namedWindow('image', cv2.WINDOW_NORMAL) # 창크기 마우스로 조정가능
cv2.imshow('image',img)

while cv2.waitKey() != ord('q'): # 특정키 입력해야 종료
    None
    
#cv2.waitKey()

cv2.destroyWindow('image') # 닫을 창의 이름을 지정
cv2.destroyAllWindows() # 띄워진 모든 창 닫기, 작업 종료 시에는 생략해도 무방, 함수/클래스 안에서는 꼭 선언해주자