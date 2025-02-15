from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480")
root.resizable(True, True)

def create_open():
    pass
def create_save():
    pass


menu = Menu(root)

menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="열기", command=create_open)
menu_file.add_command(label="저장", command=create_save)
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

root.config(menu=menu)
root.mainloop()