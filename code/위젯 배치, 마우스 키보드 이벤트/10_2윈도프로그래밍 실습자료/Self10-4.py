from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    if event.keycode == 40 :
        messagebox.showinfo("키보드 이벤트", "눌린키 : Shift +" + "아래쪽 화살표")

    elif event.keycode == 39 :
        messagebox.showinfo("키보드 이벤트", "눌린키 : Shift +" + "오른쪽 화살표")

    elif event.keycode == 38 :
        messagebox.showinfo("키보드 이벤트", "눌린키 : Shift+" + "위쪽 화살표")

    elif event.keycode == 37 :
        messagebox.showinfo("키보드 이벤트", "눌린키 : Shift+" + "왼쪽 화살표")
    
    else :
        messagebox.showinfo("키보드 이벤트", "눌린키 : " + chr(event.keycode))

window = Tk()

window.bind("<Key>", keyEvent)

window.mainloop()