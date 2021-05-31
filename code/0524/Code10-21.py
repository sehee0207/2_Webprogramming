from tkinter import *
from tkinter.filedialog import *

## 함수 정의 부분 ##
window = Tk()
window.geometry("400x100")

label1 = Label(window, text = "선택된 파일 이름 ")
label1.pack()

filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
label1.configure(text = str(filename))

saveFp = asksavesasfile(parent = window, mode = "w", defaultextension = ".jpg", filetypes = (("JPG 파일", "*.jpg;*.jpeg"), ("모든 파일", "*.*")))
label1.configure(text = saveFp)
saveFp.close()

# 모드 w = 쓰기 모드
# saveFp 는 자체를 text 에 대입 시켜 출

window.mainloop()

