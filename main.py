from datetime import datetime

name = input("Введите ваше имя: ")


current_time = datetime.now()

formatted_time = current_time.strftime("%Y:%m:%d - %H:%M:%S")

print(f"{formatted_time} - Привет, {name}!")
