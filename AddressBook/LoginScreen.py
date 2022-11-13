import tkinter as tk
import Check

USER_NAME = ""
USER_PASSWORD = ""
loginCheck = False


def endLoginScreen():

    global loginCheck
    global USER_NAME
    global USER_PASSWORD

    USER_NAME = askUserName.get()
    USER_PASSWORD = askUserPass.get()

    if Check.CheckConnection(USER_NAME, USER_PASSWORD):
        Check.checkDatabase(USER_NAME, USER_PASSWORD)
        root.destroy()
        loginCheck = True

    else:
        print("Login failed.")
        enter.configure(text="Enter valid credentials")


def showLoginScreen():

    print("Login screen pops up")

    global root
    global askUserName
    global askUserPass
    global enter

    root = tk.Tk()
    root.geometry(f"280x160+{(root.winfo_screenwidth()-280)//2}+{(root.winfo_screenheight()-160)//2 - 100}")
    root.title("Login to continue")

    loginFrame = tk.Frame(root)

    titleLabel = tk.Label(loginFrame, text="MySQL Login", font=("Arial", 25))
    titleLabel.grid(padx=10, pady=10, row=0, column=0, columnspan=2)

    tk.Label(loginFrame, text="Username : ").grid(row=1, column=0)
    tk.Label(loginFrame, text="Password : ").grid(row=2, column=0)

    askUserName = tk.Entry(loginFrame)
    askUserName.insert(0,"root")
    askUserPass = tk.Entry(loginFrame)

    # enter a password here to not have to type it in every time
    askUserPass.insert(0,"")

    enter = tk.Button(loginFrame, text="Enter credentials",
                      command=endLoginScreen)

    askUserName.grid(row=1, column=1)
    askUserPass.grid(row=2, column=1)
    enter.grid(row=3, column=0, columnspan=2, pady=10)

    loginFrame.grid(row=0, column=0, sticky="NESW")

    root.mainloop()
