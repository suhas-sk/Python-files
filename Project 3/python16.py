import tkinter as tk
from tkinter import messagebox
# creating a window
root = tk.Tk()
root.geometry("400x400")
root.title("My First Program")


'''
# adding Canvas for drawing
C = tk.Canvas(root, height=250, width=300)

# drawwing an arc on canvas
coord = 10, 20, 150, 200
arc = C.create_arc(coord, start=10, extent=340, fill='blue')
C.pack()
'''
def hello():
    print("Button is pressed")
    var = tk.StringVar()
    label = tk.Label(root,textvariable=var, relief=tk.RAISED, foreground='white', background='black', height=2, width=20,)
    var.set("Name")
    label.pack()

    entry = tk.Entry(foreground="blue", background="white", width=20)
    name = entry.get()
    print(name)
    entry.pack()

    text_box = tk.Text()
    text_box.pack()

    res = tk.messagebox.askquestion('Alert', 'Do you want to continue ??') #returns yes or no
    if res == "yes":
        res1 = tk.messagebox.askyesno('Alert', 'Do you really want to continue ??') # returns True or False
        print(res1)
        if res1 == True:
            res2 = tk.messagebox.askokcancel('Alert', 'Are you Sure??') #returns True or False
            print(res2)
            if res2 == True:
                res3 = tk.messagebox.askretrycancel('Hello !!!', 'This was a Prank') #returns True or False
                print(res3)


# adding button to the window
btn = tk.Button(root, text="Button",background="yellow",foreground="blue", command=hello)
btn.pack()

# keeping the window in loop
root.mainloop()