# Create the following GUI and perform respective operations on button click
import tkinter as tk
class GUI:
    def __init__(self,window):
        self.xlbl1=tk.Label(window,text="Num1")
        self.xlbl1.place(x=20,y=20)
        self.txt1=tk.Entry(window,width=30)
        self.txt1.place(x=80,y=20)

        self.xlbl2=tk.Label(window,text="Num2")
        self.xlbl2.place(x=20,y=40)
        self.txt2=tk.Entry(window,width=30)
        self.txt2.place(x=80,y=50)

        self.xlbl3=tk.Label(window,text="result")
        self.xlbl3.place(x=20,y=80)
        self.txt3=tk.Entry(window,width=30)
        self.txt3.place(x=80,y=80)



        self.btn1=tk.Button(window,text="Add",command=self.add)
        self.btn1.place(x=20,y=120)
        self.btn2=tk.Button(window,text="Sub",command=self.sub)
        self.btn2.place(x=60,y=120)
        self.btn3=tk.Button(window,text="Mul",command=self.mul)
        self.btn3.place(x=100,y=120)
        self.btn4=tk.Button(window,text="Div",command=self.div)
        self.btn4.place(x=140,y=120)

    def add(self):
        a=int(self.txt1.get())
        b=int(self.txt2.get())
        c=a+b
        self.txt3.delete(0,tk.END)
        self.txt3.insert(0,c)
    
    def sub(self):
        a=int(self.txt1.get())
        b=int(self.txt2.get())
        c=a-b
        self.txt3.delete(0,tk.END)
        self.txt3.insert(0,c)
    
    def mul(self):
        a=int(self.txt1.get())
        b=int(self.txt2.get())
        c=a*b
        self.txt3.delete(0,tk.END)
        self.txt3.insert(0,c)
    
    def div(self):
        a=int(self.txt1.get())
        b=int(self.txt2.get())
        c=a/b
        self.txt3.delete(0,tk.END)
        self.txt3.insert(0,c)
    
window=tk.Tk()
window.geometry('400x400')
ob=GUI(window)
window.mainloop()

