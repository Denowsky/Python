from time import time

class My_str(str):
    def __init__(self, author):
        self.author = author
        self.create_time = time()