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
    if int(pm.read_int(ptraddr(  ) == 1 :   # 메모리 주소 제거
        return 'O'
    else:
        return 'X'




try:   # 정상실행
    pm = pymem.Pymem("Among Us.exe")
    gameModule = module_from_name(pm.process_handle, "GameAssembly.dll").lpBaseOfDll #"UnityPlayer.dll"+012A7B34
    gameModule2 = module_from_name(pm.process_handle, "UnityPlayer.dll").lpBaseOfDll
    
    choice = 0
    speed = pm.read_float(ptraddr(0x01C52828,[0x14, 0x38, 0x108, 0x64, 0x5C, 0x4, 0x14],1))
    imposter_ch()



    while choice != -1:
        print("\n\n\t\t\t\t\=== 메뉴 ===/\n\n")
        print("\t|\t [1] speed[ "+ str(speed) +" ] \t|\t [2] imposter[ "+ str(imposter_ch()) +" ] \t|\t [3] Kill Cooldown \t|\t [-1] 종료 ")
        choice = int(input("요소를 선택하세요 : "))

        if choice == -1: #선택 종료
            break

        elif choice == 1: # 스피드 변경
            speed = float(input("속도를 입력하세요 : "))
            pm.write_float(ptraddr(     )    # 메모리 주소 제거
            print("\n 스피드 적용 성공")
            time.sleep(1.5)
            os.system('cls')

        elif choice == 2: # 임포스터
            if imposter_ch() == 'X':
                pm.write_int(   ) # 메모리 주소 제거
            else:
                pm.write_int(   ) # 메모리 주소 제거
            os.system('cls')
        
        elif choice == 3:
            pm.write_float(   )   # 메모리 주소 제거
            os.system('cls')


        elif choice == 4:
            pm.write_int(   )   # 메모리 주소 제거



except: # 오류발생
    
    ### 스피드 설정 후 적용 ###
    def speedset():
        print(w2.get())


    ### 기본 설정 ###
    win = Tk()
    win.geometry("320x150")
    win.title("어몽어스 핵")

    ### 체크리스트 ###
    length_label = Label(win, text="Made By Dohyun(unifox)").grid(row=0, column=1)
    chkvar1 = IntVar()
    chkvar2 = IntVar()
    chkvar3 = IntVar()
    chkbox1 = Checkbutton(win,text="임포스터", variable=chkvar1).grid(row=1, column=0,padx = 1,pady = 0,ipadx=0)
    chkbox3 = Checkbutton(win,text="No clip(벽뚫)", variable=chkvar3).grid(row=1, column=1)


    ### 이동속도 ###
    chkbox2 = Checkbutton(win,text="스피드", variable=chkvar2).grid(row=2, column=0,ipadx=0)
    w2 = Scale(win, from_=0, to=50, tickinterval= 50, orient=HORIZONTAL, length=230)
    w2.set(10)
    w2.grid(row=2, column=1)


    btn1 = Button(win, text='킬쿨 0초', command=speedset).grid(row=4,column=0)
    btn2 = Button(win, text='적용', command=speedset, width=30).grid(row=4,column=1)


    
    


    win.mainloop()

        
#UnityPlayer.dll+960C94 
# 0F 85 A2 00 00 00     : on
# 0F 84 A2 00 00 00     : off