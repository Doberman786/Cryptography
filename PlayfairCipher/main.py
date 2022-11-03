# Import Tkinter library
import unicodedata
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Starting GUI
root = Tk()

# Input and output fields
input_text = Text(root, width=110, height=3, font=("Serif", 14))
input_text.grid(row=5, column=1, rowspan=5, columnspan=5, sticky=W + N)

cipher = ttk.Entry(root, width=107)
cipher.grid(row=0, column=1, rowspan=4, columnspan=4, sticky=W + N)

Output = Text(root, width=110, height=3, font=("Serif", 14))
Output.grid(row=11, column=1, rowspan=4, columnspan=4, sticky=W + N)

Table = tk.Label(root, text="\n \n \n \n", width=17, font=('Serif', 11), relief="sunken")
Table.grid(row=15, column=3)

Pairs = Text(root, width=110, height=3, font=("Serif", 14), relief="sunken")
Pairs.grid(row=17, column=1, rowspan=4, columnspan=4, sticky=W + N)

# Language selection buttons
selection = IntVar()
Radiobutton(root, text="EN", variable=selection, value=1).grid(row=8, column=1)
Radiobutton(root, text="CZ", variable=selection, value=2).grid(row=8, column=2)
selection.set(1)


# Function for removing symbols from string
def remove_symbols(text):
    return text.translate({ord(i): None for i in r"""!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""})


# Function for removing diacritics from string
def remove_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


# Function for checking key word
def check_key(key_word):
    NUMBERS = "1234567890"
    for symbol in key_word.upper():
        if symbol in NUMBERS:
            messagebox.showerror("Error", "Key word must not contains numbers")
            break
        else:
            continue


# Function for encryption
def encrypt():
    global i1, i2, j1, j2
    Output.delete(1.0, END)
    choice = selection.get()
    Pairs.delete(1.0, END)
    temp = input_text.get(1.0, END)
    temp1 = cipher.get()
    if temp != "" and temp1 != "":

        message = temp
        key_word = temp1
        check_key(key_word)  # Checking the key word

        # Removing spaces and make UPPERCASE in key word and input message
        # Removing symbols and replace diacritics
        key_word = remove_symbols(remove_accents(key_word)).replace(" ", "").upper()
        message = remove_symbols(remove_accents(message)).replace(" ", "XQQX").upper()

        NUMBERS = {'1': 'ZXONENZY', '2': 'ZXTWOWZY', '3': 'ZXTHREERZY', '4': 'ZXFOURZY', '5': 'ZXFIVEZY',
                   '6': 'ZXSIXSZY', '7': 'ZXVSEVENZY', '8': 'ZXEIGHTXGY', '9': 'ZXNINEZY', '0': 'ZXZEROZY'}

        ALPHABET_FULL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ALPHABET_EN = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        ALPHABET_CZ = "ABCDEFGHIJKLMNOPQRSTUVXYZ"

        # Check key word input (non-repeating letters)
        r = []
        for symbol in key_word:
            if symbol not in r:
                r.append(symbol)
        g = ""
        g = g.join(r)

        # Check plain entry
        # Replacing numbers
        for symbol in message:
            if symbol not in ALPHABET_FULL:
                if symbol in NUMBERS:
                    message = message.replace(symbol, NUMBERS[symbol])
                else:
                    message = message.replace(symbol, '')

        table = []

        # Encryption for ENG
        if choice == 1:

            # Replacing letters for ENG
            for symbol in g:
                for smbl in message:
                    if symbol == "J":
                        g = g.replace("J", "I")
                    if smbl == "J":
                        message = message.replace("J", "I")
            for symbol in g:
                table.append(symbol)

            s = ""
            # Double letters check
            for symbol in message:
                if symbol == s:
                    if symbol != "X":
                        message = message.replace(symbol + s, symbol + "X" + symbol)
                    if symbol != "Z":
                        message = message.replace(symbol + s, symbol + "Z" + symbol)

                # Add letter, at odd number of characters
                s = symbol
            if len(message) % 2 == 1:
                if s != "X":
                    message = message + "X"
                if s != "Z":
                    message = message + "Z"

            # Filling out the table
            for symbol in ALPHABET_EN:
                for s in g:
                    if s == symbol:
                        ALPHABET_EN = ALPHABET_EN.replace(symbol, "")

            text = ""
            text = text.join(r)
            cipher_table = text + ALPHABET_EN

            le = len(cipher_table)
            le = le - 25
            cipher_table = cipher_table[:len(cipher_table) - le]

            h = list(cipher_table)
            h1 = h[:5]
            h2 = h[5:10]
            h3 = h[10:15]
            h4 = h[15:20]
            h5 = h[20:25]

            table = [h1, h2, h3, h4, h5]
            table_print = ""

            # Print the table
            for i in range(5):
                if i > 0:
                    table_print = table_print + "\n"
                for j in range(5):
                    table_print = table_print + "  " + table[i][j] + "  "

            Table_output = Label(root, text=table_print, font=('Serif', 11), relief="sunken")
            Table_output.grid(row=15, column=3)

            # Splitting the message into pairs
            message = [message[i:i + 2] for i in range(0, len(message), 2)]

            # Print the pairs
            pairs = str(message)
            Pairs.insert(END, pairs)

            # Encrypt algorithm
            key_table = []
            out = ""
            g = 0
            e = 0
            for symbol in message:
                for i in range(5):
                    for j in range(5):
                        if symbol[:1] == table[i][j]:
                            i1 = i
                            j1 = j
                            g = 1
                        if symbol[1:2] == table[i][j]:
                            i2 = i
                            j2 = j
                            e = 1
                        if g == 1 and e == 1:
                            g = 0
                            e = 0
                            if i1 == i2:
                                j1 = (j1 + 1) % 5
                                j2 = (j2 + 1) % 5
                                key_table.append(table[i1][j1])
                                key_table.append(table[i2][j2])
                            elif j1 == j2:
                                i1 = (i1 + 1) % 5
                                i2 = (i2 + 1) % 5
                                key_table.append(table[i1][j1])
                                key_table.append(table[i2][j2])
                            else:
                                key_table.append(table[i1][j2])
                                key_table.append(table[i2][j1])

            # Print decryption string
            out = out.join(key_table)
            out = [out[i:i + 5] for i in range(0, len(out), 5)]
            vys = ""
            vys = vys.join(out[i] + " " for i in range(len(out)))
            Output.insert(END, vys)

        # Encryption for CZ
        if choice == 2:

            # Replacing letters for CZ
            for symbol in g:
                for smbl in message:
                    if symbol == "W":
                        g = g.replace("W", "V")
                    if smbl == "W":
                        message = message.replace("W", "V")
            for symbol in g:
                table.append(symbol)

            s = ""
            # Double letters check
            for symbol in message:
                if symbol == s:
                    if symbol != "X":
                        message = message.replace(symbol + s, symbol + "X" + symbol)
                    if symbol != "Z":
                        message = message.replace(symbol + s, symbol + "Z" + symbol)

                # Add letter, at odd number of characters
                s = symbol
            if len(message) % 2 == 1:
                if s != "X":
                    message = message + "X"
                if s != "Z":
                    message = message + "Z"

            # Filling out the table
            for symbol in ALPHABET_CZ:
                for s in g:
                    if s == symbol:
                        ALPHABET_CZ = ALPHABET_CZ.replace(symbol, "")

            text = ""
            text = text.join(g)
            cipher_table = text + ALPHABET_CZ

            le = len(cipher_table)
            le = le - 25
            cipher_table = cipher_table[:len(cipher_table) - le]

            h = list(cipher_table)
            h1 = h[:5]
            h2 = h[5:10]
            h3 = h[10:15]
            h4 = h[15:20]
            h5 = h[20:25]

            table = [h1, h2, h3, h4, h5]

            # Print the table
            table_print = ""
            for i in range(5):
                if i > 0:
                    table_print = table_print + "\n"
                for j in range(5):
                    table_print = table_print + "  " + table[i][j] + "  "

            Table_output = Label(root, text=table_print, font=('Serif', 11), relief="sunken")
            Table_output.grid(row=15, column=3)

            # Splitting the message into pairs
            message = [message[i:i + 2] for i in range(0, len(message), 2)]

            # Print the pairs
            pairs = str(message)
            Pairs.insert(END, pairs)

            # Encrypt algorithm
            key_table = []
            out = ""
            g = 0
            e = 0
            for symbol in message:
                for i in range(5):
                    for j in range(5):
                        if symbol[:1] == table[i][j]:
                            i1 = i
                            j1 = j
                            g = 1
                        if symbol[1:2] == table[i][j]:
                            i2 = i
                            j2 = j
                            e = 1
                        if g == 1 and e == 1:
                            g = 0
                            e = 0
                            if i1 == i2:
                                j1 = (j1 + 1) % 5
                                j2 = (j2 + 1) % 5
                                key_table.append(table[i1][j1])
                                key_table.append(table[i2][j2])
                            elif j1 == j2:
                                i1 = (i1 + 1) % 5
                                i2 = (i2 + 1) % 5
                                key_table.append(table[i1][j1])
                                key_table.append(table[i2][j2])
                            else:
                                key_table.append(table[i1][j2])
                                key_table.append(table[i2][j1])

            # Print decryption string
            out = out.join(key_table)
            out = [out[i:i + 5] for i in range(0, len(out), 5)]
            text_out = ""
            text_out = text_out.join(out[i] + " " for i in range(len(out)))
            Output.insert(END, text_out)
    else:
        messagebox.showerror("Error", "You must enter the message you want to encrypt and the key word")


# Function for decryption
def decrypt():
    global i1, i2, j1, j2
    Output.delete(1.0, END)
    choice = selection.get()
    temp = input_text.get(1.0, END)
    temp1 = cipher.get()
    t = 0

    if temp != "" and temp1 != "":
        message = temp
        key_word = temp1
        check_key(key_word)  # Checking the key word

        # Removing spaces and make UPPERCASE in key word and input message
        # Removing symbols and replace diacritics
        key_word = remove_symbols(remove_accents(key_word)).replace(" ", "").upper()
        message = remove_symbols(remove_symbols(message)).replace(" ", "").upper()

        NUMBERS = {'1': 'ZXONENZY', '2': 'ZXTWOWZY', '3': 'ZXTHREERZY', '4': 'ZXFOURZY', '5': 'ZXFIVEZY',
                   '6': 'ZXSIXSZY', '7': 'ZXVSEVENZY', '8': 'ZXEIGHTXGY', '9': 'ZXNINEZY', '0': 'ZXZEROZY'}

        # Check cipher entry
        for sym in message:
            if sym in NUMBERS:
                messagebox.showerror("Error", "Cipher text must not contains numbers")
                t = 1
                break
            if t == 1:
                break
        if t != 1:
            ALPHABET_EN = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
            ALPHABET_CZ = "ABCDEFGHIJKLMNOPQRSTUVXYZ"

            # Check key word input (non-repeating letters)
            r = []
            for symbol in key_word:
                if symbol not in r:
                    r.append(symbol)
            g = ""
            g = g.join(r)

            # Decryption for ENG
            if choice == 1:
                if "J" in g or "J" in message:
                    messagebox.showerror("Error", "ENG decrypt must not contain J")
                else:
                    # Filling out the table
                    for symbol in ALPHABET_EN:
                        for s in g:
                            if s == symbol:
                                ALPHABET_EN = ALPHABET_EN.replace(symbol, "")

                    text = ""
                    text = text.join(g)
                    cipher_table = text + ALPHABET_EN

                    le = len(cipher_table)
                    le = le - 25
                    cipher_table = cipher_table[:len(cipher_table) - le]

                    h = list(cipher_table)
                    h1 = h[:5]
                    h2 = h[5:10]
                    h3 = h[10:15]
                    h4 = h[15:20]
                    h5 = h[20:25]

                    table = [h1, h2, h3, h4, h5]
                    table_print = ""

                    # Print the table
                    for i in range(5):
                        if i > 0:
                            table_print = table_print + "\n"
                        for j in range(5):
                            table_print = table_print + "  " + table[i][j] + "  "

                    Table_output = Label(root, text=table_print, font=('Serif', 11), relief="sunken")
                    Table_output.grid(row=15, column=3)

                    # Splitting the message into pairs
                    message = [message[i:i + 2] for i in range(0, len(message), 2)]

                    # Decryption algorithm
                    g = 0
                    e = 0
                    out = ""
                    key_table = []
                    for symbol in message:
                        for i in range(5):
                            for j in range(5):
                                if symbol[:1] == table[i][j]:
                                    i1 = i
                                    j1 = j
                                    g = 1
                                if symbol[1:2] == table[i][j]:
                                    i2 = i
                                    j2 = j
                                    e = 1
                                if g == 1 and e == 1:
                                    g = 0
                                    e = 0
                                    if i1 == i2:
                                        j1 = (j1 - 1) % 5
                                        j2 = (j2 - 1) % 5
                                        key_table.append(table[i1][j1])
                                        key_table.append(table[i2][j2])
                                    elif j1 == j2:
                                        i1 = (i1 - 1) % 5
                                        i2 = (i2 - 1) % 5
                                        key_table.append(table[i1][j1])
                                        key_table.append(table[i2][j2])
                                    else:
                                        key_table.append(table[i1][j2])
                                        key_table.append(table[i2][j1])

                    # Print decryption string
                    # Replacing numbers and spaces
                    out = out.join(str(key_table))
                    out = out.replace("]", "")
                    out = out.replace("[", "")
                    out = out.replace(",", "")
                    out = out.replace("'", "")
                    out = out.replace(" ", "")
                    out = out.replace("XQXQX", " ")
                    out = out.replace("ZXONENZY", "1")
                    out = out.replace("ZXTWOWZY", "2")
                    out = out.replace("ZXTHREXERZY", "3")
                    out = out.replace("ZXFOURZY", "4")
                    out = out.replace("ZXFIVEZY", "5")
                    out = out.replace("ZXSIXSZY", "6")
                    out = out.replace("ZXVSEVENZY", "7")
                    out = out.replace("ZXEIGHTXGY", "8")
                    out = out.replace("ZXNINEZY", "9")
                    out = out.replace("ZXZEROZY", "0")

                    # Delete extra letters
                    if out[-1] == "X":
                        out = out[:-1]
                    elif out[-1] == "Z":
                        out = out[:-1]
                    else:
                        pass
                    Output.insert(END, out)

            # Decryption for CZ
            if choice == 2:
                if "W" in message or "W" in g:
                    messagebox.showerror("Error", "CZ decrypt must not contain W")
                else:
                    # Filling out the table
                    for symbol in ALPHABET_CZ:
                        for s in g:
                            if s == symbol:
                                ALPHABET_CZ = ALPHABET_CZ.replace(symbol, "")
                    text = ""
                    text = text.join(g)
                    cipher_table = text + ALPHABET_CZ

                    le = len(cipher_table)
                    le = le - 25
                    cipher_table = cipher_table[:len(cipher_table) - le]

                    h = list(cipher_table)
                    h1 = h[:5]
                    h2 = h[5:10]
                    h3 = h[10:15]
                    h4 = h[15:20]
                    h5 = h[20:25]

                    table = [h1, h2, h3, h4, h5]
                    table_print = ""

                    # Print the table
                    for i in range(5):
                        if i > 0:
                            table_print = table_print + "\n"
                        for j in range(5):
                            table_print = table_print + "  " + table[i][j] + "  "

                    Table_output = Label(root, text=table_print, font=('Serif', 11), relief="sunken")
                    Table_output.grid(row=15, column=3)

                    # Splitting the message into pairs
                    message = [message[i:i + 2] for i in range(0, len(message), 2)]

                    # Decryption algorithm
                    g = 0
                    e = 0
                    out = ""
                    key_table = []
                    for symbol in message:
                        for i in range(5):
                            for j in range(5):
                                if symbol[:1] == table[i][j]:
                                    i1 = i
                                    j1 = j
                                    g = 1
                                if symbol[1:2] == table[i][j]:
                                    i2 = i
                                    j2 = j
                                    e = 1
                                if g == 1 and e == 1:
                                    g = 0
                                    e = 0
                                    if i1 == i2:
                                        j1 = (j1 - 1) % 5
                                        j2 = (j2 - 1) % 5
                                        key_table.append(table[i1][j1])
                                        key_table.append(table[i2][j2])
                                    elif j1 == j2:
                                        i1 = (i1 - 1) % 5
                                        i2 = (i2 - 1) % 5
                                        key_table.append(table[i1][j1])
                                        key_table.append(table[i2][j2])
                                    else:
                                        key_table.append(table[i1][j2])
                                        key_table.append(table[i2][j1])

                    # Print decryption string
                    # Replacing numbers and spaces
                    out = out.join(str(key_table))
                    out = out.replace("]", "")
                    out = out.replace("[", "")
                    out = out.replace(",", "")
                    out = out.replace("'", "")
                    out = out.replace(" ", "")
                    out = out.replace("XQXQX", " ")
                    out = out.replace("ZXONENZY", "1")
                    out = out.replace("ZXTVOVZY", "2")
                    out = out.replace("ZXTHREXERZY", "3")
                    out = out.replace("ZXFOURZY", "4")
                    out = out.replace("ZXFIVEZY", "5")
                    out = out.replace("ZXSIXSZY", "6")
                    out = out.replace("ZXVSEVENZY", "7")
                    out = out.replace("ZXEIGHTXGY", "8")
                    out = out.replace("ZXNINEZY", "9")
                    out = out.replace("ZXZEROZY", "0")

                    # Delete extra letters
                    if out[-1] == "X":
                        out = out[:-1]
                    elif out[-1] == "Z":
                        out = out[:-1]
                    else:
                        pass
                    Output.insert(END, out)
    else:
        messagebox.showerror("Error", "You must enter the message you want to decrypt and the key word")


# Configuration of GUI
# Labels and Buttons
style = ttk.Style()
root.geometry("1100x400")
root.title("Playfair Cipher Application")

style.configure("TLabel",
                font="Serif 15",
                padding=10)
style.configure("TButton",
                font="Serif 15",
                padding=10)
style.configure("TEntry",
                font="Serif 18",
                padding=10)

input_label = tk.Label(root, text="Input", fg="Lightgreen")
input_label.grid(row=4, column=0)
input_clear = tk.Button(root, text="Clear", command=lambda: clear('input'))
input_clear.grid(row=5, column=0)

pst = tk.Button(root, border=4, text="Paste", command=lambda: paste())
pst.grid(row=6, column=0)

cipher_label = tk.Label(root, text="Key word", fg="Lightblue")
cipher_label.grid(row=1, column=0)
cipher_clear = tk.Button(root, text="Clear", command=lambda: clear('key'))
cipher_clear.grid(row=2, column=0)

output_label = tk.Label(root, text="Output", fg="red")
output_label.grid(row=10, column=0)
output_clear = tk.Button(root, text="Clear", command=lambda: clear('output'))
output_clear.grid(row=11, column=0)

cp = tk.Button(root, border=4, text="Copy", command=lambda: copy())
cp.grid(row=12, column=0)

pairs_label = tk.Label(root, text="Pairs", fg="yellow")
pairs_label.grid(row=18, column=0)
pairs_clear = tk.Button(root, text="Clear", command=lambda: clear('pairs'))
pairs_clear.grid(row=19, column=0)

encrypt_button = ttk.Button(root, text="«Encipher»", command=lambda: encrypt())
encrypt_button.grid(row=8, column=3)
decrypt_button = ttk.Button(root, text="«Decipher»", command=lambda: decrypt())
decrypt_button.grid(row=8, column=4)

table_label = tk.Label(root, text="Generated table »»»", fg="green")
table_label.grid(row=15, column=2)


# Function for cleaning fields
def clear(str_val):
    if str_val == 'key':
        cipher.delete(0, 'end')
    elif str_val == 'input':
        input_text.delete(0.0, 'end')
    elif str_val == 'pairs':
        Pairs.delete(0.0, 'end')
    else:
        Output.delete(0.0, 'end')


# Function for simply copying text from Output
def copy():
    root.clipboard_clear()  # Optional
    root.clipboard_append(Output.get('1.0', tk.END).rstrip())
    root.update()


# Function for simply pasting text to the Input
def paste():
    input_text.insert(tk.END, root.clipboard_get())


# Ending GUI
root.mainloop()
