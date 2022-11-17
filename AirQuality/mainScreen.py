import tkinter as tk

def showData(Api):
    
    root = tk.Tk()
    root.title("AirNow AirQuality")
    root.geometry("350x480+500+200")

    title = tk.Label(text="AirQuality Assessment",font=("Arial bold",25),padx=25,pady=25,bg="azure4",fg="gray0")
    title.grid(row=0,column=0,padx=10,pady=10,columnspan=2)

    city = Api[0]["ReportingArea"]
    quality = Api[0]["AQI"]
    category = Api[0]["Category"]["Name"]
    date = Api[0]["DateObserved"]
    timezone = Api[0]["LocalTimeZone"]
    statecode = Api[0]["StateCode"]
    longitude = Api[0]["Longitude"]
    latitude = Api[0]["Latitude"]

    infoFrame = tk.Frame(root)

    tk.Label(infoFrame,text="City",anchor=tk.W).grid(row=1,column=0,padx=10,pady=10)
    tk.Label(infoFrame,text="Quality",anchor=tk.W).grid(row=2,column=0,padx=10,pady=10)
    tk.Label(infoFrame,text="Category",anchor=tk.W).grid(row=3,column=0,padx=10,pady=10)
    tk.Label(infoFrame,text="Date Observed",anchor=tk.W).grid(row=4,column=0,padx=10,pady=10)
    tk.Label(infoFrame,text="Local Time Zone",anchor=tk.W).grid(row=5,column=0,padx=10,pady=10)
    tk.Label(infoFrame,text="State Code",anchor=tk.W).grid(row=6,column=0,padx=10,pady=10)
    tk.Label(infoFrame,text="Longitude",anchor=tk.W).grid(row=7,column=0,padx=10,pady=10)
    tk.Label(infoFrame,text="Latitude",anchor=tk.W).grid(row=8,column=0,padx=10,pady=10)

    tk.Label(infoFrame,text=city,anchor=tk.W).grid(row=1,column=1,padx=10,pady=10)
    tk.Label(infoFrame,text=quality,anchor=tk.W).grid(row=2,column=1,padx=10,pady=10)
    tk.Label(infoFrame,text=category,anchor=tk.W).grid(row=3,column=1,padx=10,pady=10)
    tk.Label(infoFrame,text=date,anchor=tk.W).grid(row=4,column=1,padx=10,pady=10)
    tk.Label(infoFrame,text=timezone,anchor=tk.W).grid(row=5,column=1,padx=10,pady=10)
    tk.Label(infoFrame,text=statecode,anchor=tk.W).grid(row=6,column=1,padx=10,pady=10)
    tk.Label(infoFrame,text=longitude,anchor=tk.W).grid(row=7,column=1,padx=10,pady=10)
    tk.Label(infoFrame,text=latitude,anchor=tk.W).grid(row=8,column=1,padx=10,pady=10)

    if category=="Good":
        title.configure(bg="green")
    elif category=="Moderate":
        title.configure(bg="yellow")
    elif category=="Unhealthy for Sensitive Groups":
        title.configure(bg="orange")
    elif category=="Unhealthy":
        title.configure(bg="dark orange")
    elif category=="Very Unhealthy":
        title.configure(bg="red")
    elif category=="Hazardous":
        title.configure(bg="dark red")
    else:
        title.configure(bg="gray")

    infoFrame.grid(row=1,column=0)

    root.mainloop()