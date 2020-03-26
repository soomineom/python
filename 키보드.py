from tkinter import *
from tkinter import messagebox

#함수 선언
def keyEvent(event):
    messagebox.showinfo("키보드이벤트", "눌린키 : "+chr(event.keycode))

#메인코드
window = Tk()
window.geometry("400x200")

label1 = Label(window, text = "키보드 누르세요", font = 30, bg = "white", anchor = CENTER)
label1.pack()

window.bind("<Key>", keyEvent)

window.mainloop()