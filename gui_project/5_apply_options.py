import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import*
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title("Nado Gui")

#파일 추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요.", filetypes=(("PNG 파일","*.png"), ("모든 파일","*.*")),\
                                        initialdir=r"C:\PythonLecture\pygame_basic") 
                                        #최초의 사용자가 지정한 경로를 보여줌  
    for file in files:
        list_file.insert(END,file)
#선택 삭제
def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

#저장 경로(폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '': #사용자가 취소를 누를 때 
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

#이미지 통합
def merge_image():

    try:
        #가로 넓이
        img_width = cmb_width.get()
        if img_width == "원본유지":
            img_width = -1 #-1일떄는 원본 기준으로 
        else:
            img_width = int(img_width)

        #간격
        img_space = cmb_space.get()
        if img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
            img_space = 60
        elif img_space == "넓게":
            img_space = 90
        else: #없음 
            img_space = 0

        #포멧
        img_format = cmb_format.get().lower() #PNG, JPG, BMP 값을 받아와서 소문자로 변경

        ########################################################

        images = [Image.open(x) for x in list_file.get(0,END)] 

        #이미지 사이즈 리스트에 넣어서 하나씩 처리
        image_sizes = [] #[(width1, height1),(width2, height2),...]
        if img_width > -1:
            #width 값 변경
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images] #width값을 변경할 때 같은 비율로 height도 줄어들어야함. 비례식 쓰면 됨
        else:
            #원본 사이즈 적용
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        widths, heights = zip(*(image_sizes))

        #최대 넓이, 전체 높이 구해옴
        max_width, total_height = max(widths), sum(heights)
    
        #스케치북 준비
        if img_space > 0: #이미지 간격 옵션 적용
            total_height += (img_space * (len(images)-1))

        result_img = Image.new("RGB",(max_width,total_height),(255,255,255)) #배경 흰색
        y_offset = 0 #y 위치 
        
        for idx, img in enumerate(images):
            #width가 원본유지가 아닐 때에는 이미지 크기 조정
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img,(0,y_offset))
            y_offset += (img.size[1] + img_space) #height값 + 사용자가 지정한 간격

            progress = (idx + 1)/ len(images) * 100  #실제 percent 정보를 계산
            p_var.set(progress)
            progress_bar.update()


        #포멧 옵션 처리
        file_name = "nado_photo." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("알림", "작업이 완료되었습니다.")
    except Exception as err: #예외처리
        msgbox.showerror("에러",err)

#시작
def start(): 
    #각 옵션들 값 확인
    
    #파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고","이미지 파일을 추가하세요")
        return
    
    #저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고","저장 경로를 선택하세요")
        return
    
    #이미지 통합 작업
    merge_image()


#파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5,pady=5,width=12,text="파일 추가", command=add_file)
btn_add_file.pack(side="left")

btn_delete_file = Button(file_frame, padx=5,pady=5,width=12,text="선택 삭제", command=del_file)
btn_delete_file.pack(side="right")

#리스트 프레임
list_frame=Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", yscrollcommand=scrollbar.set, height=15) #선언에서는 기능을 삽입
list_file.pack(side="left", fill="both", expand=True) #pack 안에는 그리기
scrollbar.config(command=list_file.yview)

#저장 경로 프레임
path_frame = LabelFrame(root, text="저장 경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) #ipady 높이 조정

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

#옵션 프레임
frame_option = LabelFrame(root,text="옵션")
frame_option.pack(padx=5, ipady=5)

#1. 가로 넓이 옵션
#가로 넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", pady=5)

#가로 넓이 콤보
opt_width = ["원본유지","1024","800","640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", pady=5)

#2. 간격 옵션
#간격 옵션 레이블
lbl_space = Label(frame_option, text="간격",width=8)
lbl_space.pack(side="left", pady=5)

#간격 옵션 정보
opt_space= ["없음","좁게","보통","넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space)
cmb_space.current(0)
cmb_space.pack(side="left")

#3. 파일 포맷 옵션  
lbl_format = Label(frame_option, text="포멧", width = 8)
lbl_format.pack(side="left")

#포멧 옵션 정보
opt_format = ["PNG","JPG","BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=8)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

#진행 상황 Progress Bar
frame_progress = LabelFrame(root,text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

#실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, text="닫기", padx=5, pady=5, width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, text="시작", padx=5, pady=5, width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False,False)
root.mainloop()
