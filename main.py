from tkinter import *

# Function to convert miles to km.
def converter():
    value = int(miles.get())
    km = round((value * 1.6), 1)
    km = str(km)
    output_km.config(text=str(km))



# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=150, width=390)
window.config(padx=20, pady=20)


# Labels
miles_label = Label(text="Miles", font=("Arial", 15, "normal"))
miles_label.grid(row=0, column=2)

is_equal_to_label = Label(text="is equal to", font=("Arial", 15, "normal"))
is_equal_to_label.grid(row=1, column=0)

km_label = Label(text="Km", font=("Arial", 15, "normal"))
km_label.grid(row=1, column=2)

output_km = Label(text="0", font=("Arial", 15, "normal"))
output_km.grid(row=1, column=1)

# Entry
miles = Entry(width=10)
miles.grid(row=0, column=1)


# Button
button = Button(text="Calculate", command=converter)
button.grid(row=3, column=1)






window.mainloop()