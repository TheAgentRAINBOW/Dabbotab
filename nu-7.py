import tkinter as tk

load = tk.Tk()
loud = tk.PhotoImage(file="nope.gif")
Sans = "Noto Sans Mono CJK JP"

u = tk.Label(load, text="Please help.", fg="#0000FF", font=(Sans, 10, "bold"))
u.pack()
n = tk.Label(load, image=loud)
n.pack()

load.mainloop()
