from turtle import Turtle, Screen
from random import randint
from tkinter import messagebox,Tk

""" 
windows message popout way
# import ctypes
# 
# def Mbox(title, text, style):
#     return ctypes.windll.user32.MessageBoxW(0, text,  title, style)
"""


screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor('#DDF7D5')

user_input = screen.textinput(title="Make your bet", prompt="Which color turtle will win the race? Enter a color: ").lower()

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

turtle_list = []
start_y = -70
for i in range(len(colors)):
    tt = Turtle('turtle')
    tt.up()
    tt.color(colors[i])
    tt.goto(x=-230, y=start_y)
    start_y += 40
    turtle_list.append(tt)

status = 0
if user_input:
    status = 1

while status:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            status = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner.")
                # Mbox('RESULT', f"You've won! The {winning_color} turtle is the winner.", 1) ##windows
                #messagebox.showinfo(f"You've won! The {winning_color} turtle is the winner.") #mac
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
                # Mbox('RESULT', f"You've lost! The {winning_color} turtle is the winner.", 1) ##windows

                #messagebox.showinfo(message=f"You've lost! The {winning_color} turtle is the winner.") ##mac
        turtle.forward(randint(1,10))
screen.exitonclick()