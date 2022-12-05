# import tkinter as tk
from tkinter import *
import time

with open("lb.txt") as f:
    content_list = f.readlines()

content_list = [x.strip() for x in content_list]
lb=[]
lbb=[]
for i in content_list:
    l=list(map(str,i.split(" ")))
    lb.append(l)


# scores = Tk() 
scores = Tk()
scores.bind("<Escape>", lambda e: scores.destroy())
scores.configure(width=1920, height=1080)
#scores.attributes("-fullscreen", True)
displayFrame = Frame(scores)
displayFrame.configure(bg="#651A84",) 
displayFrame.grid(row=2, column=1, rowspan=5, padx=960-650, pady=540-400)
# displayFrame.pack(anchor="w")

def show():
    global displayFrame
    tempList = lb
    #tempList.sort(key=lambda e: e[1], reverse=True)
    Label(displayFrame, text="         HIGH SCORES", font=("Arial",50), fg="white", bg="#651A84").grid(row=0, column=0)
    Label(displayFrame, text="Sl.No   Name\t\t\t", font=("Arial",20), fg="white", bg="#651A84").grid(row=1, column=0, padx=10, pady=10)
    Label(displayFrame, text="Score\t", font=("Arial",20), fg="white", bg="#651A84").grid(row=1, column=1, padx=10, pady=10)
    for i, (name, score) in enumerate(tempList[:5], start=1):
        # listBox.insert("", "end", values=(i, name, score))
        Label(displayFrame, text=f"{i:>6}.       \t{name[0:10]}\t", font=("Arial", 40,), fg="white", bg="#651A84").grid(row=i+1, column=0, sticky="w")
        Label(displayFrame, text=f"{score}", font=("Arial", 40), fg="white", bg="#651A84").grid(row=i+1, column=1, sticky="w", padx=10)
        displayFrame.lift() 


scores.geometry("1920x1080")
scores.configure(bg="#651A84")
# create Treeview with 3 columns
cols = ('Position', 'Name', 'Score')
# listBox = tTreeview(scores, columns=cols, show='headings')
# set column headings
# for col in cols:
#     listBox.heading(col, text=col)    
# listBox.grid(row=1, column=0, columnspan=2)

show()
closeButton = Button(scores, text="Close", width=15, command=exit).grid(row=10, column=1)
while 1>0:
    with open("lb.txt") as f:
        content_list = f.readlines()
        content_list = [x.strip() for x in content_list]
        lb=[]
        lbb=[]
        for i in content_list:
            l=list(map(str,i.split(" ")))
            lb.append(l)
        
        tempList = lb   
        #tempList.sort(key=lambda e: e[1], reverse=True)
        Label(displayFrame, text="Sl.No   Name\t\t\t", font=("Arial",20), fg="white", bg="#651A84").grid(row=1, column=0, padx=10, pady=10)
        Label(displayFrame, text="Score\t", font=("Arial",20), fg="white", bg="#651A84").grid(row=1, column=1, padx=10, pady=10)
        for i, (name, score) in enumerate(tempList[:5], start=1):
            # listBox.insert("", "end", values=(i, name, score))
            Label(displayFrame, text=f"{i:>6}.       \t{name[0:10]}\t", font=("Arial", 40,), fg="white", bg="#651A84").grid(row=i+1, column=0, sticky="w")
            Label(displayFrame, text=f"{score}", font=("Arial", 40), fg="white", bg="#651A84").grid(row=i+1, column=1, sticky="w", padx=10)
            displayFrame.configure(bg="#651A84",)
            displayFrame.lift()
    closeButton = Button(scores, text="Close", width=15, command=scores.destroy).grid(row=10, column=1)
    scores.bind("<Escape>", lambda e: scores.destroy())
    time.sleep(5)


    scores.update()