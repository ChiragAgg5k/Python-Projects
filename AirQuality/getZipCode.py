import json
import requests
import tkinter as tk

def verify():
    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipEntry.get()+"&distance=25&API_KEY=7476949B-F80D-4E53-A0EC-9A05E4AD8F48")
        api = json.loads(api_request.content)

    except Exception as e:
        api = "Error..."

    if api==[] or api=="Error...":

        print("ZipCode failed")
        askLabel.configure(text="Invalid Zipcode Entered.")
        enterButton.configure(text="Enter Again")
    else:

        global finalApi

        finalApi = api

        root.destroy()
        print("Zipcode Succes")
        return

def askZipCode():

    global root
    global askLabel
    global enterButton
    global zipEntry

    root = tk.Tk()
    root.geometry("270x200+650+300")
    root.title("Location verification...")

    title = tk.Label(text="AirNow Location Verification",font=("Arial bold",15),bg="azure4",fg="gray0",padx=25,pady=25)
    title.grid(row=0,column=0,padx=5,pady=5)

    askLabel = tk.Label(text="Enter a valid zipcode")
    askLabel.grid(row=1,column=0,pady=10)

    zipEntry = tk.Entry(root)
    zipEntry.grid(row=2,column=0)

    enterButton = tk.Button(text="Enter",command = verify)
    enterButton.grid(row=3,column=0,padx=10)

    root.mainloop()