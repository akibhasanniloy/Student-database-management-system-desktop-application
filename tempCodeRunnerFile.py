import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Database connection
con = pymysql.connect(host='localhost', user='root', password='12345', database='project')
mycursor = con.cursor()

# Function for exiting
def iexit():
    result = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if result:
        root.destroy()

# Function to update specific fields (name, address, email, phone_no)
def update_student(student_id):
    def update_data():
        if nameEntry.get() == '' or addressEntry.get() == '' or emailEntry.get() == '' or phone_noEntry.get() == '':
            messagebox.showerror('Error', 'All fields must be filled', parent=update_window)
        else:
            try:
                query = "UPDATE Student SET name=%s, address=%s, email=%s, phone_no=%s WHERE Std_Id=%s"
                mycursor.execute(query, (nameEntry.get(), addressEntry.get(), emailEntry.get(), int(phone_noEntry.get()), student_id))
                con.commit()
                messagebox.showinfo('Success', 'Student information updated successfully')
                update_window.destroy()
                fetch_data()  # Refresh table to show updated record
            except Exception as e:
                con.rollback()
                messagebox.showerror('Error', f"Failed to update student: {str(e)}", parent=update_window)

    # New window for updating student data
    update_window = Toplevel()
    update_window.title('Update Student')
    update_window.grab_set()
    update_window.resizable(False, False)

    # Update student form fields
    Label(update_window, text='Name', font=('times new roman', 15, 'bold')).grid(row=0, column=0, padx=10, pady=5)
    nameEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=0, column=1, padx=10, pady=5)

    Label(update_window, text='Address', font=('times new roman', 15, 'bold')).grid(row=1, column=0, padx=10, pady=5)
    addressEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=1, column=1, padx=10, pady=5)

    Label(update_window, text='Email', font=('times new roman', 15, 'bold')).grid(row=2, column=0, padx=10, pady=5)
    emailEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=2, column=1, padx=10, pady=5)

    Label(update_window, text='Phone No', font=('times new roman', 15, 'bold')).grid(row=3, column=0, padx=10, pady=5)
    phone_noEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    phone_noEntry.grid(row=3, column=1, padx=10, pady=5)

    # Button to submit data
    update_button = Button(update_window, text='Update', command=update_data)
    update_button.grid(row=4, column=1, pady=10)

# Function to fetch data and display in the table
def fetch_data():
    mycursor.execute("SELECT * FROM Student")
    rows = mycursor.fetchall()
    if len(rows) != 0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('', END, values=row)

# Main student panel
root = Tk()
root.geometry('1280x700+0+0')
root.title('Student Panel')

# Student table
table_frame = Frame(root, bd=4, relief=RIDGE, bg="crimson")
table_frame.place(x=20, y=100, width=1240, height=560)

scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
scroll_y = Scrollbar(table_frame, orient=VERTICAL)
student_table = ttk.Treeview(table_frame, columns=("Std_Id", "name", "department", "intake", "address", "email", "roll_no", "phone_no"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)

student_table.heading("Std_Id", text="Student ID")
student_table.heading("name", text="Name")
student_table.heading("department", text="Department")
student_table.heading("intake", text="Intake")
student_table.heading("address", text="Address")
student_table.heading("email", text="Email")
student_table.heading("roll_no", text="Roll No")
student_table.heading("phone_no", text="Phone No")

student_table['show'] = 'headings'

student_table.column("Std_Id", width=100)
student_table.column("name", width=200)
student_table.column("department", width=150)
student_table.column("intake", width=100)
student_table.column("address", width=250)
student_table.column("email", width=200)
student_table.column("roll_no", width=100)
student_table.column("phone_no", width=100)

student_table.pack(fill=BOTH, expand=1)

# Replace this with actual student ID based on login
logged_in_student_id = 1  # Example student ID; replace as needed

# Button to open update form (only for logged-in student)
update_btn = Button(root, text='Update Info', command=lambda: update_student(logged_in_student_id), font=('times new roman', 15, 'bold'), bg='cornflowerblue', fg='white')
update_btn.place(x=20, y=20)

# Fetch data on startup
fetch_data()

root.mainloop()