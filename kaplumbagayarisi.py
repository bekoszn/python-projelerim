from turtle import *
from random import *
from tkinter import messagebox
import turtle
import time
    
# Ekran Kurulum
setup(800, 500)
title("Kaplumbağa Yarışı")
bgcolor("darkturquoise")
speed(0)

# Başlık
penup()
goto(-100, 205)
color("white")
write("KAPLUMBAĞA YARIŞI", font=("Arial", 20, "bold"))

# Yarış Alanı
goto(-350, 200)
pendown()
color("black")
begin_fill()
for i in range(2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill()

# Bitiş Çizgisi
gap_size = 20
shape("square")
penup()

# Bitiş çizgisi beyaz sırası 1
color("white")
for i in range(10):
    goto(250, (170 - (i * gap_size * 2)))
    stamp()

# Bitiş çizgisi beyaz sırası 2
for i in range(10):
    goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
    stamp()

# Bitiş çizgisi siyah sırası 1
color("black")
for i in range(10):
    goto(250, (190 - (i * gap_size * 2)))
    stamp()

# Bitiş çizgisi siyah sırası 2
for i in range(10):
    goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
    stamp()

# 1. Kaplumbağa - Beyaz
beyaz = Turtle()
beyaz.color("white")
beyaz.shape("turtle")
beyaz.shapesize(1.5)
beyaz.penup()
beyaz.goto(-210, 125)
beyaz.pendown()

# 2. Kaplumbağa - Kırmızı
kirmizi = Turtle()
kirmizi.color("red")
kirmizi.shape("turtle")
kirmizi.shapesize(1.5)
kirmizi.penup()
kirmizi.goto(-210, 50)
kirmizi.pendown()

# 3. Kaplumbağa - Pembe
pembe = Turtle()
pembe.color("hotpink")
pembe.shape("turtle")
pembe.shapesize(1.5)
pembe.penup()
pembe.goto(-210, -25)
pembe.pendown()

# 4. Kaplumbağa - Gold
gold = Turtle()
gold.color("gold")
gold.shape("turtle")
gold.shapesize(1.5)
gold.penup()
gold.goto(-210, -100)
gold.pendown()

# Yarıştan önce 1 saniye bekle
time.sleep(1)

#Kaplumbağaların yarışı için rastgele sayılar geliyor
for i in range(145):
    beyaz.forward(randint(1, 5))
    kirmizi.forward(randint(1, 5))
    pembe.forward(randint(1, 5))
    gold.forward(randint(1, 5))
    
#Kazananı açıklama
if beyaz.xcor() > kirmizi.xcor() and beyaz.xcor() > pembe.xcor() and beyaz.xcor() > gold.xcor():
    messagebox.showinfo('Yarış Sonucu', 'Beyaz kazandı')

elif kirmizi.xcor() > beyaz.xcor() and kirmizi.xcor() > pembe.xcor() and kirmizi.xcor() > gold.xcor():
    messagebox.showinfo('Yarış Sonucu', 'Kırmızı kazandı')

elif pembe.xcor() > beyaz.xcor() and pembe.xcor() > kirmizi.xcor() and pembe.xcor() > gold.xcor():
    messagebox.showinfo('Yarış Sonucu', 'Pembe kazandı')

else:
    messagebox.showinfo('Yarış Sonucu', 'Gold kazandı')
