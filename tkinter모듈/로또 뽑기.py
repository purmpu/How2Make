from tkinter import *
import tkinter   # '*'은 tkinter 라이브러리 내 모든 함수를 가져온다는 뜻
import random
window = Tk()

window.title("제발당첨제발")    #윈도우창의 이름
window.geometry("720x600+100+100")    #너비x높이+x좌표+y좌표
window.resizable(False,False) #윈도우창의 (상하,좌우) 크기 조절 여부. 여기선 False로 불가능


#def randomnum(event):
        #label.config(text = "결과\n"+str(random.sample(range(1,46),6)))



def numbtn():
    label2 = Label(window, text=str(random.sample(range(1,46),6)), width=20, height=3, relief="raised")
    label2.pack()

button1 = Button(window,text = "뽑기", overrelief="solid", width=15, command=numbtn, repeatdelay=1000, repeatinterval=100)
button1.pack()

#ent = Entry(window, width = 5, font = ('TkDefaultFont', 24), bd = 10 )
#ent.bind("<Return>",randomnum)
#ent.pack()


window.mainloop()
