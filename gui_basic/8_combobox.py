import tkinter.ttk as ttk
from tkinter import*


root = Tk()
root.title("Nado Gui")
root.geometry("640x480+300+100") #(가로 X 세로) + x좌표 + y좌표

values = [str(i) + "일" for i in range(1,32)] #1~31까지의 숫자를 반환
combobox = ttk.Combobox(root,height=5,values=values)
combobox.pack()
combobox.set("카드 결제일") #최초 목록의 제목 설정

readonly_combobox = ttk.Combobox(root, height=10,values=values,state="readonly")  #readonly는 값을 변경할 수 없고, 선택만 가능함
readonly_combobox.current(0) #0번째 인덱스 값
readonly_combobox.pack()


def btncmd():
    print(combobox.get())#선택된 값 표시
    print(readonly_combobox.get())
    
btn = Button(root,text="선택",command=btncmd)
btn.pack()

root.mainloop()
     