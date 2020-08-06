
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo

def save():
    f_name = entry.get()
    l_name = entry1.get()
    gender = entry2.get()
    age = entry3.get()

    with open("File.csv", 'w') as f:

        headers = 'First Name, Last Name, Gender, Age\n'
        f.write(headers)
        data = f_name + ',' + l_name + ',' + gender + ',' + age
        f.write(data)

    showinfo("Saved", "Your entry has been Saved")


def clear():
    entry.delete(0, tk.END)
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)

#Creating GUI window
root = tk.Tk()
root.title('Registeration workbook')
root.geometry("300x200")

#Creating Labels
label = tk.Label(root,text="First Name")
label.grid(row=0,column=0,padx=5,pady=5)

label1 = tk.Label(root,text="Last Name")
label1.grid(row=1,column=0,padx=5,pady=5)

label2 = tk.Label(root,text="Gender")
label2.grid(row=2,column=0,padx=5,pady=5)

label3 = tk.Label(root, text="Age")
label3.grid(row=3,column=0,padx=5,pady=5)

#Creating entry widgets
entry = tk.Entry(root,width=25)
entry.grid(row=0, column=1, padx=5, pady=5)

entry1 = tk.Entry(root,width=25)
entry1.grid(row=1,column=1,padx=5,pady=5)

entry2 = tk.Entry(root,width=25)
entry2.grid(row=2,column=1,padx=5,pady=5)

entry3 = tk.Entry(root,width=25)
entry3.grid(row=3,column=1,padx=5,pady=5)

#Creating Button
button = tk.Button(root,text="Register",command=save)
button.grid(row=4,column=0,padx=10,pady=10)

button1 = tk.Button(root,text="Clear",command=clear)
button1.grid(row=4,column=1,padx=10,pady=10)

root.mainloop()










