# Calculator using Tkinter
# Using Lamda function

from tkinter import *
expression = ""

# Function to update expression
# in the text box entry

def press(num):
    #point out the global expression
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


# Function to evalute the final answer
def equalpress():
    try:
        global expression
        total = str(eval(expression))

        equation.set(total)

    except:
        equation.set("error")
        expression = ""

# Function to clear the contents of the entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# Creating a GUI window

root = Tk()
root.title('Calculator')
root.geometry("310x320")

equation  = StringVar()

# creating a text box entry for showing the expression
expression_field = Entry(root, textvariable = equation)

# placing the widgets in table format using grid method
expression_field.grid(columnspan=4, ipadx=90)

# creating buttons
B1 = Button(text='1',foreground='white', background='black',height=1,width=6,command=lambda : press(1))
B1.grid(row=2, column=0)

B2 = Button(text='2',foreground='white', background='black',height=1,width=6,command=lambda : press(2))
B2.grid(row=2, column=1)

B3 = Button(text='3',foreground='white', background='black',height=1,width=6, command=lambda : press(3))
B3.grid(row=2, column=2)

B4 = Button(text='4',foreground='white', background='black',height=1,width=6,command=lambda : press(4))
B4.grid(row=3, column=0)

B5 = Button(text='5',foreground='white', background='black',height=1,width=6,command=lambda : press(5))
B5.grid(row=3, column=1)

B6 = Button(text='6',foreground='white', background='black',height=1,width=6,command=lambda : press(6))
B6.grid(row=3, column=2)

B7 = Button(text='7',foreground='white', background='black',height=1,width=6,command=lambda : press(7))
B7.grid(row=4, column=0)

B8 = Button(text='8',foreground='white', background='black',height=1,width=6,command=lambda : press(8))
B8.grid(row=4, column=1)

B9 = Button(text='9',foreground='white', background='black',height=1,width=6,command=lambda : press(9))
B9.grid(row=4, column=2)

B0 = Button(text='0',foreground='white', background='black',height=1,width=6,command=lambda : press(0))
B0.grid(row=5, column=0)

plus = Button(text='+',foreground='white', background='black',height=1,width=6,command=lambda : press('+'))
plus.grid(row=2, column=3)

minus = Button(text='-',foreground='white', background='black',height=1,width=6,command=lambda : press('-'))
minus.grid(row=3, column=3)

div = Button(text='/',foreground='white', background='black',height=1,width=6,command=lambda : press('/'))
div.grid(row=4, column=3)

multi = Button(text='*',foreground='white', background='black',height=1,width=6,command=lambda : press('*'))
multi.grid(row=5, column=3)

decimal = Button(text='.',foreground='white', background='black',height=1,width=6,command=lambda : press('.'))
decimal.grid(row=5, column=1)

clear1 = Button(text='X',foreground='white', background='black',height=1,width=6,command=lambda : clear())
clear1.grid(row=5, column=2)

equal = Button(text='=',foreground='white', background='black',height=1,width=6,command=lambda : equalpress())
equal.grid(row=6, column=3)

root.mainloop()


