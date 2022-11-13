import tkinter as tk
import mysql.connector
import LoginScreen

windowHeight = 210

def connectDb():
    """
    This function will only be ran once.
    It initializes our mysql connection and our screenheight
    """

    global db
    global curr
    global windowHeight

    db = mysql.connector.connect(
        host="localhost", user=LoginScreen.USER_NAME, password=LoginScreen.USER_PASSWORD, database="")
    curr = db.cursor()

    curr.execute("use AddressBook;")
    curr.execute("select * from Addresses")
    rows = curr.fetchall()
    if rows!=None:  
        nrows = len(rows)
    else:
        nrows = 0

    windowHeight += nrows * 35

def showMainScreen():

    """
    This function is called multiple times.
    It has 2 frames - tableFrame and ButtonFrame
    tableFrame first has all the column headings and data below it.
    buttonFrame just has one button - Add Address
    """

    global windowHeight
    global curr
    global db
    global root

    root = tk.Tk()
    root.title("AddressBook - by ChiragAgg5k")

    tableFrame = tk.Frame(root)
    buttonFrame = tk.Frame(root)

    title = tk.Label(tableFrame,width=60,borderwidth=3,text="Addresses",pady=20,font=("Arial",17))

    SNo = tk.Label(tableFrame, width=10, text="Sno",
                   anchor=tk.W, borderwidth=2, relief="ridge",pady=10,padx=10)
    FirstName = tk.Label(tableFrame, width=10, text="First Name",
                         anchor=tk.W, borderwidth=2, relief="ridge",pady=10,padx=10)
    LastName = tk.Label(tableFrame, width=10, text="Last Name",
                        anchor=tk.W, borderwidth=2, relief="ridge",pady=10,padx=10)
    City = tk.Label(tableFrame, width=10, text="City",
                        anchor=tk.W, borderwidth=2, relief="ridge",pady=10,padx=10)
    State = tk.Label(tableFrame, width=10, text="State",
                        anchor=tk.W, borderwidth=2, relief="ridge",pady=10,padx=10)
    ZipCode = tk.Label(tableFrame, width=10, text="Zipcode",
                        anchor=tk.W, borderwidth=2, relief="ridge",pady=10,padx=10)

    title.grid(row=0,column=0,columnspan=6)
    SNo.grid(row=1, column=0)
    FirstName.grid(row=1, column=1)
    LastName.grid(row=1, column=2)
    City.grid(row=1,column=3)
    State.grid(row=1,column=4)
    ZipCode.grid(row=1,column=5)

    curr.execute("select * from Addresses;")
    records = curr.fetchall()

    if(records==None):
        pass
    else:
        for i in range(len(records)):
            for j in range(len(records[i])):
                tk.Label(tableFrame,text=records[i][j],width=10,anchor=tk.E,relief="ridge",padx=10,pady=10,borderwidth=2).grid(row=i+2,column=j)

    root.geometry(
        f"680x{windowHeight}+{(root.winfo_screenwidth()-680)//2}+{(root.winfo_screenheight()-500)//2 - 100}")


    addRecords = tk.Button(buttonFrame,text="Add address",padx=10,pady=10,command=addRecord)
    addRecords.grid(row=0,column=0,columnspan=6)

    tableFrame.grid(row=0, column=0,sticky=tk.E+tk.W+tk.N+tk.S)
    buttonFrame.grid(row=2,column=0,pady=25)

    root.mainloop()

def addRecord():

    """
    This function is a button command which pops up another window
    Here the user can add all the data needed for one address row
    """
    
    global top
    global FirstName
    global LastName
    global City
    global State
    global ZipCode

    top = tk.Toplevel()
    top.geometry(
        f"400x240+{(top.winfo_screenwidth()-200)//2 - 100}+{(top.winfo_screenheight()-200)//2-230}")
    top.title("Add record")

    FirstName = tk.Entry(top)
    LastName = tk.Entry(top)
    City = tk.Entry(top)
    State = tk.Entry(top)
    ZipCode = tk.Entry(top)

    tk.Label(top,text="First Name").grid(row=0,column=0,padx=10,pady=8)
    tk.Label(top,text="Last Name").grid(row=1,column=0,padx=10,pady=8)
    tk.Label(top,text="City").grid(row=2,column=0,padx=10,pady=8)
    tk.Label(top,text="State").grid(row=3,column=0,padx=10,pady=8)
    tk.Label(top,text="Zip Code").grid(row=4,column=0,padx=10,pady=8)

    FirstName.grid(row=0,column=1,padx=30,pady=10)
    LastName.grid(row=1,column=1,padx=30)
    City.grid(row=2,column=1,padx=30)
    State.grid(row=3,column=1,padx=30)
    ZipCode.grid(row=4,column=1,padx=30)

    addButton = tk.Button(top,text="Add",padx=20,pady=5,command=saveRecord)
    addButton.grid(row=5,column=0,padx=10)

    top.mainloop()

def saveRecord():   

    """
    This function saves the records added
    It only words if all the fields are non empty
    """ 

    global windowHeight

    windowHeight += 30

    curr.execute("select * from Addresses;")
    records = curr.fetchall()
    if(records != None):
        sno = len(records) + 1
    else:
        sno = 1

    if (FirstName.get()=="") or (LastName.get()=="") or (City=="") or (State.get()=="") or (ZipCode.get()==""):
        print("All fields must be non empty")
        return

    curr.execute(f"INSERT INTO Addresses(Sno,FirstName,LastName,City,State,ZipCode) VALUES({sno},'{FirstName.get()}','{LastName.get()}','{City.get()}','{State.get()}','{ZipCode.get()}');")
    db.commit()
    print("record added.")

    # destroys both windows 
    try:
        top.destroy()
        root.destroy()
    except tk.TclError:
        pass
    
    showMainScreen()


