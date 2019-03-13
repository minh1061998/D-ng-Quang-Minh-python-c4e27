from turtle import*
def draw_square(length,mau):
    for i in range(4):
        color(mau)
        forward(length)
        left(90)
draw_square(100,'green')
mainloop()
