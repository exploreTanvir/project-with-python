import time
from tkinter import*
root =Tk()
root.configure(background="black")
def start():
    text=time.strftime("%H:%M:%S")
    Label.config(text=text)
    Label.after(200,start)
Label=Label(root,font=("Arial",100),fg="red",bg="black")
Label.grid(row=0,column=1)
print("Done")
start()
root.mainloop()
