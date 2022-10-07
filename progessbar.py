from tkinter import *
from tkinter.ttk import *
import time

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x250+1000+300')

def step():
    for i in range(1000):
        ws.update_idletasks()
        pb1['value'] -= 0.333
        time.sleep(0.1)


pb1 = Progressbar(ws, orient=HORIZONTAL, length=100, mode='determinate')
pb1.pack(expand=True)
pb1['value'] = 100


Button(ws, text='Start', command=step).pack()

ws.mainloop()