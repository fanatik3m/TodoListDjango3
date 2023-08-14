# Todo List on Django 3

Welcome to my Todo List project on Django 3!

## Which problems does my project solves

+ The Todo List project on Django solves the problem of organizing and managing tasks.
+ Users can create tasks with various parameters such as title, description, date and time of creation and status of completion.
+ Users can view a list of all tasks with the ability to filter by various parameters, edit and delete tasks, as well as mark them as completed.
+ The administrative panel allows for management of tasks and users.
+ The project helps organize work and manage tasks.
+ The project increases efficiency and productivity.

## Functionality

My project includes the following functionality:

- User registration and authentication
- Task creation with the ability to specify a title, description, date and status
- Viewing a list of all tasks with the ability to filter by date and completion status
- Editing and deleting tasks
- Marking a task as completed
- Administrative panel for managing tasks and users

## Django version:
3.1.5


## Installation and Running

To install and run the project, follow these steps:

1. Clone the repository to your computer:
   
   git clone https://github.com/fanatik3m/TodoListDjango3.git
   
2. Navigate to the project folder:
   
   cd todo_list
   
3. Create a virtual environment and activate it:
   
   python -m venv venv
   source venv/bin/activate (for Linux/MacOS)
   venv\Scripts\activate (for Windows)
   
4. Install dependencies:
   
   pip install -r requirements.txt
   
5. Create the database (credentials to create db in .env of configuration's package) and apply migrations:
   
   python manage.py migrate
   
6. Create a superuser:
   
   python manage.py createsuperuser
   
7. Run the server:
   
   python manage.py runserver
   
8. Open a browser and go to localhost:8000

## Thanks for your attention:)

# (Ru) Todo List на Django 3

Добро пожаловать в мой проект Todo List на Django 3!

## Какие проблемы решает мой проект

+ Проект Todo List на Django решает проблему организации и управления задачами.
+ Пользователи могут создавать задачи с различными параметрами, такими как название, описание, дата и время создания, статус завершения.
+ Пользователи могут просматривать список всех задач с возможностью фильтрации по различным параметрам, редактировать и удалять задачи, а также отмечать их как выполненные.
+ Административная панель позволяет управлять задачами и пользователями.
+ Проект помогает организовать работу и управлять задачами.
+ Проект повышает эффективность и производительность.

## Функциональные возможности

Мой проект включает в себя следующую функциональность:

- Регистрация и аутентификация пользователей
- Создание задачи с возможностью указания названия, описания, даты и статуса
- Просмотр списка всех задач с возможностью фильтрации по дате и статусу выполнения
- Редактирование и удаление задач
- Отметка задачи как выполненной
- Административная панель для управления задачами и пользователями

## Версия Django:
3.1.5

## Установка и запуск

Для установки и запуска проекта выполните следующие действия:

1. Клонируйте репозиторий на свой компьютер:
   
   git clone https://github.com/fanatik3m/TodoListDjango3.git
   
2. Перейдите в папку проекта:
   
   cd todo_list
   
3. Создайте виртуальную среду и активируйте ее:
   
   python -m venv venv
   source venv/bin/activate (для Linux/MacOS)
   venv\Scripts\activate (для Windows)
   
4. Установите зависимости:
   
   pip install -r requirements.txt
   
5. Создайте базу данных (поля для создания в .env пакета конфигурации) и примените миграции:
   
   python manage.py migrate
   
6. Создайте суперпользователя:
   
   python manage.py createsuperuser
   
7. Запустите сервер:
   
   python manage.py runserver
   
8. Откройте браузер и перейдите на localhost:8000

## Спасибо за внимание:)
