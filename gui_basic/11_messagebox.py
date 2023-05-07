import tkinter.messagebox as msgbox
from tkinter import*

root = Tk()
root.title("Nado Gui")
root.geometry("640x480+300+100") #(가로 X 세로) + x좌표 + y좌표

#기차 예매 시스템
def info():
    msgbox.showinfo("알림","정상적으로 예매가 완료되었습니다.")
def warn():
    msgbox.showwarning("경고","해당 좌석은 매진되었습니다.")
def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")
def okcancel():
    msgbox.askokcancel("확인 / 취소","해당 좌석은 유아 동반석입니다. 예매하시겠습니까?")
def retrycancel():
    respons = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")
    if respons == 1: #재시도 respons == True(1)
        print("재시도")
    elif respons == 0: #취소 respons == False(0)
        print("취소")
    
def yesno():
    msgbox.askyesno("예 / 아니오","해당 좌석은 역방향 좌석입니다. 예매하시겠습니까?")
def yesnocancel():
    respons = msgbox.askyesnocancel(title=None,message = "예매 내역이 저장되지않았습니다.\n저장 후 프로그램을 종료하시겠습니까?")
    #네 : 저장 후 종료 respons == True(1)
    #아니오 : 저장하지 않고 종료 respons == False(0)
    #취소 : 종료하지 않음 // respons는 그 외의 값(None)
    if respons == 1: 
        print("예")
    elif respons == 0:
        print("아니오")
    else:
        print("취소")

Button(root,command=info,text="알림").pack()
Button(root,command=warn,text="경고").pack()
Button(root,command=error,text="에러").pack()

Button(root,command=okcancel,text="확인 취소").pack()
Button(root,command=retrycancel,text="재시도 취소").pack()
Button(root,command=yesno,text="예 아니오").pack()
Button(root,command=yesnocancel,text="예 아니오 취소").pack()




root.mainloop()
     