from tkinter import *
import tkinter   # '*'은 tkinter 라이브러리 내 모든 함수를 가져온다는 뜻
import random
window = Tk()

window.title("제발당첨제발")    #윈도우창의 이름
window.geometry("720x600+100+100")    #너비x높이+x좌표+y좌표
window.resizable(False,False) #윈도우창의 (상하,좌우) 크기 조절 여부. 여기선 False로 불가능

labelist = []

def removenum():    #지금까지 표시된 숫자리스트를 전부 지움
    global label2
    global labelist
    for i in range(len(labelist)):
        labelist[i].destroy()
    
def numbtn():    #6개의 무작위 숫자로 구성된 리스트를 화면에 띄움
    global label2
    global labelist
    label2 = Label(window, text=str(random.sample(range(1,46),6)), width=20, height=3, relief="raised", bg = "orange")
    label2.pack()
    labelist.append(label2)
    

button1 = Button(window,text = "뽑기", overrelief="solid", width=15, command=numbtn, bg = "green", repeatdelay=1000, repeatinterval=100)
button1.pack()    #숫자 띄우는 버튼

button2 = Button(window,text = "전부 지우기", overrelief="solid", width=15, command=removenum, bg = "red", repeatdelay=1000, repeatinterval=100)
button2.pack()    #지우는 버튼



window.mainloop()
