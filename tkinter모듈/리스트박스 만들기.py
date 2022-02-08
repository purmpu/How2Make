from tkinter import *
import tkinter   # '*'은 tkinter 라이브러리 내 모든 함수를 가져온다는 뜻

window = Tk()

window.title("ID&PW")    #윈도우창의 이름
window.geometry("600x400+100+100")    #너비x높이+x좌표+y좌표
window.resizable(False,False) #윈도우창의 (상하,좌우) 크기 조절 여부. 여기선 False로 불가능

listbox = tkinter.Listbox(window, selectmode='extended', height=0)
listbox.insert(0, "1번")
listbox.insert(1, "2번")
listbox.insert(2, "2번")
listbox.insert(3, "2번")
listbox.insert(4, "3번")
listbox.delete(1, 2)    #이렇게 리스트박스 인덱스순서 1번째 2번째를 삭제했으므로 실제 표시되는선 0,3,4번만 표시됨
listbox.pack()


window.mainloop()
