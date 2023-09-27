
import json
import os
from typing import Callable

def decor(func: Callable) -> Callable:
    
    def wrapper(*args, **kwargs):
        file_name = func.__name__ + ".json"

        if os.path.isfile(file_name):
            with open(file_name, 'r', encoding='UTF-8') as file:
                data = json.load(file)
        else:
            data = dict()

        result = func(*args, **kwargs)
        data[result.__repr__()]=list(args + tuple(kwargs.items()))

        with open(file_name, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return result
    return wrapper
                
@decor
def some_func(a: str, b: str):
    return a + "_" + b

