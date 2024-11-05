from rich import print
import subprocess
import os
import inquirer

main_path: str = "C:\\Scripts"
libraries_to_install: list = []
project_name: str = ""

def main_menu():
    questions = [
        inquirer.List('action',
                      message="На каком языке?",
                      choices=['Python', 'C++', 'Java', 'Rust', 'Go', 'C', 'C#'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['action']

def create_project(name: str, language: str, libraries: list):

    name_with_ = f'"{name}"'
    print(name_with_)

    project_path = f"{main_path}\\{language}\\{name}"
    while os.path.exists(project_path) == True:
        print(f"[red]Проект [bold]{name}[/bold] уже существует!") 
        name = input(f"Введите другое название проекта: ")
        project_path = f"{main_path}\\{language}\\{name}"

    print("Создание проекта...")
    print(f"[gray][Debug][/gray] [bold]Создание папки {project_path}...", end=" ") # Создание папки для проекта
    os.mkdir(project_path)
    print("[bold green]Успешно!")

    print(f"[gray][Debug][/gray] [bold]Создание виртуальной среды .venv...", end=" ") # Создание виртуальной среды
    os.system(f"python -m venv {main_path}/{language}/{name_with_}/.venv")
    print("[bold green]Успешно!")

    print(f"[gray][Debug][/gray] [bold]Установка библиотек ({", ".join(libraries)})...", end=" ") # Установка библиотек
    subprocess.call(f'"{main_path}\\{language}\\{name}\\.venv\\Scripts\\pip.exe" install {' '.join(libraries)}', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    print("[bold green]Успешно!")

    print(f"[gray][Debug][/gray] [bold]Создание файла [bold yellow]main.py[/bold yellow]...", end=" ") # Создание файла main.py
    with open(f"{project_path}\\main.py", "w") as file:
        for library in libraries:
            if library == "numpy":
                file.write(f"import numpy as np\n")
                continue
            if library == "bs4":
                file.write(f"from bs4 import BeautifulSoup\n")
                continue
            if library == "rich":
                file.write(f"from rich import print\n")
                continue
            file.write(f"import {library}\n")
    print("[bold green]Успешно!")

    print(f"[green]Проект [bold]{name}[/bold] успешно создан по пути [bold orange1]{project_path}[/bold orange1]!")
    os.system("pause")

if __name__ == "__main__":
    os.system("cls")
    language = main_menu()
    project_name = str(input("Введите название проекта: "))
    libraries_to_install = input("Введите названия библиотек для установки: ").split(" ")
    create_project(project_name, language, libraries_to_install)

