from tkinter import *
from tkinter.filedialog import *

fnameList = ["pie.gif"]
photoList = [None]
num = 0


## 함수 선언 부분 ##
def func_open() :
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo
    fnameList.append(filename)

def func_exit() :
    window.quit()
    window.destroy()

def clickNext() :
    global num
    num += 1
    if num > len(fnameList) -1 :
        num = 0
    photo = PhotoImage(file = fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    
def clickPrev() :
    global num
    num -= 1
    if num < 0 :
        num = len(fnameList) -1
    photo = PhotoImage(file = fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    

## 메인 코드  부분 ##
window = Tk()
window.geometry("400x400")
window.title("그림 넘겨보기")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand=1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command = func_exit)

btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)

photo = PhotoImage(file = "gif/" + fnameList[0])

btnPrev.place(x = 100, y = 350)
btnNext.place(x = 250, y = 350)

window.mainloop()
