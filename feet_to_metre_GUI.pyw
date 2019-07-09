from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

root = Tk()
root.title("Feet to Metres Converter")

mainFrame = ttk.Frame(root, padding="3 3 12 12")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
mainFrame.columnconfigure(0, weight=1)
mainFrame.rowconfigure(0, weight=1)

def showAbout():
    showinfo("Converter", "This was created by Sanjay Bhat.")

def calculate(*args):
    value = float(feet.get())
    metres.set((0.3048 * value * 10000.0 + 0.5)/ 10000.0)

menubar = Menu(root)
root.config(menu=menubar)

menuAbout = Menu(menubar, tearoff=0)
menuAbout.add_command(label="About Converter", command=showAbout)
menubar.add_cascade(label="Credits", menu = menuAbout)

feet = StringVar()
metres = StringVar()


feet_entry = ttk.Entry(mainFrame, width = 7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainFrame,text="Feet                  ").grid(column = 3, row=1)
ttk.Label(mainFrame,text="is equivalent To").grid(column = 1, row=2, sticky=(W, E))
ttk.Label(mainFrame, textvariable = metres).grid(column=2, row=2, sticky=(W,E))
ttk.Label(mainFrame,text="Metres").grid(column = 3, row = 2, sticky=W)
ttk.Button(mainFrame, text="Calculate", command=calculate).grid(column=3, row = 3, sticky=W)

for child in mainFrame.winfo_children():    child.grid_configure(padx =5, pady= 5)

#root.withdraw()
feet_entry.focus()
root.bind('<Return>', calculate)
root.mainloop()
