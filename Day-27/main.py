# import tkinter
#
# window = tkinter.Tk()
# window.minsize(width=100,height=200)
# window.title("My Gui app")
# my_Lablel = tkinter.Label(text="hello")
# my_Lablel.pack()
#
#
#
#
#
# window.mainloop()


import tkinter
window = tkinter.Tk()
window.minsize(300,400)
window.title("hi hello")
window.minsize(300,100)

def button_clicked():
   miles = float(entry.get())
   km= round(miles*1.609)
   label_3.config(text=km)


entry = tkinter.Entry(width=13)
entry.grid(row=0,column=2)

label_1 = tkinter.Label(text="Miles")
label_1.grid(row=0,column=3)
label_2 = tkinter.Label(text="is equal to")
label_2.grid(row=1,column=1)
label_3 = tkinter.Label(text="0")
label_3.grid(row=1,column=2)
label_4 = tkinter.Label(text="km")
label_4.grid(row=1,column=3)
calculate_btn = tkinter.Button(text="Calculate",command=button_clicked)
calculate_btn.grid(row=2,column=2)











window.mainloop()

