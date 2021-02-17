import os
import time
import tkinter
from tkinter import *
from pymem import *
from pymem.process import *

def ptraddr(main,ptrlist,mod):  # 포인터 주소 구하는 함수
    if mod == 1: #모듈 선택
        main+=gameModule
    else:
        main+=gameModule2

    addr = pm.read_int(main)
    for i in range (len(ptrlist)-1):
        addr = pm.read_int(addr+ptrlist[i])
    return addr + ptrlist[-1]

def imposter_ch():
    if int(pm.read_int() == 1 :
        return 'O'
    else:
        return 'X'




try:   # 정상실행
    pm = pymem.Pymem("Among Us.exe")
    gameModule = module_from_name(pm.process_handle, "GameAssembly.dll").lpBaseOfDll #"UnityPlayer.dll"+012A7B34
    gameModule2 = module_from_name(pm.process_handle, "UnityPlayer.dll").lpBaseOfDll
    
    choice = 0
    basespeed = pm.read_float()
    speed = 0
    imposter_ch()


    ### 스피드 설정 후 적용 ###
    def apply():
        if chkvar1.get() == 10: # 임포스터
            pm.write_int())
        else:
            pm.write_int()


        if chkvar2.get() == 10: #노클립
            pm.write_int(gameModule2+0x960C95,41605)
        else:
            pm.write_int(gameModule2+0x960C95,41604)


        if chkvar3.get() == 10:
            speed = w2.get()
            pm.write_float(  ,float(speed))
        else:
            pm.write_float(  ,float(basespeed))


    def killcool():
        pm.write_float(  ,float(0))


    ### 기본 설정 ###
    win = Tk()
    win.geometry("320x140")
    win.title("어몽어스 핵")
    win.minsize(width=320, height=140)
    win.maxsize(width=320, height=140)

    length_label = Label(win, text="Made By Dohyun (unifox)", bg="orange",width=70).place(x=0,y=0)

    ### 체크리스트 ###
    chkvar1 = IntVar()
    chkvar2 = IntVar()
    chkvar3 = IntVar()
    chkbox1 = Checkbutton(win,text="임포스터", variable=chkvar1, onvalue=10, offvalue=20).place(x=10,y=25)#grid(row=0, column=0,padx = 1,pady = 0,ipadx=0)
    chkbox2 = Checkbutton(win,text="No clip(벽뚫)", variable=chkvar2, onvalue=10, offvalue=20).place(x=110,y=25)


    ### 이동속도 ###
    chkbox3 = Checkbutton(win,text="스피드", variable=chkvar3,onvalue=10, offvalue=20).place(x=10,y=62)
    w2 = Scale(win, from_=0, to=50, tickinterval= 50, orient=HORIZONTAL, length=230)
    w2.set(10)
    w2.place(x=75,y=45)

    ### 적용과 킬쿨 ###
    btn1 = Button(win, text='킬쿨 0초', command=killcool).place(x=10,y=110)
    btn2 = Button(win, text='적용', command=apply, width=32).place(x=80,y=110)

    win.mainloop()



except: # 오류발생
    
    ### 기본 설정 ###
    win = Tk()
    win.geometry("320x140")
    win.title("어몽어스 핵")
    win.minsize(width=320, height=140)
    win.maxsize(width=320, height=140)
    length_label = Label(win, text="Made By Dohyun (unifox)", bg="orange",width=70).place(x=0,y=0)
    length_label2 = Label(win, text="오류발생!!",bg="yellow",foreground="red").place(x=130,y=24)
    length_label3 = Label(win, text="프로그램 오류가 발생했습니다!\n게임에 들어간 이후\n프로그램을 다시 시작해주세요!").place(x=70,y=50)
    length_label = Label(win, text="contact | trouna43@devdori.com", bg="orange",width=45).place(x=0,y=120)
    win.mainloop()

        
#UnityPlayer.dll+960C94 
# 0F 85 A2 00 00 00     : on
# 0F 84 A2 00 00 00     : off