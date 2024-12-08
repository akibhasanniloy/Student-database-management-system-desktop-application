import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql

os.environ["TCL_LIBRARY"] = r"C:\Users\User\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ["TK_LIBRARY"] = r"C:\Users\User\AppData\Local\Programs\Python\Python313\tcl\tk8.6"

def connect_db():
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="12345",
            database="project",
        )
        return connection
    except Exception as e:
        messagebox.showerror("Database Error", f"Failed to connect to database: {str(e)}")
        exit()

logged_in_email = None

# Function to open the main application window
def open_main_window():
    global logged_in_email

    root = Tk()
    root.title("Student Information System")
    root.geometry("900x600")
    root.resizable(False, False)

    con = connect_db()
    mycursor = con.cursor()

    columns = ("Std_Id", "Name", "Department", "Intake", "Address", "Email", "Phone_No")
    student_table = ttk.Treeview(root, columns=columns, show="headings")
    for col in columns:
        student_table.heading(col, text=col)
        student_table.column(col, width=120)
    student_table.pack(fill=BOTH, expand=1)

    def fetch_student():
        try:
            if not logged_in_email:
                messagebox.showerror("Error", "No logged-in email found.")
                return            
            print(f"Searching for student with email: {logged_in_email}")

            query_student = "SELECT * FROM Student WHERE LOWER(Email) = LOWER(%s)"
            mycursor.execute(query_student, (logged_in_email.strip(),))
            student_data = mycursor.fetchone()

            student_table.delete(*student_table.get_children())

            if student_data:
                student_table.insert("", END, values=student_data)
            else:
                messagebox.showinfo("No Record", "No student found with the logged-in email.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch student information: {str(e)}")
    fetch_student()
    root.mainloop()

# Function to handle login
def login():
    global logged_in_email

    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if email and password == "1234":
        logged_in_email = email
        messagebox.showinfo("Login Successful", f"Welcome, {logged_in_email}")
        login_window.destroy()
        open_main_window()
    else:
        messagebox.showerror("Login Failed", "Invalid email or password.")

# Function to toggle password visibility
def toggle_password_visibility():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_password_btn.config(text="Hide Password")
    else:
        password_entry.config(show="*")
        show_password_btn.config(text="Show Password")

# Login Window
login_window = Tk()
login_window.title("Login")
login_window.geometry("400x300")
login_window.resizable(False, False)

Label(login_window, text="Login Page", font=("Arial", 16)).pack(pady=20)

# Email Label and Entry
Label(login_window, text="Email:").pack(pady=5)
email_entry = Entry(login_window, width=30)
email_entry.pack(pady=5)

# Password Label and Entry
Label(login_window, text="Password:").pack(pady=5)
password_entry = Entry(login_window, width=30, show="*")
password_entry.pack(pady=5)

show_password_btn = Button(login_window, text="Show Password", command=toggle_password_visibility)
show_password_btn.pack(pady=10)

Button(login_window, text="Login", command=login).pack(pady=20)

login_window.mainloop()
