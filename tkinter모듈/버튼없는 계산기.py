from tkinter import *
import tkinter   # '*'은 tkinter 라이브러리 내 모든 함수를 가져온다는 뜻

window = Tk()

window.title("ID&PW")    #윈도우창의 이름
window.geometry("600x400+100+100")    #너비x높이+x좌표+y좌표
window.resizable(False,False) #윈도우창의 (상하,좌우) 크기 조절 여부. 여기선 False로 불가능

count = 0

def calc(event):
    label.config(text="결과="+str(eval(entry.get())))    #get()은 entry에서 입력받은 것을 문자열로 반환



entry = tkinter.Entry(window)   #창에서 숫자 기입창의 속성을 정함, 매개변수 사용가능
entry.bind("<Return>",calc)     #Entry.bind()를 이용하여 키보드,마우스의 입력을 처리하여 메서드나 함수를 실행시킬 수 있음
entry.pack()

label = tkinter.Label(window)    
label.pack()

window.mainloop()
