from tkinter import *
from tkinter.filedialog import *  # 파일 입출력을 위한 모듈
from tkinter.simpledialog import *  # 숫자나 문자를 입력 받기 위한 모듈
from wand.image import *

# 전역 함수 부
window, canvas, paper = None, None, None
photo, photoClone = None, None
oriX, oriY = 0, 0


# 함수 정의 부
def displayImage(img, width, height):  # 캔버스 디스플레이 함수
    global window, canvas, paper, photo, photoClone, oriX, oriY
    if canvas != None:
        canvas.destroy()
    canvas = Canvas(window, width=width, height=height, bg="black", bd=0, highlightthickness=0)
    paper = PhotoImage(width=width, height=height)
    canvas.create_image((width / 2, height / 2), image=paper, state="normal")
    blob = img.make_blob(format="RGB")
    for i in range(0, width):
        for j in range(0, height):
            R = blob[(i * 3 * width) + (j * 3) + 0]
            G = blob[(i * 3 * width) + (j * 3) + 1]
            B = blob[(i * 3 * width) + (j * 3) + 2]
            paper.put("#%02x%02x%02x" % (R, G, B), (j, i))
    canvas.place(x=150, y=250)


def func_open():  # 파일 열기 함수
    global window, canvas, paper, photo, photoClone, oriX, oriY
    openFile = askopenfilename(parent=window,
                               filetypes=(("* Image file", "*.jpg;*.jpeng;*.bmp;*.png;*.tif;*.gif"), ("* File", "*.*")))
    photo = Image(filename=openFile)
    oriX = photo.width
    oriY = photo.height
    photoClone = photo.clone()
    newX = photo.width
    newY = photo.height
    displayImage(photoClone, newX, newY)


def func_save():  # 파일 저장 함수
    global window, canvas, paper, photo, photoClone, oriX, oriY

    if photoClone == None:
        return
    saveFile = asksaveasfile(parent=window, mode="w", defaultextension=".jpg",
                             filetypes=(("JPG File", "*.jpg;*.jpeg"), ("* File", "*.*")))
    savePhoto = photoClone.convert("jpg")
    savePhoto.save(filename=saveFile.name)


def func_exit():  # 종료 함수
    window.quit()
    window.destroy()


def func_zoomIn():  # 이미지 확대 함수
    global window, canvas, paper, photo, photoClone, oriX, oriY
    if canvas == None:
        return
    zoom = askinteger("확대", "확대할 배수 입력(2~4)", minvalue=2, maxvalue=4)
    photoClone.resize(int(oriX * zoom), int(oriY * zoom))
    newX = photoClone.width
    newY = photoClone.height
    displayImage(photoClone, newX, newY)


def func_zoomOut():  # 이미지 축소 함수
    global window, canvas, paper, photo, photoClone, oriX, oriY
    if canvas == None:
        return
    zoom = askinteger("축소", "축소할 배수 입력(2~4)", minvalue=2, maxvalue=4)
    photoClone.resize(int(oriX / zoom), int(oriY / zoom))
    newX = photoClone.width
    newY = photoClone.height
    displayImage(photoClone, newX, newY)


def func_mirror1():  # 이미지 좌우 반전 함수
    global window, canvas, paper, photo, photoClone, oriX, oriY
    if canvas == None:
        return
    photoClone.flip()
    newX = photoClone.width
    newY = photoClone.height
    displayImage(photoClone, newX, newY)


def func_mirror2():  # 이미지 상하 반전 함수
    global window, canvas, paper, photo, photoClone, oriX, oriY
    if canvas == None:
        return
    photoClone.flop()
    newX = photoClone.width
    newY = photoClone.height
    displayImage(photoClone, newX, newY)


def func_rotate():  # 이미지 회전 함수
    global window, canvas, paper, photo, photoClone, oriX, oriY
    if canvas == None:
        return
    degree = askinteger("회전", "각도 입력(0~360)", minvalue=0, maxvalue=360)
    photoClone.rotate(degree)
    newX = photoClone.width
    newY = photoClone.height
    displayImage(photoClone, newX, newY)


def func_bright():  # 이미지 밝기 조절 함수
    global window, canvas, paper, photo, photoClone, oriX, oriY
    if canvas == None:
        return
    value = askinteger("밝기 + ", "밝기 입력(100~200)", minvalue=100, maxvalue=200)
    photoClone.modulate(value, 100, 100)
    newX = photoClone.width
    newY = photoClone.height
    displayImage(photoClone, newX, newY)


def func_clear():  # 이미지 선명도 함수
    global window, canvas, paper, photo, photoClone, oriX, oriY
    if canvas == None:
        return
    value = askinteger("선명도 + ", "선명도 입력(100~200)", minvalue=100, maxvalue=200)
    photoClone.modulate(100, value, 100)
    newX = photoClone.width
    newY = photoClone.height
    displayImage(photoClone, newX, newY)


def func_dark():  # 이미지 밝기 조절 함수
    global window, canvas, paper, photo, photoClone, oriX, oriY
    if canvas == None:
        return
    value = askinteger("밝기 - ", "밝기 입력(0~100)", minvalue=0, maxvalue=100)
    photoClone.modulate(value, 100, 100)
    newX = photoClone.width
    newY = photoClone.height
    displayImage(photoClone, newX, newY)


def func_unclear():  # 이미지 선명도 함수
    global window, canvas, paper, photo, photoClone, oriX, oriY
    if canvas == None:
        return
    value = askinteger("선명도 - ", "선명도 입력(0~100)", minvalue=0, maxvalue=100)
    photoClone.modulate(100, value, 100)
    newX = photoClone.width
    newY = photoClone.height
    displayImage(photoClone, newX, newY)


def func_bw():  # 이미지 흑백 함수
    global window, canvas, paper, photo, photoClone, oriX, oriY
    if canvas == None:
        return
    photoClone.type = "grayscale"
    newX = photoClone.width
    newY = photoClone.height
    displayImage(photoClone, newX, newY)


# 메인 코드 부
window = Tk()
window.geometry("815x680")
window.resizable(width=0, height=0)
window.title("Photo Shop  ver.1")
mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="열기", command=func_open)
fileMenu.add_command(label="저장", command=func_save)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)

image1Menu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="Image Processing(1)", menu=image1Menu)
image1Menu.add_command(label="확대", command=func_zoomIn)
image1Menu.add_command(label="축소", command=func_zoomOut)
image1Menu.add_separator()
image1Menu.add_command(label="상하 반전", command=func_mirror1)
image1Menu.add_command(label="좌우 반전", command=func_mirror2)
image1Menu.add_command(label="회전", command=func_rotate)

image2Menu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="Image Processing(2)", menu=image2Menu)
image2Menu.add_command(label="밝기 +", command=func_bright)
image2Menu.add_command(label="밝기 -", command=func_dark)
image2Menu.add_separator()
image2Menu.add_command(label="선명도 +", command=func_clear)
image2Menu.add_command(label="선명도 -", command=func_unclear)
image2Menu.add_separator()
image2Menu.add_command(label="흑백", command=func_bw)

bgPhoto = PhotoImage(file="imgs/당근2.jpeg")
bg = Label(window, image=bgPhoto)
bg.place(x=-2, y=-2)
window.mainloop()