def find_items(max_weight, things):
    items = list(things.items())
    items.sort(key=lambda item: item[1])
    selected_items = []
    for item in items:
        if item[1] <= max_weight:
            selected_items.append(item[0])
            max_weight -= item[1]
    return selected_items, round(max_weight, 2)

things = {
    "Палатка": 3, 
    "Спальный мешок": 1.5, 
    "Горелка": 0.5, 
    "Баллон с газом": 2, 
    "Котелок": 1, 
    "Термос": 0.7,
    "Чипсы": 0.2,
    "Мясо": 1
    }

max_weight = 7
selected_items = find_items(max_weight, things)
print(f'В рюкзак поместятся следующие вещи: {selected_items[0]}, остаточный вес: {selected_items[1]}')