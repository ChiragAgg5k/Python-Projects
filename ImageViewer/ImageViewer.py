import os
import tkinter as tk

from PIL import ImageTk, Image

root = tk.Tk()
root.title("Image Viewer")

startLabel = tk.Label(text="Waiting for images to load.", padx=100, pady=100)
startLabel.pack()

# Iterating over all the files in the selected folder and checking for png files
imgNameList = []
imgList = []

try:
    workDir = input("Enter the path of folder containing the images: ")

    for images in os.listdir(workDir):
        if images.endswith(".png"):
            imgNameList.append(images)

    for i in imgNameList:
        imgList.append(Image.open(workDir + "/" + i))

except FileNotFoundError:
    print("\nInvalid directory entered.")

iterator = 0


def forward():
    global iterator
    global printImage

    try:
        if 0 <= iterator < len(imgList) - 1:
            iterator += 1
            printImage.grid_forget()
            printImage = tk.Label(image=imgList[iterator])  # type: ignore
            printImage.grid(row=0, column=0, columnspan=3)

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

    except IndexError:
        pass


exitButton = tk.Button(root, text="Exit", command=root.quit, padx=5, pady=10)
forwardButton = tk.Button(root, text=">>", padx=5, pady=10, command=forward)
backButton = tk.Button(root, text="<<", padx=5, pady=10, command=backward)

# reducing size of all images
for i in range(len(imgList)):
    imgList[i] = imgList[i].resize(
        (round(imgList[i].size[0] * 0.5), round(imgList[i].size[1] * 0.5)))
    imgList[i] = ImageTk.PhotoImage(imgList[i])  # type: ignore

if len(imgList) != 0:
    print("\nShowing the images in a new window.")
    startLabel.pack_forget()

    printImage = tk.Label(image=imgList[iterator])  # type: ignore
    printImage.grid(row=0, column=0, columnspan=3)

    backButton.grid(row=1, column=0)
    exitButton.grid(row=1, column=1)
    forwardButton.grid(row=1, column=2)

    root.mainloop()

else:
    print("No images found in the folder.")
    root.quit()
