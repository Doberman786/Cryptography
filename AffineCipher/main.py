import math
import unicodedata
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

SOURCE_ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                   "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def remove_symbols(text):
    return text.translate({ord(i): None for i in r"""!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""})


def remove_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def check_keys(key1, key2):
    if key1 < 0 or key2 <= 0 or key2 > len(SOURCE_ALPHABET) - 1:
        messagebox.showerror("Error", "Key 1 must be greater than 0 and Key 2 must "
                                      f"be between 1 and {len(SOURCE_ALPHABET)}")
        raise ValueError("Keys out of range")
    if math.gcd(key1, len(SOURCE_ALPHABET)) != 1:
        messagebox.showerror("Error", f"Key 1 {key1} and the symbol set size {len(SOURCE_ALPHABET)} "
                                      "are not relatively prime. Choose a different key.")
        raise ValueError("Unable to find GCD")


def encrypt(plaintext, key1, key2):
    check_keys(key1, key2)
    ciphertext = ""

    for symbol in remove_accents(plaintext.upper().replace(" ", "XQQX")):
        if symbol in SOURCE_ALPHABET:
            # Encrypt the symbol:
            symbolIndex = SOURCE_ALPHABET.index(symbol)
            ciphertext += SOURCE_ALPHABET[(symbolIndex * key1 + key2) % len(SOURCE_ALPHABET)]
        else:
            ciphertext += symbol  # Append the symbol without encrypting.
    return remove_symbols(ciphertext)


def decrypt(ciphertext, key1, key2):
    global inv_key1
    check_keys(key1, key2)
    plaintext = ""

    for x in range(1, 36):
        if (key1 * x) % 36 == 1:
            inv_key1 = x

    for symbol in ciphertext.upper():
        if symbol in SOURCE_ALPHABET:
            # Decrypt the symbol:
            symbolIndex = SOURCE_ALPHABET.index(symbol)
            plaintext += SOURCE_ALPHABET[(symbolIndex - key2) *
                                 inv_key1 % len(SOURCE_ALPHABET)]
        else:
            plaintext += symbol  # Append the symbol without decrypting.
    return plaintext.replace("XQQX", " ")


class AffineCipher:

    def __init__(self, root):
        self.plain_text = tk.StringVar(root, value="")
        self.cipher_text = tk.StringVar(root, value="")
        self.key1 = tk.IntVar(root)
        self.key2 = tk.IntVar(root)

        root.title("Affine Cipher Application")

        style = ttk.Style()
        style.configure("TLabel",
                        font="Serif 15",
                        padding=10)
        style.configure("TButton",
                        font="Serif 15",
                        padding=10)
        style.configure("TEntry",
                        font="Serif 18",
                        padding=10)

        self.plain_label = tk.Label(root, text="Plain text", fg="lightgreen")
        self.plain_label.grid(row=1, column=0)

        self.plain_entry = ttk.Entry(root, textvariable=self.plain_text, width=50)
        self.plain_entry.grid(row=0, column=1, rowspan=4, columnspan=4)

        self.plain_clear = tk.Button(root, text="Clear", command=lambda: self.clear('plain'))
        self.plain_clear.grid(row=2, column=0)

        self.key1_label = tk.Label(root, text="Key 1")
        self.key1_label.grid(row=4, column=0)

        self.key1_entry = tk.Entry(root, textvariable=self.key1)
        self.key1_entry.grid(row=4, column=1)

        self.key2_label = tk.Label(root, text="Key 2")
        self.key2_label.grid(row=5, column=0)

        self.key2_entry = tk.Entry(root, textvariable=self.key2)
        self.key2_entry.grid(row=5, column=1)

        self.encrypt_button = ttk.Button(root, text="↓ Encipher ↓", command=lambda: self.encrypt_press())
        self.encrypt_button.grid(row=4, column=3)

        self.decrypt_button = ttk.Button(root, text="↑ Decipher ↑", command=lambda: self.decrypt_press())
        self.decrypt_button.grid(row=4, column=4)

        self.cipher_label = tk.Label(root, text="Cipher text", fg="red")
        self.cipher_label.grid(row=7, column=0)

        self.cipher_entry = ttk.Entry(root, textvariable=self.cipher_text, width=50)
        self.cipher_entry.grid(row=6, column=1, rowspan=4, columnspan=4)

        self.cipher_clear = tk.Button(root, text="Clear", command=lambda: self.clear('cipher'))
        self.cipher_clear.grid(row=8, column=0)

    def clear(self, str_val):
        if str_val == 'cipher':
            self.cipher_entry.delete(0, 'end')
        else:
            self.plain_entry.delete(0, 'end')

    def get_key(self):
        key1_val = self.key1.get()
        key2_val = self.key2.get()
        return key1_val, key2_val

    def encrypt_press(self):
        key1, key2 = self.get_key()
        cipher_text = encrypt(self.plain_entry.get(), key1, key2)
        self.cipher_entry.delete(0, "end")
        self.cipher_entry.insert(0, cipher_text)

    def decrypt_press(self):
        key1, key2 = self.get_key()
        plain_text = decrypt(self.cipher_entry.get(), key1, key2)
        self.plain_entry.delete(0, "end")
        self.plain_entry.insert(0, plain_text)


root = tk.Tk()

affine = AffineCipher(root)

root.mainloop()
