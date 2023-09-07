import random


def remove_dupe(list1):
    result = sorted(list1.copy())
    for i in result:
        counter = result.count(i)
        if counter != 1:
            result.remove(i)
    return result


def make_shuffled(list1):
    return random.shuffle(list1)


first_list = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
make_shuffled(first_list)
result_list = remove_dupe(first_list)

print(first_list)
print(result_list)
