# import tkinter as tk
# window=tk.Tk()
# window.geometry('400x400')#windows size set gareko
# window.mainloop()


import tkinter as tk
window=tk.Tk()
window.geometry('400x400')#windows size set gareko
# window.minsize(width=400,height=400)# yo chai size set garne alternative way
window.title("This is title")#To add title
window.resizable(False,False)#size resize garna namilna lai

window.config(bg='Blue')#background color
window.mainloop()