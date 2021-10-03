from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Separator,Progressbar
import os
import sys
import requests
from shutil import rmtree as rmt
import shutil
from subprocess import check_output as sp_c_o
from subprocess import STDOUT as STDOUT
from webbrowser import open as wb_o
from requests import get
from PIL import Image,ImageTk
import pyglet
import pickle
import threading

font_name = ('Jua-Regular')
p = str(os.path.dirname(os.path.realpath(__file__))).replace('\\','/')

with open('data.seon_simple_installer','rb') as f:
    data = pickle.load(f)
    f.close()
    #print(data)

texts = {
    '0':{
        'kor':'<int>초 후 업데이트를 체크합니다.'
        },
    '1':{
        'kor':'''SEON 간편설치기 이용 가이드

1. 인터넷에 연결 되어있는지 확인해 주세요.

2.Java가 설치되어있는지 확인해주세요.
(설치 되어있지 않다면 "Java 설치" 버튼을 눌려주세요.)

3.이 프로그램은 .minecraft, mods, shaders 폴더를 수정합니다.

위 내용을 모두 확인 하였으면 "다음" 버튼을 눌려주세요.

Copyright 2021. seon06 all rights reserved.
'''
        },
    '2':{
        'kor':'''SEON 간편설치기

OPTIFINE을 설치 하실려면 "OPTIFINE" 을
MOD를 설치 하실려면 "MOD"을 클릭해주세요.

*OPTIFINE: 마인크래프트 최적화 프로그램, 쉐이더 적용가능
OPTIFINE 선택시 OPTIFINE, SHADER 설치 가능

*MOD:
MOD 선택시 FORGE, MOD, OPTIFINE 설치 가능

*OPTIFINE과 MOD를 함께 적용 할려면 MOD를 선택해 주세요.
'''
        }
    }

version = '0.0.1'

def uc():
    global root
    root.destroy()
    main_page()
def uce():
    global root,p
    if True:
        try:
            r = requests.get('https://api.github.com/repos/seon06/SEON_SIMPLE_INSTALLER_FOR_MC/releases/latest')
            r = r.json()['name'].split(' ')[2].replace('v','')
            print(r)
            if r == version:
                messagebox.Message(title='업데이트 완료',message='최신 버전이에요.').show()
            else:
                messagebox.Message(title='업데이트 발견',message='앗! 최신 업데이트를 발견했어요.\n아직 자동 업데이트 기능이 없으니\n업데이트를 하시고 싶으시면 GITHUB에서 다운로드 해주세요!').show()
            root.destroy()
            main_page()
        except Exception as e:
            print(e)
            messagebox.showerror(title='!',message='업데이트를 불러오는데 실패했어요\n업데이트를 취소하고 설치를 진행합니다.')
            root.destroy()
            main_page()
        
    else:
        root.destroy()
        main_page()
def loading():
    def ac(v):
        global una
        una.config(text=texts['0']['kor'].replace('<int>',str(v)))
        if v == 0:
            uce()
    global una,root
    root = Tk()
    button_i = Image.open('%s/system/img/button3.png'%p)
    button_image = ImageTk.PhotoImage(button_i.resize((150,50), Image.ANTIALIAS))
    root.title('SEON 간편설치기')
    root.resizable(False, False)
    root.geometry('700x400')
    root.config(bg='white')
    F = Frame(root, bg='white')
    Label(F,text='SEON 간편 설치기',font=('Jua',20),bg='white',fg='blue').pack()
    Separator(F,orient='horizontal').pack(fill='both')
    una = Label(F,text=texts['0']['kor'].replace('<int>','3'),bg='yellow',font=('Jua',15))
    una.pack(pady=50)
    Button(F,text='자동 업데이트 건너뀌기',command=uc,image=button_image,bg='white',highlightthickness = 0, borderwidth=0,compound='center',font=('Jua',11)).pack(side='bottom',pady=20)
    F.pack(fill='both',padx=80,expand=True)
    root.after(1000, lambda: ac(2))
    root.after(2000, lambda: ac(1))
    root.after(3000, lambda: ac(0))
    root.mainloop()
def main_page():
    def n():
        root.destroy()
        select_sm()
    root = Tk()
    root.title('SEON 간편설치기')
    root.resizable(False, False)
    button_i = Image.open('%s/system/img/button3.png'%p)
    button_image = ImageTk.PhotoImage(button_i.resize((150,50), Image.ANTIALIAS))
    root.geometry('700x500')
    root.config(bg='white')
    F = Frame(root,bg='white')
    Label(F,text='SEON 간편 설치기',font=('Jua',20),bg='white',fg='blue').pack()
    Separator(F,orient='horizontal').pack(fill='both')
    a = Text(F,bg='white',fg='gray',highlightthickness = 0, borderwidth=0)
    a.insert(END,texts['1']['kor'])
    a.config(state=DISABLED)
    a.pack(anchor=CENTER,pady=20)
    f = Frame(root,bg='white')
    Button(f,text='Java 설치',command= lambda: wb_o('https://java.com/ko/download/ie_manual.jsp?locale=ko'),image=button_image,bg='white',highlightthickness = 0, borderwidth=0,compound='center',font=('Jua',11)).pack(side='left')
    Button(f,text='다음',command=n,image=button_image,bg='white',highlightthickness = 0, borderwidth=0,compound='center',font=('Jua',11)).pack(side='right')
    
    F.pack(fill='x',padx=80)
    f.pack()
    root.mainloop()
def select_sm():
    root = Tk()
    root.title('SEON 간편설치기')
    root.resizable(False, False)
    def o():
        root.destroy()
        select_optifine()
    button_i = Image.open('%s/system/img/button3.png'%p)
    button_image = ImageTk.PhotoImage(button_i.resize((150,50), Image.ANTIALIAS))
    root.geometry('700x500')
    root.config(bg='white')

    F = Frame(root,bg='white')
    f = Frame(root,bg='white')
    Label(F,text='SEON 간편 설치기',font=('Jua',20),bg='white',fg='blue').pack()
    Separator(F,orient='horizontal').pack(fill='both')
    a = Text(F,bg='white',fg='gray',highlightthickness = 0, borderwidth=0)
    a.insert(END,texts['2']['kor'])
    a.config(state=DISABLED)
    a.pack(anchor=CENTER,pady=20)
    Button(f,text='OPTIFINE',command=o,image=button_image, bg='white',highlightthickness = 0, borderwidth=0,compound='center',font=('Jua',11)).pack(side='left')
    Button(f,text='MOD',image=button_image, bg='white',highlightthickness = 0, borderwidth=0,compound='center',font=('Jua',11)).pack(side='right')
    
    F.pack(fill='x',padx=80)
    f.pack()
    root.mainloop()
def download_url(url,name):
    global p
    dp = Toplevel()
    dp.title('Download')
    dp.resizable(False,False)
    r = requests.get(url)
    print(r)
    print(url)
    open('%s/system/download/%s.jar'%(p,name),'wb').write(r.content)

    print('end')
def download(name, version, path, version2=None):
    if name == 'optifine':
        for i in data['download']['mods']:
            if i['name'] == 'optifine':
                f = i['files']
        for i in f:
            if i['mc_version'] == version and i['version'] == version2:
                print(version,version2, '||', i['mc_version'],i['version'])
                a = messagebox.askyesno(title='Download',message='Optifine-%s_%s을 다운로드 하시겠습니까?'%(version,version2))
                if a == True:
                    download_url(i['link'],'optifine')
                else:
                    print(False)
                return
        print(version,version2, '||', i['mc_version'],i['version'])
        messagebox.showerror(title='!',message='다운 받을 파일을 선택하세요.')

def select_optifine():
    root = Tk()
    root.title('SEON 간편설치기')
    root.resizable(False, False)
    button_i = Image.open('%s/system/img/button3.png'%p)
    button_image = ImageTk.PhotoImage(button_i.resize((150,50), Image.ANTIALIAS))
    root.geometry('700x500')
    root.config(bg='white')

    F = Frame(root,bg='white')
    Label(F,text='SEON 간편 설치기',font=('Jua',20),bg='white',fg='blue').pack()
    Separator(F,orient='horizontal').pack(fill='both')
    Label(F,text='\nOPTIFINE',font=('Jua',20),bg='white',fg='gray').pack()
    sc = Scrollbar(F)
    sc.pack(side='right',fill='y')
    L = Listbox(F,selectmode='single',font=('Jua',15),yscrollcommand=sc.set)
    for i in data['download']['mods']:
        if i['name'] == 'optifine':
            f = i['files']
    for i in f:
        L.insert(f.index(i),str(i['mc_version']+' '+i['version']))
    sc['command']=L.yview
    L.pack(fill='both',expand=True)

    Button(root,text='DOWNLOAD',command=lambda: download('optifine',L.get(L.curselection()).split(' ')[0],'',version2=L.get(L.curselection()).split(' ')[1] ),image=button_image, bg='white',highlightthickness = 0, borderwidth=0,compound='center',font=('Jua',11)).pack(side='bottom')
    
    F.pack(fill='both',padx=80,expand=True)
    root.mainloop()
pyglet.font.add_file('%s/system/Jua-Regular.ttf'%p)
loading()
