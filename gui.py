import tkinter as tk
from click import ClickException
import requests
from tkinter import Entry, ttk
def stocker():
    topic=topic.get()
    num=num.get()
root=tk.Tk()
root.resizable('true','true')
root.geometry("500x100")
root.title("Image Stoker")      
l1=tk.Label(root,text="What you want to search")
l1.grid(row=1)
topic=tk.Entry(root)
topic.grid(row=1,column=1)

l2=tk.Label(root,text="Number of images you want")
l2.grid(row=2)
num=tk.Entry(root)
num.grid(row=2,column=1)
btn=tk.Button(root,text="Search",command=stocker)
btn.grid(row=4,column=1)

pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=200
)
# place the progressbar
pb.grid(column=1, row=6, columnspan=1)

root.mainloop()