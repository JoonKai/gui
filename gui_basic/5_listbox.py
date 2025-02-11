from tkinter import *

root = Tk()
root.title("EPI Program")
root.geometry("640x340")

listbox = Listbox(root, selectmode="extended", height=0) #리스트 박스 여러게 선택 single은 한개 선택택
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    #삭제제
    # listbox.delete(0)
    #갯수확인
    # print("리스트에는", listbox.size(), "개가 있어요")
    #항목확인 (시작 idx , 끝 idx)
    # print("1번째부터 3번째가지의 항목 : ", listbox.get(0, 2))

    #선택한 항목 확인(위치 인덱스 값으로 반환)
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()