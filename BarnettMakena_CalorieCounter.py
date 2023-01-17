# Program: Lesson 2 Calorie Counter
# Programmer: Makena Barnett
# Date: 1/16/2023
# Purpose: The purpose of this program is to demonstrate the use of GUIs in Python
import tkinter as tk
def calc_cals():
    #capture input data from the screen
    g_carbs = int(ent_carbs.get())
    g_fats = int(ent_fats.get())
    g_proteins = int(ent_proteins.get())
    i_cal = g_carbs * 4 + g_fats * 9 + g_proteins * 4
    lbl_item_cals["text"] =f"{i_cal}"
    tot_cals= int(lbl_tot_cals["text"])
    tot_items = int(lbl_tot_items["text"])
    tot_cals += i_cal
    tot_items += 1                    
    lbl_tot_cals["text"] =f"{tot_cals}"
    lbl_tot_items["text"]= f"{tot_items}"
window = tk.Tk()
window.title("Simple Calorie Counter")
frame1_bg= "LightBlue1"
frame1 = tk.Frame (master=window, width=400, height=400, bg=frame1_bg)
frame1.pack(fill=tk.Y, side=tk.LEFT, expand=True)
frame2 = tk.Frame (master=window, width=200, bg="DarkSeaGreen1")
frame2.pack(fill=tk.Y, side=tk.LEFT, expand=True)
frame3 = tk.Frame (master=window, width=50,bg="thistle2")
frame3.pack(fill=tk.Y, side=tk.LEFT, expand=True)
#Frame 1 Layout
label = tk.Label(master=frame1,
                 text="Makena's Calorie Counter Program",
                 bg="plum1",
                 font=("Time", "18", "italic")) 
label.place(x=20, y=0)
# Data Input Area
label= tk.Label (master=frame1, text="Please enter item name:", bg="DarkSeaGreen1")
label.place(x=0, y=40)
ent_name = tk.Entry(master=frame1, width= 40)
ent_name.place(x=150, y=40)

label= tk.Label(master=frame1, text="Please enter grams of fats:", bg="DarkSeaGreen1")
label.place(x=0, y=80)
ent_fats = tk.Entry (master= frame1, width= 10)
ent_fats.place(x=170, y= 80)

label= tk.Label(master=frame1, text="Please enter grams of carbs:", bg="DarkSeaGreen1")
label.place(x=0, y=120)
ent_carbs = tk.Entry (master= frame1, width= 10)
ent_carbs.place(x=170, y= 120)
label= tk.Label(master=frame1, text="Please enter grams of proteins:", bg="DarkSeaGreen1")
label.place(x=0, y=160)
ent_proteins = tk.Entry (master= frame1, width= 10)
ent_proteins.place(x=170, y= 160)
# button
button1 = tk.Button(master=frame1,
                    text="Submit!", 
                    bg="plum1",
                    width=60,
                    command=calc_cals)
button1.place(x=0, y= 200)
#Frame 2
label = tk.Label(master=frame2, text="Totals", bg="thistle2",
                 font=("Times", "18", "bold"))
label.place(x=10, y=20)
#item calories
label = tk.Label(master=frame2, text="Item Calories", bg="thistle2")
label.place(x=10,y=70)
lbl_item_cals = tk.Label(master=frame2, text="0", width=10)
lbl_item_cals.place(x=100, y=70)
#Total Calories
label = tk.Label(master=frame2, text="Total Calories", bg="thistle2")
label.place(x=10,y=100)
lbl_tot_cals = tk.Label(master=frame2, text="0", width=10)
lbl_tot_cals.place(x=100, y=100)
#Total Items
label = tk.Label(master=frame2, text="Total Items", bg="thistle2")
label.place(x=10,y=130)
lbl_tot_items = tk.Label(master=frame2, text="0", width=10)
lbl_tot_items.place(x=100, y=130)
window.mainloop()
