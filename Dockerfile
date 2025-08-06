FROM python:3.9

LABEL authors="v.kib"

# Установка рабочей директории
WORKDIR /app

# Копирование файла зависимостей и установка
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копирование всего проекта
COPY . .

# Команда по умолчанию для запуска тестов
CMD ["pytest", "tests/"]