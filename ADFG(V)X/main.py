# Import Tkinter Library and other stuff
import random
import unicodedata
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tabulate import tabulate
from tkinter import messagebox

########################################################################################################################

# Starting GUI
root = Tk()

# Creating tabs
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

#  INPUT FIELDS
# ADFGX
Input_text = ttk.Entry(tab1, width=110, font=("Serif", 14))
Input_text.grid(row=0, column=1, rowspan=5, columnspan=5, sticky=W + N)

# ADFGVX
Input2_text = ttk.Entry(tab2, width=110, font=("Serif", 14))
Input2_text.grid(row=0, column=1, rowspan=5, columnspan=5, sticky=W + N)
###################################

# KEYWORD FIELDS
# ADFGX
Key_input = ttk.Entry(tab1, width=110, font=("Serif", 14))
Key_input.grid(row=3, column=1, rowspan=5, columnspan=5, sticky=W + N)

# ADFGVX
Key2_input = ttk.Entry(tab2, width=110, font=("Serif", 14))
Key2_input.grid(row=3, column=1, rowspan=5, columnspan=5, sticky=W + N)
###################################

# GENERATED ALPHABET FIELDS
# ADFGX
ALPHABET_gen25 = ttk.Entry(tab1, width=110, font=("Serif", 14))
ALPHABET_gen25.grid(row=8, column=1, rowspan=5, columnspan=5, sticky=N)

# ADFGVX
ALPHABET_gen36 = ttk.Entry(tab2, width=110, font=("Serif", 14))
ALPHABET_gen36.grid(row=8, column=1, rowspan=5, columnspan=5, sticky=N)
###################################

# OUTPUT FIELDS
# ADFGX
Output = Text(tab1, width=110, height=4, font=("Serif", 14))
Output.grid(row=15, column=1, rowspan=5, columnspan=5, sticky=W + N)

# ADFGVX
Output2 = Text(tab2, width=110, height=4, font=("Serif", 14))
Output2.grid(row=14, column=1, rowspan=5, columnspan=5, sticky=W + N)
###################################

# TABLES FIELDS
# ADFGX
Table_sub25 = tk.Label(tab1, text="\n \n \n \n", width=17, font=('Serif', 11), relief="sunken")
Table_tran25 = tk.Label(tab1, text="\n \n \n \n", width=17, font=('Serif', 11), relief="sunken")

# ADFGVX
Table_sub36 = tk.Label(tab2, text="\n \n \n \n", width=17, font=('Serif', 11), relief="sunken")
Table_tran36 = tk.Label(tab2, text="\n \n \n \n", width=17, font=('Serif', 11), relief="sunken")
###################################

# Language selection buttons
selection = IntVar()
ttk.Radiobutton(tab1, text="EN", variable=selection, value=1).grid(row=13, column=2, sticky=N)
ttk.Radiobutton(tab1, text="CZ", variable=selection, value=2).grid(row=13, column=4, sticky=N)


########################################################################################################################


# Function for removing symbols from string
def remove_symbols(text):
    return text.translate({ord(i): None for i in r"""!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""})


# Function for removing diacritics from string
def remove_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


# Function for generate table 5x5
def generateALPHABET25():
    ALPHABET_gen25.delete(0, END)
    choice = selection.get()
    ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    random.shuffle(ALPHABET)

    # Creating a string from a list
    ALPHABET = remove_symbols(str(ALPHABET).replace(" ", ""))

    # Dependence on language
    # ENG
    if choice == 1:
        ALPHABET = ALPHABET.replace("Q", "")
        ALPHABET_gen25.insert(END, ALPHABET)
    # CZ
    elif choice == 2:
        ALPHABET = ALPHABET.replace("W", "")
        ALPHABET_gen25.insert(END, ALPHABET)
    else:
        ALPHABET_gen25.insert(END, "Please, choice the language!")

    # Print the 5x5 table in GUI
    ABC_table = ALPHABET
    tabl = list(ABC_table)
    tabl1 = tabl[:5]
    tabl2 = tabl[5:10]
    tabl3 = tabl[10:15]
    tabl4 = tabl[15:20]
    tabl5 = tabl[20:25]

    table = [tabl1, tabl2, tabl3, tabl4, tabl5]
    table_print = ""
    if choice != 1 and choice != 2:
        table_print = ""
    else:
        for i in range(5):
            if i > 0:
                table_print = table_print + "\n"
            for j in range(5):
                table_print = table_print + "  " + table[i][j] + "  "

    Table_output = Label(tab1, text=table_print, font=("Serif", 11), relief="sunken")
    Table_output.grid(row=21, column=5, sticky=N)


# Function for generate table 6x6
def generateAPLHABET36():
    ALPHABET_gen36.delete(0, END)
    ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    random.shuffle(ALPHABET)

    # Creating a string from a list
    ALPHABET = remove_symbols(str(ALPHABET).replace(" ", ""))
    ALPHABET_gen36.insert(END, ALPHABET)

    # Print the 6x6 table in GUI
    ABC_table = ALPHABET
    tabl = list(ABC_table)
    tabl1 = tabl[:6]
    tabl2 = tabl[6:12]
    tabl3 = tabl[12:18]
    tabl4 = tabl[18:24]
    tabl5 = tabl[24:30]
    tabl6 = tabl[30:36]

    table = [tabl1, tabl2, tabl3, tabl4, tabl5, tabl6]
    table_print = ""
    for i in range(6):
        if i > 0:
            table_print = table_print + "\n"
        for j in range(6):
            table_print = table_print + "  " + table[i][j] + "  "

    Table_output = Label(tab2, text=table_print, font=("Serif", 11), relief="sunken")
    Table_output.grid(row=20, column=5, sticky=N)


# Function for checking keyword in ADFGX (5x5)
def check_key25():
    ALPHABET_FULL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_word = Key_input.get()
    key_word = remove_symbols(remove_accents(key_word)).replace(" ", "").upper()

    for symbol in key_word:
        if symbol not in ALPHABET_FULL:
            messagebox.showerror("Error", "ADFGX key word is out of the ALPHABET")
            raise ValueError("Keys out of range")
    return key_word


# Function for checking keyword for in ADFGVX (6x6)
def check_key36():
    ALPHABET_FULL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_word2 = Key2_input.get()
    key_word2 = remove_symbols(remove_accents(key_word2)).replace(" ", "").upper()

    for symbol in remove_accents(key_word2):
        if symbol not in ALPHABET_FULL:
            messagebox.showerror("Error", "ADFGVX key word is out of the ALPHABET")
            raise ValueError("Keys out of range")
    return key_word2


# Function for checking the plain text in ADFGX (5x5)
def check_plain25():
    NUMBERS = {'1': 'ZXONENZY', '2': 'ZXTWOWZY', '3': 'ZXTHREERZY', '4': 'ZXFOURZY', '5': 'ZXFIVEZY',
               '6': 'ZXSIXSZY', '7': 'ZXVSEVENZY', '8': 'ZXEIGHTXGY', '9': 'ZXNINEZY', '0': 'ZXZEROZY'}

    ALPHABET_FULL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = Input_text.get()

    # Removing spaces, diacritics and symbols from plain text
    message = remove_symbols(remove_accents(message)).replace(" ", "XQQX").upper()
    ABC = ALPHABET_gen25.get()
    choice = selection.get()

    if len(ABC) != 25:
        choice = 0

    # Replacement of numbers and unnecessary letters
    for symbol in message:
        if symbol not in ALPHABET_FULL:
            if symbol in NUMBERS:
                message = message.replace(symbol, NUMBERS[symbol])
            else:
                message = message.replace(symbol, '')
    if choice == 1:
        for symbol in message:
            if symbol == "Q":
                message = message.replace(symbol, "O")
    elif choice == 2:
        for symbol in message:
            if symbol == "W":
                message = message.replace(symbol, "V")
    return message


# Function for checking the plain text in ADFGVX (6x6)
def check_plain36():
    NUMBERS = {'1': 'ZXONENZY', '2': 'ZXTWOWZY', '3': 'ZXTHREERZY', '4': 'ZXFOURZY', '5': 'ZXFIVEZY',
               '6': 'ZXSIXSZY', '7': 'ZXVSEVENZY', '8': 'ZXEIGHTXGY', '9': 'ZXNINEZY', '0': 'ZXZEROZY'}

    ALPHABET_FULL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message2 = Input2_text.get()

    # Removing spaces, diacritics and symbols from plain text
    message2 = remove_symbols(remove_accents(message2)).replace(" ", "XQQX").upper()

    # Replacement of numbers
    for symbol in message2:
        if symbol not in ALPHABET_FULL:
            if symbol in NUMBERS:
                message2 = message2.replace(symbol, NUMBERS[symbol])
            else:
                message2 = message2.replace(symbol, '')
    return message2


# Function for checking the cipher text in ADFGX (5x5)
def check_cipher25():
    message = Input_text.get()
    ABC = ALPHABET_gen25.get()
    key_word = Key_input.get()

    spaces = 1
    if len(ABC) == 25:
        for symbol in message:
            if symbol not in "ADFGX ":
                messagebox.showerror("Error", "The input contains letters outside the ADFGX")
                break
            else:
                continue
    else:
        messagebox.showerror("Error", "The length of the alphabet must be exactly 25")
        raise ValueError("The length isn't 25")

    # Checking the equivalence of spaces
    for symbol in message:
        if symbol == " ":
            spaces = spaces + 1
    if spaces != len(key_word):
        messagebox.showerror("Error", "Spaces must be equal to the length of the keyword")
        raise ValueError("Spaces are not equal to the length of the keyword")
    return message


# Function for checking the cipher text in ADFGVX (6x6)
def check_cipher36():
    message2 = Input2_text.get()
    ABC36 = ALPHABET_gen36.get()
    key_word2 = Key2_input.get()

    spaces = 1
    if len(ABC36) == 36:
        for symbol in message2:
            if symbol not in "ADFGVX ":
                messagebox.showerror("Error", "The input contains letters outside the ADFGVX")
                break
            else:
                continue
    else:
        messagebox.showerror("Error", "The length of the alphabet must be exactly 36")
        raise ValueError("The length isn't 36")

    # Checking the equivalence of spaces
    for symbol in message2:
        if symbol == " ":
            spaces = spaces + 1
    if spaces != len(key_word2):
        messagebox.showerror("Error", "Spaces must be equal to the length of the keyword")
        raise ValueError("Spaces are not equal to the length of the keyword")
    return message2


# Function for checking the alphabet 5x5
def check_ABC25():
    ALPHABET_EN = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
    ALPHABET_CZ = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
    ABC25 = ALPHABET_gen25.get()
    choice = selection.get()

    ABC25 = remove_accents(ABC25).upper()

    for symbol in ABC25:
        # ENG
        if choice == 1:
            if symbol == "Q":
                messagebox.showerror("Error", "The ENG alphabet must not contain Q")
                break
            elif len(ABC25) != 25:
                messagebox.showerror("Error", "The length of the alphabet must be exactly 25")
                break
            elif symbol not in ALPHABET_EN:
                messagebox.showerror("Error", "Symbols in alphabetical input out of range")
                break
            else:
                continue
        # CZ
        elif choice == 2:
            if symbol == "W":
                messagebox.showerror("Error", "The CZ alphabet must not contain W")
                break
            elif len(ABC25) != 25:
                messagebox.showerror("Error", "The length of the alphabet must be exactly 25")
                break
            elif symbol not in ALPHABET_CZ:
                messagebox.showerror("Error", "Symbols in alphabetical input out of range")
                break
            else:
                continue
    return ABC25


#  Function for checking the alphabet 6x6
def check_ABC36():
    ALPHABET_FULL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    ABC36 = ALPHABET_gen36.get()
    ABC36 = remove_accents(ABC36).upper()

    for symbol in ABC36:
        if symbol not in ALPHABET_FULL:
            messagebox.showerror("Error", "Symbols in alphabetical input out of range")
        if len(ABC36) != 36:
            messagebox.showerror("Error", "The length of the alphabet must be exactly 36")
    return ABC36


# Function for encryption 5x5
def encrypt25():
    global Table_sub25, Table_tran25
    Output.delete(1.0, END)
    Table_sub25.destroy()
    Table_tran25.destroy()

    # Filtering input data
    message = check_plain25()
    ABC = check_ABC25()
    key_word = check_key25()

    # Creating an empty dictionary
    dictionary = {'AA': '', 'AD': '', 'AF': '', 'AG': '', 'AX': '', 'DA': '', 'DD': '', 'DF': '', 'DG': '', 'DX': '',
                  'FA': '', 'FD': '', 'FF': '', 'FG': '', 'FX': '', 'GA': '', 'GD': '', 'GF': '', 'GG': '', 'GX': '',
                  'XA': '', 'XD': '', 'XF': '', 'XG': '', 'XX': ''}

    # Insert input alphabet into dictionary
    d = {}
    l = ""
    indexPlainText = []

    for (key, value), symbol in zip(dictionary.items(), ABC):
        dictionary[key] = symbol
    for symbol in message:
        for key, value in dictionary.items():
            if symbol == value:
                indexPlainText.append(key)
        l = l.join(indexPlainText)

        d.update({l: symbol})
        l = ""

    # Print the substitution table
    Table_sub25 = Label(tab1, text=tabulate(d, headers=indexPlainText, tablefmt="pretty"), font=("Serif", 11),
                        relief="sunken")
    Table_sub25.grid(row=19, columns=8, sticky=N + N)

    # Bringing the ciphertext to the keyword
    indPT = ""
    indPT = indPT.join(indexPlainText)
    t = {}
    u = ""
    k = []

    for j, symbol in zip(range(len(key_word)), key_word):
        for i in range(0, len(indPT), len(key_word)):
            if (j + i) < len(indPT):
                k.append(indPT[j + i])
        u = u.join(k)

        t.update({u: symbol})
        k = []
        u = ""

    # Alphabetical sorting
    h = sorted(t.items(), key=lambda tt: tt[1])

    # Print the transposition table
    Table_tran25 = Label(tab1, text=[tabulate(t, headers=t, tablefmt="pretty")], font=("Serif", 11), relief="sunken")
    Table_tran25.grid(row=21, columns=2, sticky=N)

    # Print the cipher text
    out = ""
    STt = []
    for s in h:
        STt.append(s[0] + " ")
    out = out.join(STt)

    Output.insert(0.0, out)


# Function for decryption 5x5
def decrypt25():
    Output.delete(1.0, END)
    choice = selection.get()

    # Filtering input data
    message = check_cipher25()
    ABC = check_ABC25()
    key_word = check_key25()

    # Creating an empty dictionary
    dictionary = {'AA': '', 'AD': '', 'AF': '', 'AG': '', 'AX': '', 'DA': '', 'DD': '', 'DF': '', 'DG': '', 'DX': '',
                  'FA': '', 'FD': '', 'FF': '', 'FG': '', 'FX': '', 'GA': '', 'GD': '', 'GF': '', 'GG': '', 'GX': '',
                  'XA': '', 'XD': '', 'XF': '', 'XG': '', 'XX': ''}

    # Sorting the keyword
    sorted_word = sorted(key_word)
    for (key, value), symbol in zip(dictionary.items(), ABC):
        dictionary[key] = symbol

    # Splitting cipher text by spaces
    message = message.split(' ')
    t = {}
    b = {}
    c = []

    # Compare key word and sorted word
    for i, symbol in zip(range(len(key_word)), sorted_word):
        t.update({message[i]: symbol})
    for s, symbol in zip(range(len(key_word)), key_word):
        b.update({s: symbol})

    # Sort by original word and matching with a sorted word
    keys = list(t.keys())

    for j, s in zip(range(len(key_word)), key_word):
        for i, symbol in zip(range(len(key_word)), sorted_word):
            if s == symbol:
                if keys[i] in c:
                    continue
                else:
                    c.append(keys[i])
                    break

    # Sorting by indexes
    f = ""
    r = ""
    r = r.join(message)
    r = r + (len(key_word) - 1) * " "

    for j in range(len(r)):
        for i, symbol in zip(range(len(c)), c):
            f = f + c[i][j:j + 1]

    # Splitting the string in pairs
    outt = []
    keyd = list(dictionary.keys())
    o = []

    while f:
        o.append(f[:2])
        f = f[2:]
    for symbol in o:
        for i in range(len(dictionary)):
            if symbol == keyd[i]:
                outt.append(dictionary[keyd[i]])

    # Print the plain text
    # Replacing spaces and numbers
    out = ""
    out = out.join(outt)
    # ENG
    if choice == 1:
        out = out.replace("XOOX", " ")
        out = out.replace("ZXONENZY", "1")
        out = out.replace("ZXTWOWZY", "2")
        out = out.replace("ZXTHREERZY", "3")
        out = out.replace("ZXFOURZY", "4")
        out = out.replace("ZXFIVEZY", "5")
        out = out.replace("ZXSIXSZY", "6")
        out = out.replace("ZXVSEVENZY", "7")
        out = out.replace("ZXEIGHTXGY", "8")
        out = out.replace("ZXNINEZY", "9")
        out = out.replace("ZXZEROZY", "0")
    # CZ
    elif choice == 2:
        out = out.replace("XQQX", " ")
        out = out.replace("ZXONENZY", "1")
        out = out.replace("ZXTVOVZY", "2")
        out = out.replace("ZXTHREERZY", "3")
        out = out.replace("ZXFOURZY", "4")
        out = out.replace("ZXFIVEZY", "5")
        out = out.replace("ZXSIXSZY", "6")
        out = out.replace("ZXVSEVENZY", "7")
        out = out.replace("ZXEIGHTXGY", "8")
        out = out.replace("ZXNINEZY", "9")
        out = out.replace("ZXZEROZY", "0")

    Output.insert(0.0, out)


# Function for encryption 6x6
def encrypt36():
    global Table_sub36, Table_tran36
    Output2.delete(1.0, END)
    Table_sub36.destroy()
    Table_tran36.destroy()

    # Filtering input data
    message = check_plain36()
    ABC = check_ABC36()
    key_word = check_key36()

    # Creating an empty dictionary
    dictionary = {'AA': '', 'AD': '', 'AF': '', 'AG': '', 'AV': '', 'AX': '', 'DA': '', 'DD': '', 'DF': '', 'DG': '',
                  'DV': '', 'DX': '', 'FA': '', 'FD': '', 'FF': '', 'FG': '', 'FV': '', 'FX': '', 'GA': '', 'GD': '',
                  'GF': '', 'GG': '', 'GV': '', 'GX': '', 'VA': '', 'VD': '', 'VF': '', 'VG': '', 'VV': '', 'VX': '',
                  'XA': '', 'XD': '', 'XF': '', 'XG': '', 'XV': '', 'XX': ''}

    # Insert input alphabet into dictionary
    d = {}
    l = ""
    indexPlainText = []

    for (key, value), symbol in zip(dictionary.items(), ABC):
        dictionary[key] = symbol
    for symbol in message:
        for key, value in dictionary.items():
            if symbol == value:
                indexPlainText.append(key)
        l = l.join(indexPlainText)

        d.update({l: symbol})
        l = ""

    # Print the substitution table
    Table_sub36 = Label(tab2, text=tabulate(d, headers=indexPlainText, tablefmt="pretty"), font=("Serif", 11),
                        relief="sunken")
    Table_sub36.grid(row=18, columns=8, sticky=N)

    # Bringing the ciphertext to the keyword
    indPT = ""
    indPT = indPT.join(indexPlainText)
    t = {}
    u = ""
    k = []

    for j, symbol in zip(range(len(key_word)), key_word):
        for i in range(0, len(indPT), len(key_word)):
            if (j + i) < len(indPT):
                k.append(indPT[j + i])
        u = u.join(k)

        t.update({u: symbol})
        k = []
        u = ""

    # Alphabetical sorting
    h = sorted(t.items(), key=lambda tt: tt[1])

    # Print the transposition table
    Table_tran36 = Label(tab2, text=[tabulate(t, headers=t, tablefmt="pretty")], font=("Serif", 11), relief="sunken")
    Table_tran36.grid(row=20, columns=2, sticky=N)

    # Print the cipher text
    out = ""
    STt = []
    for s in h:
        STt.append(s[0] + " ")
    out = out.join(STt)

    Output2.insert(0.0, out)


# Function for decryption 6x6
def decrypt36():
    Output2.delete(1.0, END)

    # Filtering input data
    message = check_cipher36()
    ABC = check_ABC36()
    key_word = check_key36()

    # Creating an empty dictionary
    dictionary = {'AA': '', 'AD': '', 'AF': '', 'AG': '', 'AV': '', 'AX': '', 'DA': '', 'DD': '', 'DF': '', 'DG': '',
                  'DV': '', 'DX': '', 'FA': '', 'FD': '', 'FF': '', 'FG': '', 'FV': '', 'FX': '', 'GA': '', 'GD': '',
                  'GF': '', 'GG': '', 'GV': '', 'GX': '', 'VA': '', 'VD': '', 'VF': '', 'VG': '', 'VV': '', 'VX': '',
                  'XA': '', 'XD': '', 'XF': '', 'XG': '', 'XV': '', 'XX': ''}

    # Sorting the keyword
    sorted_word = sorted(key_word)
    for (key, value), symbol in zip(dictionary.items(), ABC):
        dictionary[key] = symbol

    # Splitting cipher text by spaces
    message = message.split(' ')
    t = {}
    b = {}
    c = []

    # Compare key word and sorted word
    for i, symbol in zip(range(len(key_word)), sorted_word):
        t.update({message[i]: symbol})
    for s, symbol in zip(range(len(key_word)), key_word):
        b.update({s: symbol})

    # Sort by original word and matching with a sorted word
    keys = list(t.keys())

    for j, s in zip(range(len(key_word)), key_word):
        for i, symbol in zip(range(len(key_word)), sorted_word):
            if s == symbol:
                if keys[i] in c:
                    continue
                else:
                    c.append(keys[i])
                    break

    # Sorting by indexes
    f = ""
    r = ""
    r = r.join(message)
    r = r + (len(key_word) - 1) * " "

    for j in range(len(r)):
        for i, symbol in zip(range(len(c)), c):
            f = f + c[i][j:j + 1]

    # Splitting the string in pairs
    outt = []
    keyd = list(dictionary.keys())
    o = []

    while f:
        o.append(f[:2])
        f = f[2:]
    for symbol in o:
        for i in range(len(dictionary)):
            if symbol == keyd[i]:
                outt.append(dictionary[keyd[i]])

    # Print the plain text
    # Replacing spaces and numbers
    out = ""
    out = out.join(outt)
    out = out.replace("XQQX", " ")
    out = out.replace("ZXONENZY", "1")
    out = out.replace("ZXTWOWZY", "2")
    out = out.replace("ZXTHREERZY", "3")
    out = out.replace("ZXFOURZY", "4")
    out = out.replace("ZXFIVEZY", "5")
    out = out.replace("ZXSIXSZY", "6")
    out = out.replace("ZXVSEVENZY", "7")
    out = out.replace("ZXEIGHTXGY", "8")
    out = out.replace("ZXNINEZY", "9")
    out = out.replace("ZXZEROZY", "0")

    Output2.insert(0.0, out)


# Configuration of GUI
# Label and Buttons
########################################################################################################################

# Basic Settings
style = ttk.Style()
root.title("ADFG(V)X Cipher Application")
root.geometry("1280x660")

style.configure("TLabel", font="Serif 15", padding=10)
style.configure("TButton", font="Serif 15", padding=10)
style.configure("TEntry", font="Serif 18", padding=10)

tabControl.add(tab1, text="ADFGX")
tabControl.add(tab2, text="ADFGVX")
tabControl.pack(expand=1, fill="both")
########################################################################################################################

# INPUT LABELS
# ADFGX
Input_label = tk.Label(tab1, text="Input text", fg="lightgreen")
Input_label.grid(row=0, column=0, sticky=N + W)
Input_clear = tk.Button(tab1, text="Clear", command=lambda: clear('input'))
Input_clear.grid(row=1, column=0, sticky=N + W)
Input_paste = tk.Button(tab1, text="Paste", command=lambda: paste('input'))
Input_paste.grid(row=2, column=0, sticky=N + W)
###################################

# ADFGVX
Input2_label = tk.Label(tab2, text="Input text", fg="lightgreen")
Input2_label.grid(row=0, column=0)
Input2_clear = tk.Button(tab2, text="Clear", command=lambda: clear('input2'))
Input2_clear.grid(row=1, column=0)
Input2_paste = tk.Button(tab2, text="Paste", command=lambda: paste('input2'))
Input2_paste.grid(row=2, column=0)
########################################################################################################################

# KEY LABELS
# ADFGX
Key_label = tk.Label(tab1, text="Key Word", fg="lightblue")
Key_label.grid(row=5, column=0)
Key_clear = tk.Button(tab1, text="Clear", command=lambda: clear('key'))
Key_clear.grid(row=6, column=0)
###################################

# ADFGVX
Key2_label = tk.Label(tab2, text="Key Word", fg="lightblue")
Key2_label.grid(row=5, column=0)
Key2_clear = tk.Button(tab2, text="Clear", command=lambda: clear('key2'))
Key2_clear.grid(row=6, column=0)
########################################################################################################################

# ALPHABET LABELS
# ADFGX
ALPHABET25_label = tk.Label(tab1, text="Generated Alphabet", fg="cyan")
ALPHABET25_label.grid(row=7, column=3)
ALPHABET25_clear = tk.Button(tab1, text="Clear", command=lambda: clear('alphabet25'))
ALPHABET25_clear.grid(row=8, column=0)
###################################

# ADFGVX
ALPHABET36_label = tk.Label(tab2, text="Generated Alphabet", fg="cyan")
ALPHABET36_label.grid(row=7, column=3)
ALPHABET36_clear = tk.Button(tab2, text="Clear", command=lambda: clear('alphabet36'))
ALPHABET36_clear.grid(row=8, column=0)
########################################################################################################################

# OUTPUT LABELS
# ADFGX
Output_label = tk.Label(tab1, text="Output", fg="red")
Output_label.grid(row=15, column=0)
Output_clear = tk.Button(tab1, text="Clear", command=lambda: clear('output'))
Output_clear.grid(row=16, column=0)
Output_copy = tk.Button(tab1, border=4, text="Copy", command=lambda: copy('output'))
Output_copy.grid(row=17, column=0)
###################################

# ADFGVX
Output2_label = tk.Label(tab2, text="Output", fg="red")
Output2_label.grid(row=14, column=0)
Output2_clear = tk.Button(tab2, text="Clear", command=lambda: clear('output2'))
Output2_clear.grid(row=15, column=0)
Output2_copy = tk.Button(tab2, border=4, text="Copy", command=lambda: copy('output2'))
Output2_copy.grid(row=16, column=0)
########################################################################################################################

# LABELS OF TABLES
# Substitution table
# ADFGX
SUBSTITUTION_TABLE25_label = tk.Label(tab1, text="Substitution Table", fg="magenta")
SUBSTITUTION_TABLE25_label.grid(row=18, column=3)

# ADFGVX
SUBSTITUTION_TABLE36_label = tk.Label(tab2, text="Substitution Table", fg="magenta")
SUBSTITUTION_TABLE36_label.grid(row=17, column=3)
###################################

# Transposition table
# ADFGX
TRANSPOSITION_TABLE25_label = tk.Label(tab1, text="Transposition Table", fg="yellow")
TRANSPOSITION_TABLE25_label.grid(row=20, column=1)

# ADFGVX
TRANSPOSITION_TABLE36_label = tk.Label(tab2, text="Transposition Table", fg="yellow")
TRANSPOSITION_TABLE36_label.grid(row=19, column=1)
###################################

# Table of the generated alphabet
# ADFGX
GENERATED_TABLE25_label = tk.Label(tab1, text="Generated Table", fg="green")
GENERATED_TABLE25_label.grid(row=20, column=5)

# ADFGVX
GENERATED_TABLE36_label = tk.Label(tab2, text="Generated Table", fg="green")
GENERATED_TABLE36_label.grid(row=19, column=5)
########################################################################################################################

# ENCRYPT, DECRYPT AND GENERATE
# Buttons for generate table
# ADFGX
generate25_button = ttk.Button(tab1, text="Generate", command=lambda: generateALPHABET25())
generate25_button.grid(row=8, column=6)

# ADFGVX
generate36_button = ttk.Button(tab2, text="Generate", command=lambda: generateAPLHABET36())
generate36_button.grid(row=8, column=6)
###################################

# Buttons for encrypt
# ADFGX
encrypt25_button = ttk.Button(tab1, text="Encrypt", command=lambda: encrypt25())
encrypt25_button.grid(row=14, column=2, sticky=N)

# ADFGVX
encrypt36_button = ttk.Button(tab2, text="Encrypt", command=lambda: encrypt36())
encrypt36_button.grid(row=13, column=2)
###################################

# Buttons for decryption
# ADFGX
decrypt25_button = ttk.Button(tab1, text="Decrypt", command=lambda: decrypt25())
decrypt25_button.grid(row=14, column=4, sticky=N)

# ADFGVX
decrypt36_button = ttk.Button(tab2, text="Decrypt", command=lambda: decrypt36())
decrypt36_button.grid(row=13, column=4)
########################################################################################################################


# Other GUI buttons
# Function for cleaning fields
def clear(str_val):
    if str_val == 'key':
        Key_input.delete(0, 'end')
    elif str_val == 'key2':
        Key2_input.delete(0, 'end')
    elif str_val == 'input':
        Input_text.delete(0, 'end')
    elif str_val == 'input2':
        Input2_text.delete(0, 'end')
    elif str_val == 'alphabet25':
        ALPHABET_gen25.delete(0, 'end')
    elif str_val == 'alphabet36':
        ALPHABET_gen36.delete(0, 'end')
    elif str_val == 'output':
        Output.delete(0.0, 'end')
    else:
        Output2.delete(0.0, 'end')


# Function for simply copying text from Output
def copy(str_val):
    root.clipboard_clear()  # Optional
    if str_val == 'output':
        root.clipboard_append(Output.get('1.0', tk.END).rstrip())
        root.update()
    else:
        root.clipboard_append(Output2.get('1.0', tk.END).rstrip())
        root.update()


# Function for simply pasting text to the Input
def paste(str_val):
    if str_val == 'input':
        Input_text.delete(0, 'end')
        Input_text.insert(tk.END, root.clipboard_get())
    else:
        Input2_text.delete(0, 'end')
        Input2_text.insert(tk.END, root.clipboard_get())


# Ending GUI
root.mainloop()
