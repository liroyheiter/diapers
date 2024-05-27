# Используем официальный образ Python в качестве базового образа
FROM python:latest

# Устанавливаем переменные среды
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && apt-get install -y libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем все файлы проекта в контейнер
COPY . .

# Указываем команду для запуска uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
