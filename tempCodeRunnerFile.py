import os
os.environ['TCL_LIBRARY'] = r'C:\Users\User\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\User\AppData\Local\Programs\Python\Python313\tcl\tk8.6'

import pymysql
from tkinter import *
from tkinter import messagebox

# MySQL connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345',
    'database': 'project'
}

def fetch_Student():
    """Fetch student emails and names from the database."""
    connection = None  # Initialize the connection variable
    try:
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT email, name FROM Student")
        student_data = cursor.fetchall()
        return {email: name for email, name in student_data}
    except pymysql.MySQLError as err:
        messagebox.showerror("Database Error", f"Error connecting to database: {err}")
        return {}
    finally:
        if connection:
            connection.close()

def login():
    """Handle login logic."""
    username = usernameEntry.get()
    password = passwordEntry.get()

    if username == '' or password == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif username in Student and password == '1234':
        messagebox.showinfo('Success', f'Welcome {Student[username]}')
        window.destroy()
        import ssms
    else:
        messagebox.showerror('Error', "Invalid credentials")

Student = fetch_Student()

window = Tk()
window.geometry('1280x700+0+0')
window.title('Login')
window.resizable(False, False)

# Login Frame
loginFrame = Frame(window)
loginFrame.place(x=400, y=150)

# Username Label and Entry
usernameLabel = Label(loginFrame, text='Username', compound=LEFT, font=('times new roman', 20, 'bold'))
usernameLabel.grid(row=1, column=0, pady=10, padx=20)
usernameEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='royalblue')
usernameEntry.grid(row=1, column=1, pady=10, padx=20)

# Password Label and Entry
passwordLabel = Label(loginFrame, text='Password', compound=LEFT, font=('times new roman', 20, 'bold'))
passwordLabel.grid(row=2, column=0, pady=10, padx=20)
passwordEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='red', show='*')  # Mask password
passwordEntry.grid(row=2, column=1, pady=10, padx=20)

# Login Button
loginButton = Button(
    loginFrame, text='Login', font=('times new roman', 14, 'bold'), width=15,
    fg='white', bg='cornflowerblue', activebackground='cornflowerblue',
    activeforeground='white', cursor='hand2', command=login
)
loginButton.grid(row=3, column=1, pady=10)

# Run the main event loop
window.mainloop()
