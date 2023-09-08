# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

def return_keys_and_names(**kwargs):
    return {v if v.__hash__ is not None else str(v):k for k,v in kwargs.items()}

print(return_keys_and_names(a=1,b="string", c=[1,2]))

