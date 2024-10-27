import tkinter as tk
import random


def transliterate(text):
    translit_dict = {
        "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "yo",
        "ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m",
        "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
        "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "sch",
        "ы": "y", "э": "e", "ю": "yu", "я": "ya", "ь": "", "ъ": "", " ": "."
    }

    result = ""
    for char in text.lower():
        result += translit_dict.get(char, char)

    return result


def generate_password(length=16):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_.-'
    return ''.join(random.choice(characters) for _ in range(length))


def capitalize_transliterated_name(name):
    return ' '.join(word.capitalize() for word in name.split('.'))


def on_transliterate_click():
    input_text = input_text_box.get("1.0", tk.END).strip()
    words = input_text.split()

    if len(words) == 2:
        first_name, last_name = words
    else:
        first_name, last_name = input_text, ""

    translit_full_name = transliterate(input_text)
    translit_reverse_name = transliterate(f"{last_name} {first_name}")

    email1 = f"{translit_full_name}@onetwotrip.com"
    email2 = f"ru.{translit_full_name}@12trip"
    password = generate_password()

    result_text1 = (
        f"{capitalize_transliterated_name(translit_full_name)}\n"
        f"{translit_full_name}\n"
        f"{email1}\n"
        f"{email2}\n"
        f"{password}"
    )

    email1_rev = f"{translit_reverse_name}@onetwotrip.com"
    email2_rev = f"ru.{translit_reverse_name}@12trip"

    result_text2 = (
        f"{capitalize_transliterated_name(translit_reverse_name)}\n"
        f"{translit_reverse_name}\n"
        f"{email1_rev}\n"
        f"{email2_rev}\n"
        f"{password}"
    )

    output_text_box1.config(state=tk.NORMAL)
    output_text_box1.delete("1.0", tk.END)
    output_text_box1.insert(tk.END, result_text1)
    output_text_box1.config(state=tk.DISABLED)

    output_text_box2.config(state=tk.NORMAL)
    output_text_box2.delete("1.0", tk.END)
    output_text_box2.insert(tk.END, result_text2)
    output_text_box2.config(state=tk.DISABLED)


# Create the main window
root = tk.Tk()
root.title("Transliterator and Generator")

# Input text area for transliteration
input_text_label = tk.Label(root, text="Введите текст для транслитерации:")
input_text_label.pack()
input_text_box = tk.Text(root, height=5, width=50)
input_text_box.pack()

# Button to start transliteration
transliterate_button = tk.Button(root, text="Транслитерировать", command=on_transliterate_click)
transliterate_button.pack()

# Frame to hold the result fields
results_frame = tk.Frame(root)
results_frame.pack()

# Result field 1: First Name then Last Name
output_text_label1 = tk.Label(results_frame, text="Результат 1 (Имя Фамилия):")
output_text_box1 = tk.Text(results_frame, height=8, width=35, state=tk.DISABLED)
output_text_label1.grid(row=0, column=0, padx=10, pady=5)
output_text_box1.grid(row=1, column=0, padx=10, pady=5)

# Result field 2: Last Name then First Name
output_text_label2 = tk.Label(results_frame, text="Результат 2 (Фамилия Имя):")
output_text_box2 = tk.Text(results_frame, height=8, width=35, state=tk.DISABLED)
output_text_label2.grid(row=0, column=1, padx=10, pady=5)
output_text_box2.grid(row=1, column=1, padx=10, pady=5)

# Start the main application loop
root.mainloop()