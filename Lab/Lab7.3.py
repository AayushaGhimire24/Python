# create a GUI with a text box and two buttons (ok and clear). When ok button is clicked, display "you clicked the button" in the text box.when clear button is clicked, clear the text box.
import tkinter as tk
class GUI:
    def __init__(self,window):
        self.txt1=tk.Entry(window,width=30)
        self.txt1.place(x=20,y=20)
        self.btn1=tk.Button(window,text="Ok", command=self.show)
        self.btn1.place(x=20,y=50)

        self.btn2=tk.Button(window,text="Clear",command=self.clear)
        self.btn2.place(x=50,y=50)
    def show(self):
        self.txt1.delete(0,tk.END)
        self.txt1.insert(0,"You clicked the button")
    
    def clear(self):
        self.txt1.delete(0,tk.END)
window=tk.Tk()
window.geometry('400x400')
ob=GUI(window)
window.mainloop()


