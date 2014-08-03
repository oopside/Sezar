# -*- coding: cp1254 -*-
#Pencere İşlemler
from Tkinter import *
anapen = Tk()
anapen.title(u"Ceasar Yöntemiyle Şifreleme")
anapen.geometry("470x580+300+100")
anapen.wm_iconbitmap("gray12")
anapen.resizable(False, False)
anapen.wm_attributes("-topmost", 1)
anapen.tk_setPalette("black")

#Fonksiyonlar
def geriCevir(x):
    return chr(x)
 
def yapistir():
    global metin
    metin = giris.get(0.0, END)
    sifre = list(map(f, metin))
    cikis1.delete(0.0,END)
    cikis1.insert(INSERT, str(sifre[:-1])[1:-1])
    sifrelimetin = ''.join(geriCevir(i) for i in sifre)
    cikis2.delete(0.0,END)
    cikis2.insert(INSERT, str(sifrelimetin))
    cozulen = list(map(coz, sifrelimetin))

def sifreCoz():
    global metin
    metin = giris.get(0.0, END)
 
    sifre = list(map(coz, metin[:-1]))
    cikis1.delete(0.0,END)
    cikis1.insert(INSERT, str(sifre)[1:-1])
    sifrelimetin = ''.join(geriCevir(i) for i in sifre)
    cikis2.delete(0.0,END)
    cikis2.insert(INSERT, str(sifrelimetin))
    cozulen = list(map(coz, sifrelimetin))
 
def f(x):
    return ord(x)+3
 
def coz(x):
    return ord(x)-3
 
#Pencere
Karsila = Label(anapen)
Karsila.config(text = u"Ceasar Yöntemiyle Şifreleme ve Çözme")
Karsila.place(x=1,y=1)
 
GirisBir = Label(anapen)
GirisBir.config(text = u"Giriş:")
GirisBir.place(x=1,y=25)
 
giris = Text(anapen)
giris.config(width = 40, height = 8, font = "arial 12")
giris.place(x=100,y=25)
 
karsilama1 = Label(anapen)
karsilama1.config(text = u"ASCII Hali:")
karsilama1.place(x=1,y=200)
 
cikis1 = Text(anapen)
cikis1.config(width = 40, height = 8, font = "arial 12")
cikis1.place(x=100,y=200)
 
karsilama2 = Label(anapen)
karsilama2.config(text = u"Çıkış:")
karsilama2.place(x=1,y=375)
 
cikis2 = Text(anapen)
cikis2.config(width = 40, height = 8, font = "arial 12")
cikis2.place(x=100,y=375)
 

 
hesapButon = Button(anapen)
hesapButon.config(text = u"Hesapla!",command = yapistir)
hesapButon.place(x=1,y=550)
 
cozButon = Button(anapen)
cozButon.config(text = u"Şifre Çöz!",command = sifreCoz)
cozButon.place(x=410,y=550)
 
mainloop()
