from tkinter import *
from time import *

fnameList = ["hotdog.gif", "puppy.gif", "sundog.gif", "superdog.gif",
             "swingdog.gif", "tenor.gif", "doggun.gif", "bathdog.gif",
             "flyingdof.gif"]
photoList = [None] * 9
#Photoimage()함수로 생성할 변수9개 준비
num = 0 #현재 사진번호

##함수선언
def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

def clickPrev():
    global num
    num -=1
    if num < 0:
        num = 8
    photo = PhotoImage(fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo


#메인코드
window = Tk()
window.geometry("800x600")
window.title("사진 앨범")

btnPrev = Button(window, text = "<<이전", command = clickPrev)
btnNext = Button(window, text = "다음>>", command = clickNext)

photo = PhotoImage(file = fnameList[0])
pLabel = Label(window, image = photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x = 15, y = 50)

window.mainloop()

