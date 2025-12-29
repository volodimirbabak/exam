import sys

# --- Ця функція потрібна для тестів ---
def calculate_sum(n):
    """Обчислює суму перших n членів прогресії 2, 4, 6..."""
    if n < 0:
        raise ValueError("Число має бути невід'ємним")
    return n * (n + 1)

# --- Ця частина працює, коли запускаєш програму вручну ---
def main():
    # ОБОВ'ЯЗКОВО ЗМІНИ ПРІЗВИЩЕ
    print("Виконав студент: Петренко Петро Петрович")
    
    try:
        user_input = input("Введіть кількість членів прогресії (n): ")
        n = int(user_input)
        
        result = calculate_sum(n)
        print(f"Сума: {result}")
        
    except ValueError:
        print("Помилка: Введіть коректне ціле число.")

if __name__ == "__main__":
    main()