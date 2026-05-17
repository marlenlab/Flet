import flet as ft # Импортируем и переимениуем (сокращаем на ft)
from datetime import datetime
import random


# Создание Страницы С помощью 
def main_page(page: ft.Page):

    # Создаем и задаем тему для страницы
    page.theme_mode = ft.ThemeMode.LIGHT

    # Даем название страницы
    page.title = 'Мое первое приложение'
    
    hello_text = ft.Text("Hello World")


    greeting_histori = []

    histori_text = ft.Text('История приветствий', size=25, weight=ft.FontWeight.BOLD)
    histori_text.visible = True

    def toggle_history(_):

        histori_text.visible = not histori_text.visible

        page.update()

    # # Добавлям текст  в страницу
    # greeting = ft.Text(value="Hello")

    def on_button_click(_):

        name = name_input.value.strip()

        current_time = datetime.now().strftime("%H:%M:%S")


        if name:
            hello_text.color = None
            hello_text.value = f'Hello {name}'
            name_input.value = ""


            greeting_histori.append(f"{name}-Время:{current_time}")
            print(greeting_histori)

            histori_text.value = 'История приветствий: \n' + '\n' .join(greeting_histori)
        else:
            hello_text.value = "Ошибка! Введите имя!!!"
            hello_text.color = ft.Colors.RED
        
        
        page.update()

    def add_name(_):

        random_name = random.choice(names_list)
        current_time = datetime.now().strftime("%H:%M:%S")
        hello_text.value = f"Hello {random_name}"
        greeting_histori.append(f"Случайное имя - {random_name} время: {current_time}" )
        histori_text.value = ('История приветствий:\n' + '\n'.join(greeting_histori))

        page.update()


    names_list = [
    "Алексей",
    "Мария",
    "Иван",
    "Ольга",
    "Максим",
    "Анна"]

    name_random = ft.ElevatedButton( "Random Name",icon=ft.Icons.ADD,on_click=add_name)

    toggle_button = ft.ElevatedButton("Скрыть / Показать историю",icon=ft.Icons.VISIBILITY,on_click=toggle_history)

    # Создаем введение имени через страницу
    name_input = ft.TextField(label="Введите имя:", on_submit = on_button_click)

    # 3D кнопка
    elevated_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click= on_button_click )



    # Обычная кнопка
    # text_button = ft.TextButton('SEND', icon=ft.Icons.SEND)

    # Кнопка иконка
    # icon_button = ft.IconButton(icon=ft.Icons.SEND)

    def on_clear_button(_):
        greeting_histori.clear()
        histori_text.value = 'История приветствий'
        page.update()

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=on_clear_button)

    buttons_row = ft.Row([elevated_button, name_random, clear_button])
    # Добавляем элементы в страницы чтоб они работали
    page.add(hello_text, name_input, buttons_row, toggle_button, histori_text)

# text_button, icon_button

# Для запуска
ft.app(main_page)

# Для запуска через браузер
# ft.app(main_page , view = ft.AppView.WEB_BROWSER)