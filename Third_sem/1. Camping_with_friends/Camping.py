def print_things(stuff):
    result = ", ".join(stuff)
    return result

def show_all_equip(dict):
    equipment = []
    for key in dict:
        for thing in dict.get(key):
            equipment.append(thing)
    return equipment

def show_unique_stuff(list):
    return set(list)

def find_equal_stuff(set, list, dict):
    same_things = []
    result = []
    for i in set:
        if list.count(i) == 2:
            same_things.append(i)
    for name in dict:
        for item in same_things:
            if item not in dict.get(name):
                result.append(f'{name} не взял {item}')
    return result, same_things

        


friends_with_stuff = {
        "Mike":("tent", "towel", "cool boots", "jacket"), 
        "Carl":("candies", "ball", "novel"), 
        "Stieve":("carpet", "tent", "jacket")
        }

all_stuff = show_all_equip(friends_with_stuff)
unique_stuff = show_unique_stuff(all_stuff)
who_didnt_take = find_equal_stuff(unique_stuff, all_stuff, friends_with_stuff)

print(f'Все вещи, которые взяли в поход: {print_things(all_stuff)}')
print(f'Уникальные вещи: {print_things(unique_stuff)}')
print(f'Почти все ребята взяли {print_things(who_didnt_take[1])},\nно {print_things(who_didnt_take[0])}')