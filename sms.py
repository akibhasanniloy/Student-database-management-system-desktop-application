import os
os.environ['TCL_LIBRARY'] = r'C:\Users\User\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\User\AppData\Local\Programs\Python\Python313\tcl\tk8.6'

from tkinter import *
from tkinter import messagebox
import time
import ttkthemes
from tkinter import ttk
import pymysql

# Function
def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit')
    if result:
        root.destroy()
    else:
        pass

def update_student():
    selected_item = studentTable.focus()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a student to update.")
        return
    selected_data = studentTable.item(selected_item)['values']
    if not selected_data:
        return
    update_window = Toplevel()
    update_window.title('Update Student')
    update_window.grab_set()
    update_window.resizable(False, False)
    def update_data():
        if Std_IdEntry.get() == '' or nameEntry.get() == '' or departmentEntry.get() == '' or intakeEntry.get() == '' or addressEntry.get() == '' or emailEntry.get() == '' or roll_noEntry.get() == '' or phone_noEntry.get() == '' or admin_idEntry.get() == '':
            messagebox.showerror('Error', 'All fields must be filled', parent=update_window)
        else:
            try:
                query = '''UPDATE Student SET Name=%s, Department=%s, Intake=%s, Address=%s, Email=%s,
                           Roll_No=%s, Phone_No=%s, Admin_id=%s WHERE Std_Id=%s'''
                mycursor.execute(query, (
                    nameEntry.get(),
                    departmentEntry.get(),
                    intakeEntry.get(),
                    addressEntry.get(),
                    emailEntry.get(),
                    int(roll_noEntry.get()),
                    int(phone_noEntry.get()),
                    int(admin_idEntry.get()),
                    int(Std_IdEntry.get())
                ))
                con.commit()
                messagebox.showinfo('Success', f'ID {Std_IdEntry.get()} updated successfully')
                update_window.destroy()
                view_student()
            except Exception as e:
                con.rollback()
                messagebox.showerror('Error', f"Failed to update student: {str(e)}", parent=update_window)

    Std_IdLabel = Label(update_window, text='Std_Id', font=('times new roman', 20, 'bold'))
    Std_IdLabel.grid(row=0, column=0, padx=30, pady=10)
    Std_IdEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    Std_IdEntry.grid(row=0, column=1, pady=10, padx=40)
    Std_IdEntry.insert(0, selected_data[0])
    Std_IdEntry.config(state='readonly')
    
    nameLabel = Label(update_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=10)
    nameEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=10, padx=40)
    nameEntry.insert(0, selected_data[1])

    departmentLabel = Label(update_window, text='Department', font=('times new roman', 20, 'bold'))
    departmentLabel.grid(row=2, column=0, padx=30, pady=10)
    departmentEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    departmentEntry.grid(row=2, column=1, pady=10, padx=40)
    departmentEntry.insert(0, selected_data[2])

    intakeLabel = Label(update_window, text='Intake', font=('times new roman', 20, 'bold'))
    intakeLabel.grid(row=3, column=0, padx=30, pady=10)
    intakeEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    intakeEntry.grid(row=3, column=1, pady=10, padx=40)
    intakeEntry.insert(0, selected_data[3])

    addressLabel = Label(update_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=10)
    addressEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=10, padx=40)
    addressEntry.insert(0, selected_data[4])

    emailLabel = Label(update_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=5, column=0, padx=30, pady=10)
    emailEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=5, column=1, pady=10, padx=40)
    emailEntry.insert(0, selected_data[5])

    roll_noLabel = Label(update_window, text='Roll_No', font=('times new roman', 20, 'bold'))
    roll_noLabel.grid(row=6, column=0, padx=30, pady=10)
    roll_noEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    roll_noEntry.grid(row=6, column=1, pady=10, padx=40)
    roll_noEntry.insert(0, selected_data[6])

    phone_noLabel = Label(update_window, text='Phone_No', font=('times new roman', 20, 'bold'))
    phone_noLabel.grid(row=7, column=0, padx=30, pady=10)
    phone_noEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    phone_noEntry.grid(row=7, column=1, pady=10, padx=40)
    phone_noEntry.insert(0, selected_data[7])

    admin_idLabel = Label(update_window, text='Admin_id', font=('times new roman', 20, 'bold'))
    admin_idLabel.grid(row=8, column=0, padx=30, pady=10)
    admin_idEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    admin_idEntry.grid(row=8, column=1, pady=10, padx=40)
    admin_idEntry.insert(0, selected_data[8])

    update_student_button = ttk.Button(update_window, text='Update Student', command=update_data)
    update_student_button.grid(row=9, column=1, pady=10)

def view_student():
    Query='select * from Student'
    mycursor.execute(Query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)

def delete_student():
    indexing = studentTable.focus()
    if not indexing:
        messagebox.showwarning("Selection Error", "Please select a student to delete.")
        return
    print(indexing)
    content = studentTable.item(indexing)
    content_id = content['values'][0]
    query = 'DELETE FROM Student WHERE Std_id=%s'
    try:
        mycursor.execute(query, (content_id,))
        con.commit()
        messagebox.showinfo('Deleted', f'ID {content_id} is deleted successfully')
        Query = 'SELECT * FROM Student'
        mycursor.execute(Query)
        fetched_data = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('', 'end', values=data)
    except Exception as e:
        con.rollback()
        messagebox.showerror("Error", f"Failed to delete student: {str(e)}")

def search_student():
    def search_data():
        query= 'select *from Student where Std_Id=%s or Name=%s'
        mycursor.execute(query,(Std_IdEntry.get(), nameEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('',END, values=data)
    search_window=Toplevel()
    search_window.title('Search Student')
    search_window.grab_set()
    search_window.resizable(False, False)
    
    Std_IdLabel=Label(search_window, text='Std_Id', font=('times new roman',20,'bold'))
    Std_IdLabel.grid(row=0, column=0, padx=30, pady=10)
    Std_IdEntry=Entry(search_window, font=('roman', 15,'bold'),width=24)
    Std_IdEntry.grid(row=0, column=1, pady=10, padx=40)
    
    nameLabel=Label(search_window, text='Name', font=('times new roman',20,'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=10)
    nameEntry=Entry(search_window, font=('roman', 15,'bold'),width=24)
    nameEntry.grid(row=1, column=1, pady=10, padx=40)
    
    add_student_button=ttk.Button(search_window, text='Search', command=search_data)
    add_student_button.grid(row=2, column=1, pady=10)

def add_student():
    def add_data():
        if Std_IdEntry.get()=='' or nameEntry.get()=='' or departmentEntry.get()=='' or intakeEntry.get()=='' or addressEntry.get()=='' or emailEntry.get()=='' or roll_noEntry.get()=='' or phone_noEntry.get()=='' or admin_idEntry.get()=='':
            messagebox.showerror('Error', 'All field Must be filled', parent=add_window)
        else:
            try:
                query='insert into Student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(int(Std_IdEntry.get()), nameEntry.get(), departmentEntry.get(), intakeEntry.get(), addressEntry.get(),emailEntry.get(), int(roll_noEntry.get()), int(phone_noEntry.get()), int(admin_idEntry.get())))
                # print(query,(Std_IdEntry.get(), nameEntry.get(), departmentEntry.get(), intakeEntry.get(), addressEntry.get(),emailEntry.get(), roll_noEntry.get(),phone_noEntry.get(),admin_idEntry.get()))
                con.commit()
                result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?', parent=add_window)
                if result:
                    Std_IdEntry.delete(0, END)
                    nameEntry.delete(0, END)
                    departmentEntry.delete(0, END)
                    intakeEntry.delete(0, END)
                    addressEntry.delete(0, END)
                    emailEntry.delete(0, END)
                    roll_noEntry.delete(0, END)
                    phone_noEntry.delete(0, END)
                    admin_idEntry.delete(0, END)
                else:
                    pass
            except:
                messagebox.showerror('Error',"Value can't be repeated.", parent=add_window)
                return
            query='select *from Student'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:
                # dataList=list(data)
                studentTable.insert('',END, values=data)
    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(False, False)
    
    Std_IdLabel=Label(add_window, text='Std_Id', font=('times new roman',20,'bold'))
    Std_IdLabel.grid(row=0, column=0, padx=30, pady=10)
    Std_IdEntry=Entry(add_window, font=('roman', 15,'bold'),width=24)
    Std_IdEntry.grid(row=0, column=1, pady=10, padx=40)
    
    nameLabel=Label(add_window, text='Name', font=('times new roman',20,'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=10)
    nameEntry=Entry(add_window, font=('roman', 15,'bold'),width=24)
    nameEntry.grid(row=1, column=1, pady=10, padx=40)
    
    departmentLabel=Label(add_window, text='Department', font=('times new roman',20,'bold'))
    departmentLabel.grid(row=2, column=0, padx=30, pady=10)
    departmentEntry=Entry(add_window, font=('roman', 15,'bold'),width=24)
    departmentEntry.grid(row=2, column=1, pady=10, padx=40)
    
    intakeLabel=Label(add_window, text='Intake', font=('times new roman',20,'bold'))
    intakeLabel.grid(row=3, column=0, padx=30, pady=10)
    intakeEntry=Entry(add_window, font=('roman', 15,'bold'),width=24)
    intakeEntry.grid(row=3, column=1, pady=10, padx=40)
    
    addressLabel=Label(add_window, text='Address', font=('times new roman',20,'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=10)
    addressEntry=Entry(add_window, font=('roman', 15,'bold'),width=24)
    addressEntry.grid(row=4, column=1, pady=10, padx=40)
    
    emailLabel=Label(add_window, text='Email', font=('times new roman',20,'bold'))
    emailLabel.grid(row=5, column=0, padx=30, pady=10)
    emailEntry=Entry(add_window, font=('roman', 15,'bold'),width=24)
    emailEntry.grid(row=5, column=1, pady=10, padx=40)
    
    roll_noLabel=Label(add_window, text='Roll_No', font=('times new roman',20,'bold'))
    roll_noLabel.grid(row=6, column=0, padx=30, pady=10)
    roll_noEntry=Entry(add_window, font=('roman', 15,'bold'),width=24)
    roll_noEntry.grid(row=6, column=1, pady=10, padx=40)
    
    phone_noLabel=Label(add_window, text='Phone_No', font=('times new roman',20,'bold'))
    phone_noLabel.grid(row=7, column=0, padx=30, pady=10)
    phone_noEntry=Entry(add_window, font=('roman', 15,'bold'),width=24)
    phone_noEntry.grid(row=7, column=1, pady=10, padx=40)
    
    admin_idLabel=Label(add_window, text='Admin_id', font=('times new roman',20,'bold'))
    admin_idLabel.grid(row=8, column=0, padx=30, pady=10)
    admin_idEntry=Entry(add_window, font=('roman', 15,'bold'),width=24)
    admin_idEntry.grid(row=8, column=1, pady=10, padx=40)
    
    add_student_button=ttk.Button(add_window, text='Add Student', command=add_data)
    add_student_button.grid(row=9, column=1, pady=10)

def connect_database():
    def connect():
        global mycursor, con
        try:
            # con=pymysql.connect(host=hostEntry.get(), user=usernameEntry.get(), password=passwordEntry.get())
            con=pymysql.connect(host='localhost', user='root', password='12345')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details', parent=connectWindow)
            return
        try:
            query='create database project'
            mycursor.execute(query)
            query='use project'
            mycursor.execute(query)
            query='create table Student(Std_Id int auto_increment primary key, Name varchar(70),Department varchar(50),Intake varchar(40),Address varchar(90),Email varchar(40),Roll_No int,Phone_No int,Admin_id int,FOREIGN KEY (admin_id) REFERENCES admin(admin_id))'
            mycursor.execute(query)
        except:
            query='use project'
            mycursor.execute(query)
        messagebox.showinfo('Success','Successfully Connected', parent=connectWindow)
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        viewstudentButton.config(state=NORMAL)
        exitButton.config(state=NORMAL)

    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('490x250+738+238')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)
    
    hostnameLabel=Label(connectWindow, text='Host Name', font=('arial', 20,'bold'))
    hostnameLabel.grid(row=0, column=0,padx=20)
    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0, column=1, padx=20, pady=20)
    
    usernameLabel=Label(connectWindow, text='User Name', font=('arial', 20,'bold'))
    usernameLabel.grid(row=1, column=0,padx=20)
    usernameEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    usernameEntry.grid(row=1, column=1, padx=20, pady=20)
    
    passwordLabel=Label(connectWindow, text='Password', font=('arial', 20,'bold'))
    passwordLabel.grid(row=2, column=0,padx=20)
    passwordEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    passwordEntry.grid(row=2, column=1, padx=20, pady=20)
    
    connectButton=ttk.Button(connectWindow,text='Connect',command=connect)
    connectButton.grid(row=3, columnspan=3)

def clock():
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000, clock)

# Gui part
root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('1280x700+0+0')
root.resizable(0,0)
root.title('Admin Panel')

datetimeLabel=Label(root,font=('times new roman', 15, 'bold'))
datetimeLabel.place(x=5, y=5)
clock()

s='Student Database Management System'
textLabel= Label(root, text=s, font=('arial', 25,'italic bold'))
textLabel.place(x=300, y=0)

connectButton= ttk.Button(root, text='Connect to database', command=connect_database)
connectButton.place(x=1100, y=10)

# Buttons
leftFrame=Frame(root)
leftFrame.place(x=50, y=150, width=450, height=600)

# Add student
addstudentButton=ttk.Button(leftFrame, text='Add Student', width=25, state=DISABLED, command=add_student)
addstudentButton.grid(row=0, column=0, pady=20)

# Search Student
searchstudentButton=ttk.Button(leftFrame, text='Search Student', width=25, state=DISABLED, command=search_student)
searchstudentButton.grid(row=1, column=0, pady=20)

# Update Student
updatestudentButton=ttk.Button(leftFrame, text='Update Student', width=25, state=DISABLED, command=update_student)
updatestudentButton.grid(row=2, column=0, pady=20)

# Delete Student
deletestudentButton=ttk.Button(leftFrame, text='Delete Student', width=25, state=DISABLED, command=delete_student)
deletestudentButton.grid(row=3, column=0, pady=20)

# View Student
viewstudentButton=ttk.Button(leftFrame, text='View Student', width=25, state=DISABLED, command=view_student)
viewstudentButton.grid(row=4, column=0, pady=20)

# Exit
exitButton=ttk.Button(leftFrame, text='Exit', width=25, command=iexit)
exitButton.grid(row=5, column=0, pady=20)

# Preview Panel
rightFrame=Frame(root)
rightFrame.place(x=350, y=150, width=920, height=500)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame, columns=('Std_Id','Name','Department','Intake','Address','Email','Roll_No','Phone_No','Admin_id'), xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Std_Id', text='Std_Id')
studentTable.heading('Name', text='Name')
studentTable.heading('Department', text='Department')
studentTable.heading('Intake', text='Intake')
studentTable.heading('Address', text='Address')
studentTable.heading('Email', text='Email')
studentTable.heading('Roll_No', text='Roll_No')
studentTable.heading('Phone_No', text='Phone_No')
studentTable.heading('Admin_id', text='Admin_id')

studentTable.column('Std_Id', width=80, anchor=CENTER)
studentTable.column('Name', width=300, anchor=CENTER)
studentTable.column('Department', width=150, anchor=CENTER)
studentTable.column('Intake', width=120, anchor=CENTER)
studentTable.column('Address', width=200, anchor=CENTER)
studentTable.column('Email', width=300, anchor=CENTER)
studentTable.column('Roll_No', width=150, anchor=CENTER)
studentTable.column('Phone_No', width=200, anchor=CENTER)
studentTable.column('Admin_id', width=120, anchor=CENTER)

style=ttk.Style()
style.configure('Treeview', rowheight=40, font=('arial', 13, 'bold'), foreground='black')
style.configure('Treeview.Heading', font=('arial',14,'bold'))

studentTable.config(show='headings')

root.mainloop()