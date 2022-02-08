from tkinter import *
import tkinter   # '*'은 tkinter 라이브러리 내 모든 함수를 가져온다는 뜻

window = Tk()

window.title("ID&PW")    #윈도우창의 이름
window.geometry("600x400+100+100")    #너비x높이+x좌표+y좌표
window.resizable(False,False) #윈도우창의 (상하,좌우) 크기 조절 여부. 여기선 False로 불가능

count = 0

def countUP():
    global count
    count += 1
    label.config(text=str(count))

label = tkinter.Label(window, text = "0", width=10,height=3,fg="black",relief="raised")    #이것으로 위젯을 설정할수 있다.
label.pack()    #pack함수로 창에 배치해야 위젯을 창에서 볼 수 있다

button = tkinter.Button(window, text = "click", overrelief="solid", width=15, command=countUP, repeatdelay=1000, repeatinterval=100)
button.pack()

window.mainloop()
