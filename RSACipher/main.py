# Import Tkinter and other libraries
import math
import random
import sympy
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Starting GUI
root = Tk()

# Configuration of GUI
style = ttk.Style()
root.geometry("970x425")
root.title("RSA Cipher Application")

style.configure("TLabel", font="Serif 15", padding=10)
style.configure("TButton", font="Serif 15", padding=10)
style.configure("TEntry", font="Serif 18", padding=10)

# Input fields
Input = ttk.Entry(root, width=95)
Input.grid(row=0, column=1, rowspan=5, columnspan=5, sticky=N + W)

nKey_input = ttk.Entry(root, width=95)
nKey_input.grid(row=3, column=1, rowspan=5, columnspan=5, sticky=N + W)

eKey_input = ttk.Entry(root, width=95)
eKey_input.grid(row=8, column=1, rowspan=5, columnspan=5, sticky=N + W)

dKey_input = ttk.Entry(root, width=95)
dKey_input.grid(row=13, column=1, rowspan=5, columnspan=5, sticky=N + W)


selection = IntVar()
tk.Radiobutton(root, text="Encrypt", variable=selection, value=1).grid(row=18, column=2, sticky=N)
tk.Radiobutton(root, text="Decrypt", variable=selection, value=2).grid(row=18, column=4, sticky=N)

Output = Text(root, width=88, height=5, font=("Serif", 15))
Output.grid(row=20, column=1, rowspan=5, columnspan=5, sticky=N + W)


# Function for generating keys
def generateKeys():
    nKey_input.delete(0, END)
    eKey_input.delete(0, END)
    dKey_input.delete(0, END)

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

    # Print the keys
    nKey_input.insert(END, n)
    dKey_input.insert(END, d)
    eKey_input.insert(END, e)


# Function for checking public key
def checkE():
    public_key = eKey_input.get()
    for symbol in public_key:
        if symbol.isnumeric():
            continue
        else:
            messagebox.showerror("Error", "The public key must not contain the characters")
            raise ValueError("Unexpected input")

    public_key = int(public_key)
    if public_key <= 1:
        messagebox.showerror("Error", "Public key must be greater than 1")
        raise ValueError("Unable to calculate GCD")

    return int(public_key)


# Function for checking private key
def checkD():
    private_key = dKey_input.get()
    for symbol in private_key:
        if symbol.isnumeric():
            continue
        else:
            messagebox.showerror("Error", "The private key must not contain the characters")
            raise ValueError("Unexpected input")

    return int(private_key)


# Function for encryption
def encrypt():
    global out
    Output.delete(0.0, END)
    message = Input.get()
    module = nKey_input.get()
    public_key = checkE()

    module = int(module)
    arr = []
    arr2 = []

    # Characters to numbers
    messageToList = [message]
    print("Message to List: ", messageToList)
    for i in messageToList:
        for symbol in i:
            arr2.append(ord(symbol))

    print("To numbers: ", arr2)

    # Split by 8 characters
    for i in range(0, len(arr2), 8):
        arr.append(arr2[i:i + 8])

    print("8 characters: ", arr)

    # Conversion into binary system
    arr2 = []
    for i in arr:
        for symbol in i:
            arr2.append(bin(symbol).replace("0b", ""))

    print("Binary system: ", arr2)

    # Add zeros if the binary number doesn't have 11 characters
    arr = []
    for symbol in arr2:
        if len(symbol) != 11:
            symbol = (11 - len(symbol)) * "0" + symbol
        arr.append(symbol)

    print("Add 0: ", arr)

    # Split by 8 characters
    arr2 = []
    for i in range(0, len(arr), 8):
        arr2.append(arr[i:i + 8])

    print("8 characters: ", arr2)

    # Convert to decimal from binary and encryption
    messageToList = []
    for s in arr2:
        text = "".join(s)
        out = int(text, 2)
        cipher_text = pow(out, public_key, module)
        messageToList.append(cipher_text)

    print("To decimal: ", str(out))
    print("Final: ", messageToList)

    # Printing result
    Output.insert(END, messageToList)


# Function for decryption
def decrypt():
    Output.delete(0.0, END)
    message = Input.get()
    module = nKey_input.get()
    private_key = checkD()

    # Splitting the input
    messageList = message.split(" ")

    # Creating array of integers from input
    messageToList = map(int, messageList)
    module = int(module)
    arr = []

    # Conversion into decimal system
    for symbol in messageToList:
        indexesPT = pow(symbol, private_key, module)
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
    Output.insert(END, plain_text)


# Function for Encrypt/Decrypt buttons
def execute():
    choice = selection.get()
    if choice == 1:
        encrypt()
    elif choice == 2:
        decrypt()
    else:
        messagebox.showerror("Error", "You need to choose a function (Encrypt/Decrypt)")
        raise ValueError("The function was not selected")


########################################################################################################################
# Labels and Buttons
Input_label = tk.Label(root, text="Input text", fg="lightgreen")
Input_label.grid(row=0, column=0, sticky=N)
Input_clear = tk.Button(root, text="Clear", command=lambda: clear('input'))
Input_clear.grid(row=1, column=0, sticky=N)

GenerateKeys_button = ttk.Button(root, text="Generate keys", command=lambda: generateKeys())
GenerateKeys_button.grid(row=2, column=3, sticky=N)

nKey_label = tk.Label(root, text="Module", fg="cyan")
nKey_label.grid(row=5, column=0, sticky=N)

eKey_label = tk.Label(root, text="Public key", fg="green")
eKey_label.grid(row=10, column=0, sticky=N)

dKey_label = tk.Label(root, text="Private key", fg="lightblue")
dKey_label.grid(row=15, column=0, sticky=N)

Execute_button = ttk.Button(root, text="Execute", command=lambda: execute())
Execute_button.grid(row=19, column=3, sticky=N)

Output_label = tk.Label(root, text="Output text", fg="red")
Output_label.grid(row=21, column=0)
Output_copy = tk.Button(root, border=4, text="Copy", command=lambda: instantPaste())
Output_copy.grid(row=22, column=0)
Output_clear = tk.Button(root, border=4, text="Clear", command=lambda: clear('output'))
Output_clear.grid(row=23, column=0)


# Function for cleaning fields
def clear(str_val):
    if str_val == 'input':
        Input.delete(0, 'end')
    elif str_val == 'output':
        Output.delete(0.0, 'end')


# Function for simply copying text from Output and simply pasting text to the Input
def instantPaste():
    root.clipboard_clear()  # Optional
    root.clipboard_append(Output.get('1.0', END).rstrip())
    root.update()
    Input.delete(0, 'end')
    Input.insert(END, root.clipboard_get())
    Output.delete(0.0, 'end')
    selection.set(2)


# Ending GUI
root.mainloop()
