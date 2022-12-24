import turtle as t
import Library_Queen as q #собственно написанная библиотека
SIZE=50 #длина и ширина одной клетки
N=8 #количество ферзей
t.speed(1000)

queen=q.Queen(N)
res = queen.get_result()

def square(x,y,z):
    t.penup() #подняли ручку - при перемещении рисунок не выполняется
    t.goto(x,y) #перемещение черепашки в точку с координатами x,y
    t.pendown() #опустили ручку - при перемещении рисунок будет выполняться

    if z%2==1:
        t.color('#000000','#3366CC')
    else:
        t.color('#000000','#FFFFFF')

    t.begin_fill()
    for i in range(4):
        t.forward(SIZE)
        t.left(90)
    t.end_fill()

def rectangle(x,y,w,h): #прямоугольник от ферзя
    t.penup()
    t.goto(x,y)
    t.pendown()

    t.begin_fill()
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()


def trapezoid(x,y,w,h): #трапеция от ферзя
        t.penup()
        t.goto(x, y)
        t.pendown()

        t.begin_fill()
        for i in range(1):
            t.left(115)
            t.forward(w)
            t.right(115)
            t.forward(h)
            t.right(115)
            t.forward(w)
            t.left(115)
        t.end_fill()

def crown(a):  # корона ферзя
        t.penup()
        t.goto(a[0][0], a[0][1])
        t.pendown()

        t.begin_fill()
        for b in a:
            t.goto(b[0], b[1])
        t.end_fill()


def queen(x,y,z):

    if z%2==0:
        t.color('#000000','#F386AC')
    else:
        t.color('#000000','#FFFFFF')

    rectangle(x + SIZE * 0.1, y + SIZE * 0.1, SIZE * 0.8, SIZE * 0.1)
    rectangle(x + SIZE * 0.15, y + SIZE * 0.2, SIZE * 0.7, SIZE * 0.1)
    trapezoid(x+SIZE*0.15, y+SIZE*0.3,SIZE*0.2,SIZE*0.88)
    a = ((x + SIZE * 0.10, y + SIZE * 0.49),
         (x + SIZE * 0.01, y + SIZE * 0.95),
         (x + SIZE * 0.30, y + SIZE * 0.49),
         (x + SIZE * 0.50, y + SIZE * 0.95),
         (x + SIZE * 0.70, y + SIZE * 0.49),
         (x + SIZE * 0.99, y + SIZE * 0.95),
         (x + SIZE * 0.9, y + SIZE * 0.49))
    crown(a) #используем список с координатами, по которым строим точки

######################### - создание доски
t.hideturtle() #прячем черепашку
for j in range(8):
    for k in range(8):
        x=j*SIZE-4*SIZE
        y=k*SIZE-4*SIZE
        z=j+k
        square(x,y,z)
        if res[j][k] == 1:
            queen(x, y, z)
########################
t.update()