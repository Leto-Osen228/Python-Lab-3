import tkinter as tk
from PIL import Image, ImageTk
import string

def shift_text(text, shift):
    chars = string.ascii_uppercase + string.digits
    shifted = ''.join(chars[(chars.index(c) + shift) % len(chars)] for c in text)
    return shifted

def generate_key():
    input_block = entry.get().upper()
    if len(input_block) != 5 or not all(c in string.ascii_uppercase + string.digits for c in input_block):
        result_label.config(text="Введите корректный блок (5 символов A-Z, 0-9).")
        return
    
    block2 = shift_text(input_block, 3)
    block3 = shift_text(input_block, -5)
    key = f"{input_block}-{block2}-{block3}"
    result_label.config(text=key)

# Создание интерфейса
root = tk.Tk()
root.title("Key Generator")
root.geometry("500x300")


def change_background(i=0):
    background_image = Image.open(f"frames/frame_{i%8}.png")
    background_image = background_image.resize((500, 300))
    background_photo = ImageTk.PhotoImage(background_image)

    background_label.config(image=background_photo)
    background_label.image = background_photo

    root.after(150, change_background, i+1)


background_label = tk.Label(root)
background_label.place(relwidth=1, relheight=1)  # Заполняем весь экран
change_background()  # Запуск смены фона

tk.Label(root, text="Введите первый блок ключа (XXXXX):", bg='white').pack(pady=10)
entry = tk.Entry(root, font=('Helvetica', 18), justify='center', width=10)
entry.pack()

tk.Button(root, text="Сгенерировать ключ", width=15, command=generate_key).pack(pady=20)
result_label = tk.Label(root, text="", font=('Helvetica', 10), bg='white')
result_label.pack(pady=10)

root.mainloop()
