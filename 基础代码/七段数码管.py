import turtle, datetime
def drawline(draw) :
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawDigit(d):
    drawline(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawline(False)
    drawline(True) if d in [0, 2, 6, 8] else drawline(False)
    turtle.left(90)
    drawline(True) if d in [0, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    for i in date:
        drawDigit(eval(i))
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    # drawDate(datetime.datetime.now().strftime('%Y%m%d'))
    # 输出0-9
    for s in range(0, 10):
        drawDigit(s)
    turtle.hideturtle()
main()