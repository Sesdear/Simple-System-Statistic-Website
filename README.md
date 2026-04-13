# Simple System Statistic Website

Простое Flask-приложение для отображения системной статистики: загрузка CPU, оперативная память, диск и температура.

## Запуск локально

1. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Запустить приложение:
   ```bash
   python app/app.py
   ```
3. Открыть в браузере:
   ```text
   http://localhost:5000
   ```

## Запуск в Docker

1. Собрать и запустить контейнер:
   ```bash
   docker-compose up --build -d
   ```
2. Открыть в браузере:
   ```text
   http://localhost:80
   ```

## Особенности

- Поддержка работы на Raspberry Pi, Orange Pi и обычных Linux-системах
- API endpoint `/stats` для выдачи данных в формате JSON
