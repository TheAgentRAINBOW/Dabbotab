# Why did I create this?
import tkinter as tk
import random as ran
import os

counter = 0
def counter_sign(label):
    def count():
        global counter
        label.config(text = "%.2f" % counter)
        label.after(100, count)
        counter = counter + 0.1
    count()

def center_mum(load):
    width = load.winfo_screenwidth()
    height = load.winfo_screenheight()
    x = ran.randint(0,width)
    y = ran.randint(0,height)
    load.geometry('%dx%d+%d+%d' % (190, 99, x, y))

def month():
    os.system("ffplay -nodisp reet.mp3 & disown")
    load = tk.Tk()
    center_mum(load)
    load.title("I ran out of funny things to say.")
    label = tk.Label(load, fg="orange")
    label.pack()
    counter_sign(label)
    butt = tk.Button(load, text="NEIN, NEIN, NEIN", width=30, command=load.destroy)
    butt.pack()
    load.mainloop()
while True:
    month()
