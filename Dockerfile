# Используем официальный образ Python
FROM python:3.9-slim

# Установка рабочей директории
WORKDIR /app

# Установка системных зависимостей (для Selenium и Chrome)
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Копирование файла зависимостей и установка Python-пакетов
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование всего проекта
COPY . .

# Команда по умолчанию для запуска тестов
CMD ["pytest", "tests/"]