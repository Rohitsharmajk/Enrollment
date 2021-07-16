from tkinter import *
def register_usr():

    username_info = username.get()
    password_info = password.get()

    file = open("Register.txt", "a")
    file.write("Username- "+username_info+"\n")
    file.write("Password- "+password_info+"\n")
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Created by Rohit")
    screen3.geometry("300x100")

    Label(screen3, text="You've Registered Successfully", font=("Calibri", 13)).pack()
    Label(screen3, text="").pack()
    Button(screen3, text="OK", width=10, height=1, command=lambda: screen3.destroy()).pack()



def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x400")
    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please enter your details").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_usr).pack()
    Button(screen1, text = "Cancel", width = 10, height = 1, command = lambda: screen1.destroy()).pack()
    Label(screen1, text = "").pack()

def lgin():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Created by Rohit")
    screen2.geometry("300x100")

    Label(screen2, text = "You've Logged In Successfully", font = ("Calibri",13)).pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "OK", width = 10, height = 1, command = lambda: screen2.destroy()).pack()

def login():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Created by Rohit")
    screen1.geometry("300x300")

    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please Enter your Log In Credentials below: ").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Log in", width=10, height=1, command= lgin).pack()
    Button(screen1, text = "Cancel", width=10, height=1, command= lambda: screen1.destroy()).pack()
    Label(screen1, text="").pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry('300x250')
    screen.title('Created by Rohit')
    Label(text = "Created by Rohit", bg = "grey",width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height = "2", width = "30", command = login).pack()
    Label(text="").pack()
    Button(text ="Register", height = "2", width = "30", command = register).pack()

    screen.mainloop()

main_screen()
