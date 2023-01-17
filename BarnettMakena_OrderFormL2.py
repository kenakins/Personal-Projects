# Program: Lesson 2 Oder Form
# Programmer: Makena Barnett
# Date: 1/16/2023
# Purpose: The purpose of this lab is to design a functional Graphical User Interface in Python using Tkinter. 

from tkinter import *
import tkinter as tk
def clear_entries():
    ent_iprice.delete(0,END)
    ent_name.delete(0,END)
    ent_qty.delete(0,END)
    lbl_tot_iprice ["text"] = "0"
    lbl_tot_price["text"] ="0"
    lbl_tot_items["text"]= "0"
def calc_price():
    #capture input data from the screen
    g_qty = int(ent_qty.get())
    g_iprice = int(ent_iprice.get())
    i_price = g_qty * g_iprice 
    tot_price= int(lbl_tot_price["text"])
    tot_items = int(lbl_tot_items["text"])
    tot_price += i_price
    tot_items += 1
    lbl_tot_iprice ["text"] =f"{i_price}"
    lbl_tot_price["text"] =f"{tot_price}"
    lbl_tot_items["text"]= f"{tot_items}"

#Formatting
window = tk.Tk()
window.title("Simple Order Form")
frame1_bg= "LightBlue1"
frame1 = tk.Frame (master=window, width=400, height=400, bg=frame1_bg)
frame1.pack(fill=tk.Y, side=tk.LEFT, expand=True)
frame2 = tk.Frame (master=window, width=200, bg="DarkSeaGreen1")
frame2.pack(fill=tk.Y, side=tk.LEFT, expand=True)
frame3 = tk.Frame (master=window, width=50,bg="thistle2")
frame3.pack(fill=tk.Y, side=tk.LEFT, expand=True)

#Frame 1 Layout
label = tk.Label(master=frame1,
                 text="Makena's Order Form",
                 bg="plum1",
                 font=("Time", "18", "italic")) 
label.place(x=20, y=0)

#Data Input Area
label= tk.Label (master=frame1, text="Please enter item name:", bg="DarkSeaGreen1")
label.place(x=0, y=40)
ent_name = tk.Entry(master=frame1, width= 40)
ent_name.place(x=150, y=40)
label= tk.Label(master=frame1, text="Please enter price:", bg="DarkSeaGreen1")
label.place(x=0, y=80)
ent_iprice = tk.Entry (master= frame1, width= 10)
ent_iprice.place(x=170, y= 80)
label= tk.Label(master=frame1, text="Please enter item quantity:", bg="DarkSeaGreen1")
label.place(x=0, y=120)
ent_qty = tk.Entry (master= frame1, width= 10)
ent_qty.place(x=170, y= 120)

#Buttons
button1 = tk.Button(master=frame1,
                    text="Submit!", 
                    bg="plum1",
                    width=60,
                    command= calc_price)
button1.place(x=0, y= 200)
button2 = tk.Button (master=frame1,
                     text="Reset",
                     width =60,
                     command= clear_entries)
button2.place(x=0,y=230)

#Frame 2
label = tk.Label(master=frame2, text="Total", bg="thistle2",
                 font=("Times", "18", "bold"))
label.place(x=10, y=20)

#Total Items
label = tk.Label(master=frame2, text="Total Items", bg="thistle2")
label.place (x=10, y=120)
lbl_tot_items = tk.Label(master=frame2, text="0", width=10)
lbl_tot_items.place(x=100, y=120)

#Item price
label = tk.Label(master=frame2, text="Item  Price", bg="thistle2")
label.place(x=10,y=70)

lbl_tot_iprice = tk.Label(master=frame2, text="0", width=10)
lbl_tot_iprice.place(x=100, y=70)

#Total Order Price
label = tk.Label(master=frame2, text="Total Order Price", bg="thistle2")
label.place(x=10,y=100)
lbl_tot_price = tk.Label(master=frame2, text="0", width=10)
lbl_tot_price.place(x=100, y=100)

window.mainloop()

