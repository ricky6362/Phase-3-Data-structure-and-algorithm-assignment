import re
from collections import defaultdict

def word_frequency(sentence):
    word_counts = defaultdict(int)
    sentence = sentence.lower()
    words = re.findall(r'\b\w+\b', sentence)

    for word in words:
        word_counts[word] += 1

    return word_counts

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
