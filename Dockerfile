# Используем официальный образ Python с указанной версией
FROM python:3.11

# Копируем requirements.txt в контейнер
COPY requirements.txt /app/requirements.txt

# Устанавливаем зависимости для проекта
RUN pip install -r /app/requirements.txt

# Копируем файл с моделью в контейнер
COPY models/model_knn.joblib /app/model_knn.joblib

# Копируем все файлы проекта в рабочую директорию контейнера
COPY . /app

# Задаем рабочую директорию
WORKDIR /app

# Запускаем API-приложение через Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
