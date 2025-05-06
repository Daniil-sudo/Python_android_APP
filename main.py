
import random

from tkinter import Tk, Label, PhotoImage, Button, ttk, X, Text, BOTH

root = Tk()     # создаем корневой объект - окно
root.title("Генератор паролей") # устанавливаем заголовок окна
root.iconbitmap(default="py.ico.png") # здесь добавил иконку, но применилась не корректно, в след апдейтах переделаю
root.attributes("-toolwindow", True)
root.resizable(False, False)

root.geometry("600x500")

clicks = []
letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbol = ["!","@","#","$","%"]
#run = True

def genering_password (letter,numbers,symbol, length=20):
    """пароли геенерируются из списков """
    password = ''.join(random.choice(letter+numbers+symbol) for _ in range(length))
    return password
password = genering_password(letter,numbers,symbol, length=20)
#while run:
#print(password)
"""пишется лейбл, в дальнейшем планируется что бы активировался от кнопки"""
# label = Label(text=password)
# label.pack()
"""//////////////////////////////////////////////////////////"""

"""создал кнопку"""




pas = []


def prassed():
    """в цикле описаны атрибуты кнопки и что она длеает.Она запускает цикл
    для генерации паролей genering_password """
    btn = ttk.Button(text="Click me",  command = genering_password)
    btn.place(anchor = "nw",width=120, height=55)

    return btn
pas.append(genering_password)
button = prassed() # обязательно вне цикла создать кнопку


"""место вывода пароля"""
# editor = Text()
# editor.pack(fill=BOTH, expand=1)
# editor.insert("1.0", pas)






if __name__ == "__main__":
    root.mainloop()