import random
import tkinter as tk
from tkinter import ttk

def generate_password(length=20, use_letters=True, use_numbers=True, use_symbols=True):
    """Generates a password based on selected criteria."""
    characters = []
    if use_letters:
        characters.extend("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if use_numbers:
        characters.extend("0123456789")
    if use_symbols:
        characters.extend("!@#$%")

    if not characters:
        return "Выберите хотя бы один набор символов!"  # or raise an exception

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def update_password():
    """Updates the password display."""
    global password_label, password_length, use_letters_var, use_numbers_var, use_symbols_var

    length = password_length.get()
    use_letters = use_letters_var.get()
    use_numbers = use_numbers_var.get()
    use_symbols = use_symbols_var.get()

    new_password = generate_password(length, use_letters, use_numbers, use_symbols)
    password_label.config(text=new_password)

def copy_to_clipboard():
    """Copies the generated password to the clipboard."""
    global root, password_label
    password = password_label.cget("text")  # Get the text from the label

    if password: # Make sure there's something to copy
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update() # This is necessary on some systems to make the clipboard work
        print("Password copied to clipboard!")
    else:
        print("No password generated yet!")

# --- Tkinter Setup ---
root = tk.Tk()
root.title("Генератор паролей")
#root.iconbitmap(default="py.ico.png")  # Fix icon path if needed
root.attributes("-toolwindow", True)
root.resizable(False, False)
root.geometry("600x500")

# --- Variables ---
password_length = tk.IntVar(value=20)
use_letters_var = tk.BooleanVar(value=True)
use_numbers_var = tk.BooleanVar(value=True)
use_symbols_var = tk.BooleanVar(value=True)


# --- Widgets ---
# Password Label
password_label = tk.Label(root, text="", font=("Arial", 16), wraplength=550)  # Adjust wraplength if needed
password_label.pack(pady=20)

# Length Scale
length_label = tk.Label(root, text="Длина пароля:")
length_label.pack()
length_scale = tk.Scale(root, from_=8, to=32, orient=tk.HORIZONTAL, variable=password_length) # increased max length
length_scale.pack(pady=5)

# Checkbuttons
letters_check = tk.Checkbutton(root, text="Буквы", variable=use_letters_var)
letters_check.pack()
numbers_check = tk.Checkbutton(root, text="Цифры", variable=use_numbers_var)
numbers_check.pack()
symbols_check = tk.Checkbutton(root, text="Символы", variable=use_symbols_var)
symbols_check.pack()


# Generate Button
generate_button = ttk.Button(root, text="Сгенерировать пароль", command=update_password)
generate_button.pack(pady=10)

# Copy to Clipboard Button
copy_button = ttk.Button(root, text="Копировать в буфер обмена", command=copy_to_clipboard)
copy_button.pack(pady=10)



if __name__ == "__main__":
    update_password()  # Generate initial password
    root.mainloop()