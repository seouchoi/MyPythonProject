import os
from tkinter import*

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480+300+100") #(가로 X 세로) + x좌표 + y좌표

#열기, 저장 파일 이름
filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename):
        with open(filename,"r",encoding="utf8")as file: #파일 있으면 True, 없으면 False
            txt.delete("1.0",END) #텍스트 위젯 본문 삭제
            txt.insert(END,file.read()) #파일 내용을 본문에 입력

def save_file():
    with open(filename,"w",encoding="utf8")as file: #모든 내용을 가져와서 저장
        file.write(txt.get("1.0",END))


menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label = "열기", command=open_file)
menu_file.add_command(label = "저장",command=save_file)
menu_file.add_separator()
menu_file.add_command(label = "종료",command=root.quit)
menu.add_cascade(label = "파일",menu = menu_file)

#스크롤 바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right",fill="y")

#편집, 서식, 보기, 도움말
menu.add_cascade(label = "편집")
menu.add_cascade(label = "서식")
menu.add_cascade(label = "보기")
menu.add_cascade(label = "도움말")

#본문 영역
txt = Text(root,yscrollcommand=scrollbar.set)
txt.pack(side="left",fill="both",expand=True)
scrollbar.config(command=txt.yview)

#메뉴를 생성할 때 필수!
root.config(menu=menu)

root.mainloop()
