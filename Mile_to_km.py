
from cgitb import text
import tkinter
from turtle import width


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(300,200)

entery_box= tkinter.Entry()
entery_box.place(x="80", y="20")
print(entery_box)

label1 = tkinter.Label(text="Miles")
label1.place(x="220" , y="20")

label2 = tkinter.Label(text="Km")
label2.place(x="220" , y="50")


output_box = tkinter.Label(0)
output_box.place(x="80", y="50")

def cal():
  output = float (entery_box.get()) * 1.609344
  output_box.config(text=round(output))


calculate = tkinter.Button(text="Calculate" , command=cal)
calculate.place(x="110", y="80")



window.mainloop()