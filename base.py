from tkinter import *
from gtts import gTTS
import os
unit_dict = {
    "cm" : 0.01,
    "m" : 1.0,
    "km": 1000.0,
    "feet": 0.3048,
    "miles": 1609.344,
    "inches": 0.0254,
    "grams" : 1.0,
    "kg" : 1000.0,
    "tonnes" : 1000000.0,
    "pounds" : 453.59,
    "sq. m" : 1.0,
    "sq. km": 1000000.0,
    "hectare" : 10000.0,
    "acre": 4046.856,
    "sq. mile" : 2590000.0,
    "sq. foot" : 0.0929,
    "cu. cm" : 0.001,
    "Litre" : 1.0,
    "ml" : 0.001,
    "gallon": 3.78
}

ls = ["cm", "m", "km", "feet", "miles", "inches",]
ws = ["kg", "grams", "quintals", "tonnes", "pounds",]
ts = ["Celsius", "Fahrenheit"]
areas = ["sq. m", "sq. km","hectare", "acre", "sq. mile", "sq. foot"]
vs = ["cu. cm", "Litre", "ml", "gallon"]

# Options for drop-down menu
OPTIONS = ["select units",
            "cm",
            "m",
            "km",
            "feet",
            "miles",
            "inches",
            "kg",
            "grams",
            "tonnes",
            "pounds",
            "Celsius",
            "Fahrenheit",
            "sq. m",
            "sq. km",
            "hectare",
            "acre",
            "sq. mile",
            "sq. foot",
            "cu. cm",
            "Litre",
            "ml",
            "gallon"]
root = Tk()
root.geometry("800x800")
root.title("Unit Converter")
root['bg'] = '#f44f36'
def ok():
    inp = float(fromentry.get())
    inp_unit = from_optionmenu.get()
    out_unit = to_optionmenu.get()

    cal_c_error_check = [inp_unit in ls and out_unit in ls,
    inp_unit in ws and out_unit in ws,
    inp_unit in ts and out_unit in ts,
    inp_unit in areas and out_unit in areas,
    inp_unit in vs and out_unit in vs]

    if any(cal_c_error_check): # If both the units are of same type, do the conversion
        if inp_unit == "Celsius" and out_unit == "Fahrenheit":
            to_entry.delete(0, END)
            to_entry.insert(0, (inp * 1.8) + 32)
        elif inp_unit == "Fahrenheit" and out_unit == "Celsius":
            to_entry.delete(0, END)
            to_entry.insert(0, (inp - 32) * (5/9))
        else:
            to_entry.delete(0, END)
            to_entry.insert(0, round(inp * unit_dict[inp_unit]/unit_dict[out_unit], 5))

    else: # Display error if units are of different types
        to_entry.delete(0, END)
        to_entry.insert(0, "these selection are wrong")
    temp1=from_optionmenu.get()
    temp2=to_optionmenu.get()
    #c=fromentry.get()
    #d=to_entry.get()
    t= fromentry.get() + " " + temp1+ " " + "is "+to_entry.get() + " "+ temp2 + "\n"
    password_file=open("basefile.txt","a")
    password_file.write(t)
    password_file.close()
    fh=open("basefile.txt","r" )
    mytext=fh.read().replace("\n","")
    language ="en"
    output=gTTS(text=mytext,lang=language,slow=False)
    output.save("output_base.mp3")
    fh.close()
    os.system("output_base.mp3")
#save to file
'''def click_to_save_to_play():
    temp1=from_optionmenu.get()
    temp2=to_optionmenu.get()
    #c=fromentry.get()
    #d=to_entry.get()
    t= fromentry.get() + " " + temp1+ " " + "is "+to_entry.get() + " "+ temp2 + "\n"
    password_file=open("basefile.txt","a")
    password_file.write(t)
    password_file.close()
    fh=open("basefile.txt","r" )
    mytext=fh.read().replace("\n","")
    language ="en"
    output=gTTS(text=mytext,lang=language,slow=False)
    output.save("output_base.mp3")
    fh.close()
    os.system("output_base.mp3")'''

f_label=Label(root,text="NIS unit converter",font="Algerian 30 ",bg="#51afc4")
f_label.grid(row=0,column=0)

frame1=Frame(root,bg="#f44f36")
frame1.grid(pady=20)

fromlabel = Label(frame1, text = "from",font = "Calibri 22 bold",bg="#f44f36")
fromlabel.grid(row = 1, column = 0,padx = 15, pady = 15)

fromentry = Entry(frame1,  font = "bold")
fromentry.grid(row = 1, column = 1)
#input variable
from_optionmenu = StringVar()
from_optionmenu.set(OPTIONS[0])
#option for input
from_menu = OptionMenu(frame1, from_optionmenu, *OPTIONS)
from_menu.grid(row = 1, column = 2, padx = 15, pady = 15)
from_menu.config(font = "Arial 10 bold")

to_label = Label(frame1, text = "to",font = "Calibri 22 bold",bg="#f44f36")
to_label.grid(row = 3, column = 0, padx = 15, pady = 15)

to_entry = Entry(frame1, font = "bold")
to_entry.grid(row = 3, column = 1)
#output variable
to_optionmenu = StringVar()
to_optionmenu.set(OPTIONS[0])
outputmenu_list = OptionMenu(frame1, to_optionmenu, *OPTIONS)
outputmenu_list.grid(row = 3, column = 2, padx = 15, pady = 15)
outputmenu_list.config(font = "Arial 10 bold")

okbtn = Button(root, text = "OK", command = ok, padx = 30, pady = 2,font = "Calibri 18 bold",bg="#6f4cb5", width = 10)
okbtn.grid(row = 4, column = 0, padx = 10, pady = 10, columnspan = 2)
#savebtn = Button(root, text = "play", command = click_to_save_to_play, padx = 80, pady = 2,font = "Calibri 18 bold",bg="#6f4cb5")
#savebtn.grid(row = 4, column = 2, pady=50,columnspan = 2)

root.mainloop()
