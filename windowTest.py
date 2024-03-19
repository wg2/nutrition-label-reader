from tkinter import *

window = Tk()
window.title("Window Test")


welcome = Label(window, text="Welcome to the window test!")
welcome.grid(row=0, column=0, columnspan=3)

def go():
    rule_window = Toplevel(window)
    rule_window.title("The Rules")
    the_rules = Label(rule_window, text="Here are the rules...", foreground="black")
    the_rules.grid(row=0, column=0, columnspan=3)


thing = Button(window, text="Click me!", command=go)
thing.grid(row=1, column=0, columnspan=1)
window.mainloop()