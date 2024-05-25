

import heapq

def minimize_connection_cost(cables):
    # Створюємо мінімальну купу з початкових довжин кабелів
    heapq.heapify(cables)
    total_cost = 0
    
    while len(cables) > 1:
        # Витягуємо два найменші кабелі з купи
        first_min = heapq.heappop(cables)
        second_min = heapq.heappop(cables)
        
        # Об'єднуємо їх і додаємо витрати
        combined_length = first_min + second_min
        total_cost += combined_length
        
        # Вставляємо об'єднаний кабель назад у купу
        heapq.heappush(cables, combined_length)
    
    return total_cost

# Приклад використання
cable_lengths = [4, 3, 2, 6]
result = minimize_connection_cost(cable_lengths)
print(f"Мінімальні загальні витрати на з'єднання кабелів: {result}")
