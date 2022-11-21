# Import Tkinter and other libraries
import os
import time
import math
import sympy
import base64
import random
import hashlib
import binascii
import tkinter as tk
from tkinter import *
from tkinter import ttk
from pathlib import Path
from tkinter import messagebox
from zipfile import ZipFile as zp
from tkinter import filedialog as fd

# Starting GUI
root = Tk()

# Configuration of GUI
style = ttk.Style()
root.geometry("650x250")
root.title("Digital Signature Application")

style.configure("TLabel", font="Serif 15", padding=10)
style.configure("TButton", font="Serif 15", padding=10)
########################################################################################################################


# Function for generating keys
def generateKeys():
    global n, e, d
    # Generate p
    p = sympy.randprime(10 ** 19, (10 ** 20) - 1)

    # Generate q
    q = sympy.randprime(10 ** 19, (10 ** 20) - 1)
    if p == q:
        q = sympy.randprime(10 ** 19, (10 ** 20) - 1)

    # Generate n
    n = p * q

    # Generate e
    fn = (p - 1) * (q - 1)
    e = 2
    while math.gcd(e, fn) != 1:
        e = random.randint(2, fn)

    # Generate d
    fn = (p - 1) * (q - 1)
    d = pow(e, -1, fn)

    # Displaying the keys selection windows
    # Module
    open(fd.asksaveasfilename(initialdir="/", defaultextension=".txt", title="Save the module"), "w") \
        .write(str(n))

    # Public key
    open(fd.asksaveasfilename(initialdir="/", defaultextension=".pub", title="Save the public key"), "w") \
        .write(str(e))

    # Private key
    open(fd.asksaveasfilename(initialdir="/", defaultextension=".priv", title="Save the private key"), "w") \
        .write(str(d))

    messagebox.showinfo("Success", "The keys were successfully generated and saved")


# Function for selection the module
def selectModule():
    moduleType = [('txt', '*.txt')]
    module = fd.askopenfilename(initialdir="/", title="Select the module", filetypes=moduleType)
    nKey = open(module, 'r').read()

    return nKey


# Function for selection the public key
def selectPublicKey():
    publicKeyType = [('pub', '*.pub')]
    publicKey = fd.askopenfilename(initialdir="/", title="Select the public key", filetypes=publicKeyType)
    eKey = open(publicKey, 'r').read()

    return eKey


# Function for selection the private key
def selectPrivateKey():
    privateKeyType = [('priv', '*.priv')]
    privateKey = fd.askopenfilename(initialdir="/", title="Select the private key", filetypes=privateKeyType)
    dKey = open(privateKey, 'r').read()

    return dKey


# Function for selection the file
def selectFile():
    global fileName
    fileTypes = [
        ('txt', '*.txt'),
        ('pdf', '*.pdf'),
        ('docx', '*.docx'),
        ('pptx', '*.pptx'),
        ('jpg', '*.jpg'),
        ('jpeg', '*.jpeg'),
        ('png', '*.png'),
        ('bmp', '*.bmp'),
        ('All Files', '*.*')
    ]

    fileName = fd.askopenfilename(
        title="Select the file for encrypt",
        initialdir='/',
        filetypes=fileTypes)

    # Size and date of file
    size = os.path.getsize(fileName)
    size = str(size)
    date = time.ctime(os.path.getmtime(fileName))
    date = str(date)

    # Displaying file data
    File_label = tk.Label(root, text="Path: " + fileName, fg="SpringGreen3")
    File_label.grid(row=6, column=1, sticky=N + E)
    Size_label = tk.Label(root, text="File size: " + size + " bytes", fg="SpringGreen3")
    Size_label.grid(row=4, column=1, sticky=N + E)
    Date_label = tk.Label(root, text="Created time: " + date, fg="SpringGreen3")
    Date_label.grid(row=5, column=1, sticky=N + E)


# Function for selection the zip file
def selectZip():
    folderType = [('zip', '*.zip')]
    zipFile = fd.askopenfilename(initialdir="/", title="Select the zip file for decrypt", filetypes=folderType)

    return zipFile


# Function for encryption
def encryptRSA(arg):
    module = selectModule()
    private_key = selectPrivateKey()
    module = int(module)
    private_key = int(private_key)
    arr = []
    arr2 = []

    # Characters to numbers
    messageToList = [arg]
    for i in messageToList:
        for symbol in i:
            arr2.append(ord(symbol))

    # Split by 8 characters
    for i in range(0, len(arr2), 8):
        arr.append(arr2[i:i + 8])

    # Conversion into binary system
    arr2 = []
    for i in arr:
        for symbol in i:
            arr2.append(bin(symbol).replace("0b", ""))

    # Add zeros if the binary number doesn't have 11 characters
    arr = []
    for symbol in arr2:
        if len(symbol) != 11:
            symbol = (11 - len(symbol)) * "0" + symbol
        arr.append(symbol)

    # Split by 8 characters
    arr2 = []
    for i in range(0, len(arr), 8):
        arr2.append(arr[i:i + 8])

    # Convert to decimal from binary and encryption
    messageToList = []
    for s in arr2:
        text = "".join(s)
        out = int(text, 2)

        cipher_text = pow(out, private_key, module)
        messageToList.append(str(cipher_text))

    cipher = " ".join(messageToList)
    return cipher


# Function for decryption
def decryptRSA(arg):
    module = selectModule()
    public_key = selectPublicKey()

    # Splitting the input
    messageList = arg.split(" ")

    # Creating array of integers from input
    messageToList = map(int, messageList)
    module = int(module)
    public_key = int(public_key)
    arr = []

    # Conversion into decimal system
    for symbol in messageToList:
        indexesPT = pow(symbol, public_key, module)
        arr.append(indexesPT)

    # Conversion into binary system
    arr2 = []
    for s in arr:
        temp = bin(s).replace("0b", "")
        # Add zeros depending on whether the block has 110 characters
        if len(temp) < 110:
            temp = (110 - len(temp)) * "0" + temp
        arr2.append(temp)

    # Split by 11 characters
    arr = []
    u = "".join(arr2)
    for i in range(0, len(u), 11):
        arr.append(u[i:i + 11])

    # Conversion from binary system into decimal
    arr2 = []
    for s in arr:
        text = "".join(s)
        decimal = int(text, 2)
        arr2.append(decimal)

    # Conversion from decimal to characters, if x00 appears it is removed from the string
    arr = []
    for s in arr2:
        smbl = chr(s)
        if smbl == "\x00":
            smbl = smbl.replace("\x00", "")
        arr.append(smbl)

    # Printing result
    plain_text = "".join(arr)
    return plain_text


# Function for creating hash
def hashFunction(arg):
    hashObject = hashlib.sha3_512(arg).hexdigest()
    return hashObject


# Function for base64 encode
def base64Encode(arg):
    return base64.b64encode(arg.encode('utf-8'))


def base64Decode(arg):
    hash_ = base64.b64decode(arg)
    hashDecode = hash_.decode('utf-8')
    return hashDecode


# Function for signing the file
def sign():
    saveZip = fd.asksaveasfilename(defaultextension=".zip", title="Save the signed file")
    typeOfFile = Path(fileName).suffix

    # Writing files into zip
    zipFile = zp(saveZip, 'w')
    try:
        fileToSign = open(fileName, 'rb')
        copyOfFile = open("copy-of-original-file" + typeOfFile, 'wb')

        # Encrypt the file + hash and save as copy
        try:
            hashOfFile = fileToSign.read()
            hashFile = hashFunction(hashOfFile)
            copyOfFile.write(hashOfFile)
            cipher = encryptRSA(str(hashFile))
        finally:
            zipFile.write("copy-of-original-file" + typeOfFile)

        cipher_list = []
        for symbol in cipher:
            symbol = str(symbol)
            cipher_list.append(symbol)

        cipher_text = "".join(cipher_list)
        cipher = base64Encode(cipher_text).decode('utf-8')

        finalResult = open("encrypted-hash.sign", 'w')
        try:
            finalResult.write(cipher)
        finally:
            finalResult.close()
            zipFile.write("encrypted-hash.sign")
    finally:
        messagebox.showinfo("Success", "The file was successfully signed")


# Function for verification the zip file
def verification():
    global hash1, hash2
    folder = selectZip()
    signExtension = ".sign"

    zipFile = zp(folder, 'r')
    try:
        filesInZip = zipFile.namelist()
        for file in filesInZip:

            # Decryption a file with a .sign extension
            if signExtension in file:
                signedFile = zipFile.open(file, 'r')
                try:
                    hashOfFile = signedFile.read()
                    decodedHash = base64Decode(hashOfFile)
                    hash2 = decryptRSA(decodedHash)
                except UnicodeDecodeError:
                    messagebox.showerror("Error", "File verification error")
                    break
                except binascii.Error:
                    messagebox.showerror("Error", "File verification error")
                    break
                except ValueError:
                    messagebox.showerror("Error", "File verification error")
                    break
                finally:
                    signedFile.read()

            # Creating a hash of a copy of a file
            elif signExtension not in file:
                copyOfFile = zipFile.open(file, 'r')
                try:
                    hashOfFile2 = copyOfFile.read()
                    hash1 = hashFunction(hashOfFile2)
                finally:
                    copyOfFile.read()
            else:
                messagebox.showerror("Error", "The file with the extension .sign was not found")
                break
        try:
            if hash1 == hash2:
                messagebox.showinfo("Success", "Zip file was verified successfully")
        except NameError:
            messagebox.showerror("Error", "Necessary files was not found")
    finally:
        zipFile.close()


########################################################################################################################
# Labels and Buttons
Welcome_label = tk.Label(root, text="Welcome to the Digital Signature application!", fg="red")
Welcome_label.grid(row=0, column=1, sticky=N + W)

Info_Label = tk.Label(root, text="Selected file Info:", fg="cyan3")
Info_Label.grid(row=3, column=1, sticky=N)

Select_label = tk.Label(root, text="1. Select the file for encryption", fg="green")
Select_label.grid(row=1, column=0, sticky=N + W)
Select_button = ttk.Button(root, text="Select File", command=lambda: selectFile())
Select_button.grid(row=2, column=0, sticky=N + W)

Generate_label = tk.Label(root, text="2. Generate the necessary keys", fg="green")
Generate_label.grid(row=3, column=0, sticky=N + W)
Generate_button = ttk.Button(root, text="Generate", command=lambda: generateKeys())
Generate_button.grid(row=4, column=0, sticky=N + W)

Save_label = tk.Label(root, text="3. Save the signed file", fg="green")
Save_label.grid(row=5, column=0, sticky=N + W)
Save_button = ttk.Button(root, text="Save", command=lambda: sign())
Save_button.grid(row=6, column=0, sticky=N + W)

Decryption_label = tk.Label(root, text="You can also select the file for decryption", fg="DarkOrange1")
Decryption_label.grid(row=1, column=1, sticky=N + E)
Decryption_button = ttk.Button(root, text="Select File", command=lambda: verification())
Decryption_button.grid(row=2, column=1, sticky=N)

# Ending GUI
root.mainloop()
