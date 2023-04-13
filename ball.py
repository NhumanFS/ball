from tkinter import *
import random
import time

tk = Tk()
tk.title("ball")
tk.resizable(0, 0)
canvas = Canvas(tk, width=500, height=400)
canvas.pack()


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.x = 0
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.canvas_height:
            self.y = -2
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2


ball = Ball(canvas, "green")
while True:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
