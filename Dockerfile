# Базовий образ Python
FROM python:3.11-slim

# Робоча директорія
WORKDIR /app

# Копіюємо файли
COPY . .

# Команда запуску
CMD ["python", "app.py"]