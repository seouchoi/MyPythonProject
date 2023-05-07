from tkinter import*

root = Tk()
root.title("Nado Gui")
root.geometry("640x480+300+100") #(가로 X 세로) + x좌표 + y좌표

listbox = Listbox(root, selectmode="extended",height=0) #extended는 여러개 선택 가능, single은 하나만 선택 가능                                                             
listbox.insert(0,"사과")                                 #height는 한번에 몇 개의 항목을 보여줄 지 결정(0 : 모든 항목 표시, n>0 n개만큼의 항목 표시)
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END,"수박")
listbox.insert(END,"포도")

listbox.pack()

def btncmd():
    #삭제
    #listbox.delete(END) #맨 뒤 항목을 삭제
    #listbox.delete(0) #첫 번째 항목을 삭제

    #갯수 확인
    #print("리스트에는",listbox.size(),"개가 있어요")

    #항목 확인 (시작 인덱스, 끝 인덱스)
    print("1번재부터 3번째까지의 항목 : ",listbox.get(0,2))

    #선택된 항목 확인(위치로 반환 (ex) (1,2,3))
    print("선택된 항목 : ",listbox.curselection())
btn = Button(root,text="클릭",command=btncmd)
btn.pack()

root.mainloop()
