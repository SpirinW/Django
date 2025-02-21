# Конвертер валют

Конвертер валют, который позволяет конвертировать сумму между различными валютами с помощью API. Веб-приложение позволяет пользователю ввести валюты и сумму, а затем выполнить конвертацию, отображая результат на странице.

## Особенности

- Конвертация валют в реальном времени.
- Поддержка популярных валют, таких как USD, EUR, RUB, и другие.
- Простой и интуитивно понятный интерфейс.

## Стек технологий

- **Django** — для серверной части.
- **Django REST Framework** — для создания API.
- **HTML, CSS, JavaScript** — для фронтенда.

## Установка и запуск

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/ваш_репозиторий/currency_converter.git
   cd currency_converter
   ```

2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Создайте файл `.env` в корне проекта и добавьте свой API-ключ для конвертации валют (например, от [exchangerate.host](https://exchangerate.host/)):

   ```
   API_KEY=ваш_api_ключ
   ```

4. Запустите сервер:

   ```bash
   python manage.py runserver
   ```

5. Откройте браузер и перейдите по адресу:

   ```
   http://127.0.0.1:8000/
   ```

## Использование

1. Введите валюты и сумму для конвертации.
2. Нажмите кнопку **Конвертировать**.
3. Результат конвертации отобразится ниже.

## Скриншоты

Вот как выглядит интерфейс вашего конвертера валют:

![Скриншот 1](https://github.com/SpirinW/Django/blob/main/currency_converter/screenshots/1.png)
![Скриншот 2](https://github.com/SpirinW/Django/blob/main/currency_converter/screenshots/2.png)

## Структура проекта

```
currency_converter/
│
├── exchange/                  # Приложение для обработки конвертации валют
│   ├── migrations/            
│   ├── static/
│   ├── templates/
│   ├── urls.py                # Роуты для приложения
│   ├── views.py               # Логика конвертации
│   ├── serializers.py         # Сериализаторы для API
│   └── ...
│
├── currency_converter/        # Основной проект Django
│   ├── settings.py            # Конфигурация проекта
│   ├── urls.py                # Основные роуты проекта
│   ├── wsgi.py
│   ├── asgi.py
│   └── ...
│
├── manage.py                  # Скрипт для управления проектом
├── requirements.txt           # Список зависимостей
└── .env                       # Конфигурация API ключа
```

