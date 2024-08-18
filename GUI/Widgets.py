# Widgets->Components that are placed in a windows frame
# Create a GUI with a textbox and a button when button is clicked, display "You clicked the button" in the textbox
import tkinter as tk
class GUI:
    def __init__(self,window):
        self.txt1=tk.Entry(window,width=30)
        self.txt1.place(x=20,y=20)
        self.btn1=tk.Button(window,text="Click",command=self.show)#command chai callback function c=sanga button lai register garna lai lekheko
        self.btn1.place(x=20,y=50)
    def show(self):#Button ma click garepaxi text aaune banaune(Callback function)
        self.txt1.insert(0,"You clicked the button")
window=tk.Tk()
window.geometry('400x400')
ob=GUI(window)
window.mainloop()
