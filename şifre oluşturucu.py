from tkinter import *
import random
import string
from tkinter import messagebox

def olustur():
    sifre= []
    for i in range(2):
        entry.delete(0, END)
        kucukharf=random.choice(string.ascii_lowercase)
        buyukharf=random.choice(string.ascii_uppercase)
        sayi=random.choice(string.digits)
        karakter=random.choice(string.punctuation)
        sifre.append(kucukharf)
        sifre.append(buyukharf)
        sifre.append(sayi)
        sifre.append(karakter)
        kat="".join(str(x)for x in sifre)
        entry.insert(0, kat)
        
        

def kopyala():
    pencere.clipboard_clear()
    pencere.clipboard_append(entry.get())
    messagebox.showinfo("Bilgilendirme", "Seçiminiz başarıyla kopyalanmıştır.")

def secim():
    if choice.get()== 1:
        return"".join(random.sample(zayif,))
    if choice.get()== 2:
        return"".join(random.sample(normal, val.get()))
    if choice.get()== 3:
        return"".join(random.sample(guclu, val.get()))
    
zayif=string.ascii_lowercase+string.ascii_uppercase
normal=string.ascii_lowercase+string.ascii_uppercase+string.digits
guclu=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

    
pencere =Tk()
pencere.configure(background="black")
pencere.geometry("450x300")
pencere.title("Şifre Oluşturma Programı")
choice = IntVar()
r1=Radiobutton(pencere,text="Zayıf Şifre Seçimi", font = ('arial', 20, 'bold'), bg="dark orange" , variable=choice, value=1, command=secim)
r2=Radiobutton(pencere,text="Normal Şifre Seçimi", font = ('arial', 20, 'bold'), bg="dark orange", variable=choice, value=2, command=secim)
r3=Radiobutton(pencere,text="Güçlü Şifre Seçimi", font = ('arial', 20, 'bold'), bg="dark orange", variable=choice, value=3, command=secim)
r1.pack()
r2.pack()
r3.pack()

entry= Entry(pencere, font = ('arial', 40, 'bold'), bg="dark orange")
entry.pack()
buton=Button(pencere,text="Şifre Oluştur", font = ('arial', 40, 'bold'), fg="dark orange",command= olustur). place(x=100,y=200)
buton2=Button(pencere, text="Kopyala", font = ('arial', 20, 'bold'), fg="dark orange",command=kopyala). place(x=100,y=250)
pencere.mainloop()
