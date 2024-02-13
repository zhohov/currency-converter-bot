# currency-converter-bot

**Проект телеграм бота для конвертации валют реализован с использованием aiogram 
и api для получения курсов валют [currency-api](https://github.com/fawazahmed0/currency-api.git). 
Кроме того, в проект включен Docker для контейнеризации приложения**
## Инструкция по установке

1. **Установка Docker**
   - [Docker](https://docs.docker.com/get-docker/)
2. **Клонирование репозитория**
	```bash
	git clone https://github.com/zhohov/currency-converter-bot.git
	```
3. **Создание бота**
   - Создание бота и получение токена через @BotFather в телеграм
4. **Настройка проекта**
   - Переименовать `env` в `.env`
   - Заполнить данные в `.env`
     ```
     TELEGRAM_TOKEN = ...
     ```
5. **Запуск проекта** 
    ```bash
    make build
    ```
   или
    ```bash
    docker-compose up --build
    ```