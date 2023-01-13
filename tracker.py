from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from pil import ImageTk, Image
import time
import psutil
import socket

#main window configuration

window1 = tk.Tk() #create a tkinter gui window frame
window1.title("network usage tracker")  #title given is "dictionary"
window1.geometry('1000*700')

#top label

start1=tk.label(text="Network usage\nTracker",font=("arial",55,"underline"),fg="magenta")
start1.place(x=150,y=10)

def start_fun():
    window1.destroy()
    
    #start button created
    startb = button(window1,text="Start",command=start_fun,font=("arial",25,),bg="orange",gf="blue",borderwidth=3,relief="raised")
    startb.place(x=130,y=590)
    
    
    #image on the main window
    path = "Images/images.png"
    
    #creates a tkinter-compatible photo image which can be used everywhere tkinter image object
    img1 = ImageTk.PhotoImage(Image.open(path))
    
    # the label widget is a stadar tkinter widget used to display a text or image on th screen
    panel =tk.Label(window1, image=img1)
    panel.place(x=320,y=200)
    
    #function created for exiting 
    def exit():
        if mbox.askokcancel("exit","Do you want to exit?"):
            window1.destroy()