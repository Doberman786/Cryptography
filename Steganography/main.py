# Import Tkinter library and other stuff
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog as fd

# Starting GUI
root = Tk()

# GUI configuration
style = ttk.Style()
root.geometry("900x600")
root.title("Steganography Application")

style.configure("TLabel", font="Serif 15", padding=10)
style.configure("TButton", font="Serif 15", padding=10)
style.configure("TEntry", font="Serif 18", padding=10)

# Input and Output fields
Input = ttk.Entry(root, width=85)
Input.grid(row=1, column=1, rowspan=5, columnspan=5, sticky=N + W)

Output = Text(root, width=79, height=3, font=("Serif", 15))
Output.grid(row=4, column=1, rowspan=5, columnspan=5, sticky=N + W)

########################################################################################################################


# Convert data into binary form (ASCII (8-bit))
def generateData(data):
    new_data = []
    for i in data:
        new_data.append(format(ord(i), '08b'))
    return new_data


# Function to modify the pixels of image
def modifyPixels(pixels, data):
    dataList = generateData(data)
    lengthOfData = len(dataList)
    imageData = iter(pixels)

    for i in range(lengthOfData):
        pixels = [value for value in imageData.__next__()[:3] +
                  imageData.__next__()[:3] +
                  imageData.__next__()[:3]]

        for j in range(0, 8):
            if dataList[i][j] == '0' and pixels[j] % 2 != 0:
                if pixels[j] % 2 != 0:
                    pixels[j] -= 1
            elif dataList[i][j] == '1' and pixels[j] % 2 == 0:
                pixels[j] -= 1

        if i == lengthOfData - 1:
            if pixels[-1] % 2 == 0:
                pixels[-1] -= 1
        else:
            if pixels[-1] % 2 != 0:
                pixels[-1] -= 1

        pixels = tuple(pixels)
        yield pixels[0:3]
        yield pixels[3:6]
        yield pixels[6:9]


# Function to enter the data pixels into image
def pixelsToImage(newImage, data):
    imageSize = newImage.size[0]
    (x, y) = (0, 0)

    for pixel in modifyPixels(newImage.getdata(), data):
        newImage.putpixel((x, y), pixel)
        if x == imageSize - 1:
            x = 0
            y += 1
        else:
            x += 1


# Function for enter text to the image
def encode(image):
    global Show_labelCode, Image_labelCode

    message = Input.get()
    if len(message) == 0:
        messagebox.showinfo("Alert", "You need to put some text into the image")
    else:
        newImage = image.copy()
        pixelsToImage(newImage, message)

        imagePath = os.path.splitext(os.path.basename(image.filename))[0]
        newImage.save(fd.asksaveasfilename(
            initialfile=imagePath,
            filetypes=([('png', '*.png'),
                        ('bmp', '*.bmp')]),
            defaultextension=".png"))

        messagebox.showinfo("Success", "The message was successfully attached to the image!")

        # Reducing the image for GUI
        codeImagePreview = newImage
        image_preview = codeImagePreview.resize((300, 250))

        # Displaying image data
        Image_labelCode = tk.Label(root, text="Image with the hidden message: ", fg="cyan")
        Image_labelCode.grid(row=9, column=2, sticky=N + W)

        # Displaying the image
        ShowImageInGUI = ImageTk.PhotoImage(image_preview)
        Show_labelCode = Label(root, image=ShowImageInGUI)
        Show_labelCode.grid(row=12, column=2, sticky=N + W)
        Show_labelCode.image = ShowImageInGUI


# Function for reading the message in the image
def decode(image):
    Output.delete(0.0, END)
    imageData = iter(image.getdata())
    data = ''

    while True:
        pixels = [value for value in imageData.__next__()[:3] +
                  imageData.__next__()[:3] +
                  imageData.__next__()[:3]]
        binaryStr = ''
        for i in pixels[:8]:
            if i % 2 == 0:
                binaryStr += '0'
            else:
                binaryStr += '1'

        data += chr(int(binaryStr, 2))
        if pixels[-1] % 2 != 0:
            return Output.insert(0.0, data)


# Image selection function
def selectImage():
    global image_org

    # Available types
    imageTypes = [
        ('jpeg', '*.jpeg'),
        ('jpg', '*.jpg'),
        ('png', '*.png'),
        ('bmp', '*.bmp'),
        ('All Files', '*.*')
    ]

    # Displaying the image selection window
    imageName = fd.askopenfilename(
        title="Select an Image",
        initialdir='/',
        filetypes=imageTypes)

    image_org = Image.open(imageName)

    # Reducing the image for GUI
    image_preview = image_org.resize((300, 250))
    ImageOriginal = ImageTk.PhotoImage(image_org)
    ShowImageInGUI = ImageTk.PhotoImage(image_preview)

    # Dimensions and size of image
    dimensions = "Dimensions: %dx%d" % (ImageOriginal.width(), ImageOriginal.height())
    size = os.path.getsize(imageName)
    size = str(size)

    # Displaying image data
    Image_labelOrg = tk.Label(root, text="Selected Image: " + imageName, fg="cyan")
    Image_labelOrg.grid(row=9, column=1, sticky=N + W)
    Dimension_label = tk.Label(root, text=dimensions, fg="lightblue")
    Dimension_label.grid(row=10, column=1, sticky=N + W)
    Size_label = tk.Label(root, text="Image size: " + size + " bytes", fg="lightgreen")
    Size_label.grid(row=11, column=1, sticky=N + W)

    # Displaying the image
    Show_labelOrg = Label(root, image=ShowImageInGUI)
    Show_labelOrg.grid(row=12, column=1, sticky=N + W)
    Show_labelOrg.image = ShowImageInGUI


########################################################################################################################
# Labels and Buttons
SelectImage_button = ttk.Button(root, text="Select Image", command=lambda: selectImage())
SelectImage_button.grid(row=0, column=1, sticky=N + W)

Encode_button = ttk.Button(root, text="Insert the message", command=lambda: encode(image_org))
Encode_button.grid(row=3, column=1, sticky=N + W)

Decode_button = ttk.Button(root, text="Read the message", command=lambda: decode(image_org))
Decode_button.grid(row=3, column=2, sticky=N + W)

Input_label = tk.Label(root, text="Input text", fg="lightgreen")
Input_label.grid(row=1, column=0, sticky=N)
Input_clear = tk.Button(root, text="Clear", command=lambda: clear('input'))
Input_clear.grid(row=2, column=0, sticky=N)

Output_label = tk.Label(root, text="Output text", fg="red")
Output_label.grid(row=4, column=0)
Output_clear = tk.Button(root, text="Clear", command=lambda: clear('output'))
Output_clear.grid(row=5, column=0)


# Function for cleaning fields
def clear(str_val):
    if str_val == 'input':
        Input.delete(0, 'end')
    elif str_val == 'output':
        Output.delete(0.0, 'end')


# Ending GUI
root.mainloop()
