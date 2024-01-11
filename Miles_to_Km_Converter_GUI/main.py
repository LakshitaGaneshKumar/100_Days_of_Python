from tkinter import *

RESULT_FONT = ("georgia", 16, "bold")
FONT = ("georgia", 12)

def mi_to_km():
    miles = float(input_mi.get())
    km = miles * 1.609
    label_km.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)

input_mi = Entry(width=10, textvariable="miles")
label_mi = Label(text="Miles", font=FONT)
label_equal = Label(text="is equal to", font=FONT)
label_km = Label(text="0", font=RESULT_FONT)
label_km_text = Label(text="Km", font=FONT)
button_calc = Button(text="Calculate", command=mi_to_km)

input_mi.pack()
label_mi.pack()
label_equal.pack()
label_km.pack()
label_km_text.pack()
button_calc.pack()

# input_mi.grid(row=0, column=1)
# label_mi.grid(row=0, column=2)  
# label_equal.grid(row=1, column=0)
# label_km.grid(row=1, column=1)
# label_km_text.grid(row=1, column=2)
# button_calc.grid(row=2, column=1)

window.mainloop()
