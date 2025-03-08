import tkinter as tk
from PIL import Image, ImageTk
import random
import os
import sys

# Папка с картинками
assets_folder = "assets"

# Функция получения правильного пути к файлу
def resource_path(relative_path):
    """Возвращает правильный путь к файлам в зависимости от того, упакован ли проект."""
    try:
        # PyInstaller создаёт временную директорию, где лежат все ресурсы
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Функция уменьшения текстуры воды (если нужно)
def resize_water_texture():
    water_image_path = resource_path(os.path.join(assets_folder, "water.png"))
    resized_water_image_path = resource_path(os.path.join(assets_folder, "water_resized.png"))

    if os.path.exists(water_image_path):
        try:
            image = Image.open(water_image_path)
            new_size = (int(image.width / 1.5), int(image.height / 1.5))  # Уменьшаем в 1.5 раза
            resized_image = image.resize(new_size, Image.LANCZOS)
            resized_image.save(resized_water_image_path)
        except Exception as e:
            print(f"Ошибка при обработке water.png: {e}")

resize_water_texture()  # Вызываем уменьшение текстуры воды

# Вопросы и ответы
questions = [
    {"text": "What is the color of the sky on a clear day?", "answers": ["blue"], "image": "sky.png"},
    {"text": "How many legs does a cat have?", "answers": ["4", "four"], "image": "cat.png"},
    {"text": "What is Earth's natural satellite?", "answers": ["moon"], "image": "moon.png"},
    {"text": "How many days are in a week?", "answers": ["7", "seven"], "image": "week.png"},
    {"text": "Which country is known for the Eiffel Tower?", "answers": ["france"], "image": "france.png"},
    {"text": "How many months are in a year?", "answers": ["12", "twelve"], "image": "calendar.png"},
    {"text": "What do people drink to stay hydrated?", "answers": ["water"], "image": "water_resized.png"},
    {"text": "What day of the week is today?", "answers": ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"], "image": "day.png"},
    {"text": "Who is the main character in Harry Potter?", "answers": ["harry potter"], "image": "harry.png"},
    {"text": "What number comes after 9?", "answers": ["10", "ten"], "image": "ten.png"}
]

# Перемешиваем вопросы
random.shuffle(questions)

# Глобальные переменные
current_question = 0
score = 0

# Функция для загрузки изображений
def load_image(image_name):
    image_path = resource_path(os.path.join(assets_folder, image_name))
    if os.path.exists(image_path):
        try:
            img = Image.open(image_path)
            img.thumbnail((600, 600), Image.LANCZOS)  # Максимум 600x600
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Ошибка загрузки изображения {image_name}: {e}")
            return None
    else:
        print(f"Файл {image_name} не найден!")
        return None

# Функция проверки ответа
def check_answer():
    global current_question, score
    user_answer = entry.get().strip().lower()
    correct_answers = [ans.lower() for ans in questions[current_question]["answers"]]

    if user_answer in correct_answers:
        result_label.config(text="✅ Correct!", fg="green")
        score += 1
    else:
        result_label.config(text=f"❌ Wrong! The correct answer: {correct_answers[0]}", fg="red")

    current_question += 1
    entry.delete(0, tk.END)

    if current_question < len(questions):
        root.after(1000, show_question)
    else:
        root.after(1000, end_game)

# Функция показа вопроса
def show_question():
    question_data = questions[current_question]
    question_label.config(text=question_data["text"], fg="#4a4a4a", font=("Helvetica", 24))

    img = load_image(question_data["image"])
    if img:
        image_label.config(image=img, text="")
        image_label.image = img
    else:
        image_label.config(text="Image not found!", fg="red", font=("Helvetica", 16), image="")

    result_label.config(text="")

# Функция завершения игры
def end_game():
    question_label.config(text=f"🎉 Congratulations! You scored {score}/{len(questions)}.", fg="purple", font=("Helvetica", 24))
    entry.pack_forget()
    submit_button.pack_forget()

# Интерфейс
root = tk.Tk()
root.title("SmartQuiz")
root.geometry("900x900")

question_label = tk.Label(root, text="", font=("Helvetica", 24), fg="#4a4a4a", wraplength=800)
question_label.pack(pady=20)

image_label = tk.Label(root, text="")
image_label.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 18), width=30)
entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit", font=("Helvetica", 18), command=check_answer)
submit_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 20))
result_label.pack(pady=10)

show_question()

root.mainloop()
