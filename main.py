from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def m_forward():
    tim.forward(10)

def m_backward():
    tim.back(10)

def t_left():
    tim.lt(10)

def t_right():
    tim.rt(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()

def draw():
    tim.pendown()

screen.onkeypress(key="w", fun=m_forward)
screen.onkeypress(key="s", fun=m_backward)
screen.onkeypress(key="a", fun=t_left)
screen.onkeypress(key="d", fun=t_right)
screen.onkeypress(key="c", fun=clear)
screen.onkeypress(key="v", fun=draw)


screen.listen()
screen.exitonclick()
