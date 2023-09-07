import re 
from collections import Counter

def load(name):
    with open(name, encoding="utf-8") as file:
        result = re.sub(r'[^\w\s]','', file.read()).lower()
    file.close()
    return result

def count_words(text):
    word_count = Counter(text.split())
    top_10 = word_count.most_common(10)
    return top_10

long_string = load("file.txt")
print(long_string)
print(count_words(long_string))