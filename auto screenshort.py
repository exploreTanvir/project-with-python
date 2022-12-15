import pyautogui
import tkinter as tk
from tkinter.filedialog import*

root=tk.Tk()
root.title('screenshot')

canvas=tk.Canvas(root,width=300, heigh=300)
canvas.pack()
def takeScreenShot():
    myScreenShot=pyautogui.screenshot()
    save_path=asksaveasfilename()
    myScreenShot.save(save_path+"_screenshot.png")

myButton=tk.Button(text="Take ScreenShot",command=takeScreenShot,font=5)
canvas.create_window(150,150,window=myButton)

root.mainloop()
