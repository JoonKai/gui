import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgbox
from PIL import Image

root = Tk()
root.title("EPI Program")
root.geometry()

# 파일 추가
def add_file():
    files=filedialog.askopenfilenames(title="이미지 파일을 선택하세요", filetypes=(("PNG 파일", "*.png"),("모든 파일","*")), initialdir=r"C:\Users\seok\Desktop\python_project\gui\gui_basic") #최초의 c드라이버를 보여줌
    for file in files:
        list_file.insert(END, files)
# 선택 삭제
def del_file():
    # print(list_file.curselection())
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected is None:
        return
    # print(folder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)
    
# 이미지 통합
def merge_image():
    # print(list_file.get(0, END)) #모든 파일 목록을 가져옴
    images = [Image.open(x) for x in list_file.get(0, END)]
    # size -> size[0] : width , size[1] : height

    widths = [x.size[0] for x in images]
    heights = [x.size[1] for x in images]

    print("width : ", widths)
    print("height : ", heights)

# 시작
def start():
    # 각 옵션들 값을 확인
    print("가로넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포맷 : ", cmb_format.get())

    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가 하세요")
        return 

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택 하세요")
        return 
    
    merge_image()
    



# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame,padx=5, pady=5, width=12, text="파일 추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame,padx=5, pady=5, width=12, text="선택삭제", command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

#저장 경로 프레임
path_frame= LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path= Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True,padx=5, pady=5, ipady=4) #높이 변경

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right",padx=5, pady=5)

#옵션 프레임
#가로 넓이 레이블
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(fill="x", padx=5, pady=5, ipady=5)

#1. 가로 넓이 옵션
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left",padx=5, pady=5)

#가로 넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left",padx=5, pady=5)

#2. 간격 옵션
#간격 옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left",padx=5, pady=5)

#간격 옵션 콤보
opt_space = ["없음", "좁게", "보통넓이", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left",padx=5, pady=5)

#3. 파일 포맷 옵션
#파일 포맷 옵션 레이블
lbl_format = Label(frame_option, text="간격", width=8)
lbl_format.pack(side="left",padx=5, pady=5)

#파일 포맷 옵션 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left",padx=5, pady=5)

# 진행 상황 Progress Bar
frame_progressbar = LabelFrame(root, text="진행상황")
frame_progressbar.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progressbar, maximum=100, variable=p_var)
progress_bar.pack(fill="x",padx=5, pady=5)

# 실행 프레임
frame_run=Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, pady=5, padx=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right",padx=5, pady=5)

btn_start = Button(frame_run, pady=5, padx=5, text="시작", width=12, command=start)
btn_start.pack(side="right",padx=5, pady=5)




root.resizable(False, False)
root.mainloop()