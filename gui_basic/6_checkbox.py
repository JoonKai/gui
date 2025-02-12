from tkinter import *

root = Tk()
root.title("EPI Program")
root.geometry("640x340")

chkvar = IntVar() #chkvar 에 int 형으로 값을 저장한다.
checkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# checkbox.select() # 자동 선택 처리
# checkbox.deselect() #자동 해제 처리
checkbox.pack()


chkvar2 = IntVar()
checkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
checkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0 : 체크 해제, 1: 체크
    print(chkvar2.get()) # 0 : 체크 해제, 1: 체크

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()