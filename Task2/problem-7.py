#  class, which is designed for counting occurrences of items in an iterable
from collections import Counter

filename ="Sample.txt"


word_counts = Counter()

with open(filename, 'r') as file:
    
    for line in file:
        words = line.split()
        
        word_counts.update(words)

for word, count in word_counts.items():
    print(word, ":", count)
