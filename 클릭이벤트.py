from tkinter import *
from tkinter import messagebox

##함수선언
def clickImage(event):
    messagebox.showinfo("핫도그", "마우스 클릭됨~~~~")

##메인코드
window = Tk()
window.geometry("400x400")

photo = PhotoImage(file = "hotdog.gif")
label1 = Label(window, image = photo)

label1.bind("<Button>", clickImage)

label1.pack(expand = 1, anchor = CENTER)
window.mainloop()