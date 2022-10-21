import os
import tkinter as tk
from tkinter import filedialog as fd

from PIL import ImageTk, Image

def forward():
    global iterator
    global printImage

    try:
        if 0 <= iterator < len(imgList) - 1:
            iterator += 1

            printImage.grid_forget()
            printImage = tk.Label(image=imgList[iterator])
            printImage.grid(row=0, column=0, columnspan=3)

            backButton.configure(state=tk.NORMAL)
            statusText.set(f"Image {iterator+1} of {len(imgList)}")

        if iterator == (len(imgList)-1):
            forwardButton.configure(state=tk.DISABLED)

    except IndexError:
        pass


def backward():
    global iterator
    global printImage

    try:
        if 0 < iterator <= len(imgList):
            iterator -= 1

            printImage.grid_forget()
            printImage = tk.Label(image=imgList[iterator])  # type: ignore
            printImage.grid(row=0, column=0, columnspan=3)

            forwardButton.configure(state=tk.NORMAL)
            statusText.set(f"Image {iterator+1} of {len(imgList)}")

        if iterator == 0:
            backButton.configure(state=tk.DISABLED)

    except IndexError:
        pass


def showImages(ques):
    global dirLocation
    global statusText
    global imgList
    global iterator
    global printImage

    startLabel.grid_forget()
    selectFolderButton.grid_forget()
    useCurrentButton.grid_forget()

    if ques:
        text = tk.Label(text="Select a folder in the dialog box")
        text.pack(padx=50,pady=50)
        dirLocation = fd.askdirectory(initialdir=os.getcwd(), title="Select a folder")
        text.pack_forget()
    else:
        dirLocation = os.path.dirname(os.path.realpath(__file__))

    try:
        for images in os.listdir(dirLocation):
            if images.endswith(tuple(allowed_extentions)):
                imgList.append(Image.open(dirLocation+"/"+images))

    except FileNotFoundError:
        tk.Label(text="No image found.", padx=50,
                 pady=50).grid(column=0, row=1)
        return

    # creating a status bar that shows the current image we are one
    statusText = tk.StringVar()
    status = tk.Label(root, textvariable=statusText, anchor=tk.E)
    statusText.set(f"Image {iterator+1} of {len(imgList)}")

    # reducing size of all images
    # 600x600 is arbitrary , can be anything
    for i in range(len(imgList)):
        imgList[i].thumbnail((600, 600), Image.ANTIALIAS)
        imgList[i] = ImageTk.PhotoImage(imgList[i])  # type: ignore

    exitButton.grid(row=1, column=0)

    if len(imgList) != 0:
        startLabel.pack_forget()

        printImage = tk.Label(image=imgList[iterator])  # type: ignore
        printImage.grid(row=0, column=0, columnspan=3)

        backButton.grid(row=1, column=0)
        forwardButton.grid(row=1, column=2)

        workingDir = tk.Label(root, text="Working directory = "+dirLocation, anchor=tk.W)
        workingDir.grid(row=2, column=0, columnspan=2, sticky=tk.W)

        status.grid(row=2, column=1, columnspan=2, sticky=tk.W+tk.E)

        if len(imgList)==1:
            forwardButton.config(state=tk.DISABLED)

    else:
        tk.Label(text="No images found.").grid(row=0, column=0, padx=50, pady=50)

# Main code starts from here

root = tk.Tk()
root.eval('tk::PlaceWindow . center')
root.title("Image Viewer - by ChiragAgg5k")

# os.path. blah blah gets full path of the current working directory
try:
    titleImage = ImageTk.PhotoImage(Image.open(os.path.dirname(os.path.realpath(__file__))+"/Title.png"))
    startLabel = tk.Label(image=titleImage)
except FileNotFoundError:
    startLabel = tk.Label(text="Image Viewer", font=("Arial", 25))

startLabel.grid(row=0, column=0, columnspan=2, padx=50, pady=50)

# True means using filedialog while False means using current directory

selectFolderButton = tk.Button(text="Select a folder", command=lambda: showImages(True))
selectFolderButton.grid(row=1, column=0, pady=20)

useCurrentButton = tk.Button(text="Use current folder", command=lambda: showImages(False))
useCurrentButton.grid(row=1, column=1, pady=20)


imgList = []
allowed_extentions = [".png", ".jpg"]
iterator = 0

# defining buttons
exitButton = tk.Button(root, text="Exit", command=root.quit, padx=5, pady=10)
forwardButton = tk.Button(root, text=">>", padx=5, pady=10, command=forward)
backButton = tk.Button(root, text="<<", padx=5, pady=10,command=backward, state=tk.DISABLED)

root.mainloop()
