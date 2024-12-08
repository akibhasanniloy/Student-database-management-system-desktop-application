import os
os.environ['TCL_LIBRARY'] = r'C:\Users\User\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\User\AppData\Local\Programs\Python\Python313\tcl\tk8.6'

from tkinter import *
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='admin' and passwordEntry.get()=='12345':
        messagebox.showinfo('Success', 'Welcome Admin')
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error',"Please enter correct credentials")

window=Tk()

window.geometry('800x400+0+0')
window.title('Login')

window.resizable(False, False)

# loginFrame = Frame(window, bg='white')
loginFrame = Frame(window)
loginFrame.place(x=100, y=50)

# User Name
usernameLabel=Label(loginFrame, text='Username', compound=LEFT, font=('times new roman', 20, 'bold'))
usernameLabel.grid(row=1, column=0, pady=10, padx=20)
usernameEntry= Entry(loginFrame,font=('times new roman', 20, 'bold'),bd=5, fg='royalblue')
usernameEntry.grid(row=1, column=1, pady=10, padx=20)

# Password
passwordLabel=Label(loginFrame, text='Password', compound=LEFT, font=('times new roman', 20, 'bold'))
passwordLabel.grid(row=2, column=0, pady=10, padx=20)
passwordEntry= Entry(loginFrame,font=('times new roman', 20, 'bold'),bd=5, fg='red')
passwordEntry.grid(row=2, column=1, pady=10, padx=20)

# Login Button
loginButton= Button(loginFrame, text='Login', font=('times new roman', 14,'bold'), width=15, fg='white', bg='cornflowerblue', activebackground='cornflowerblue', activeforeground='white', cursor='hand2', command=login)
loginButton.grid(row=3, column=1, pady=10)

window.mainloop()