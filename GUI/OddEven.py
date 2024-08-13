# Create a GUI with a text box and a button. When the button is clicked, check value of textbox and print odd/even in a message box
import tkinter as tk
from tkinter import messagebox
class GUI:
    def __init__(self,window):
        self.xlbl1=tk.Label(window,text="Text1")
        self.xlbl1.place(x=20,y=20)
        self.txt1=tk.Entry(window,width=30)
        self.txt1.place(x=80,y=20)
        self.btn1=tk.Button(window,text="Msg",command=self.show)
        self.btn1.place(x=20,y=120)
    def show(self):
       messagebox.showinfo("odd even check",'even')
window=tk.Tk()
window.geometry('400x400')
ob=GUI(window)
window.mainloop()


