from tkinter import *
from tkinter.ttk import *
from time import strftime

# Initialize the main window
root = Tk()
root.title("Clock")

# Define the time function to update the clock
def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)  # Update the time every 1000ms (1 second)

# Create a label to display the time
label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor="center")

# Call the time function
time()

# Start the Tkinter event loop
root.mainloop()
