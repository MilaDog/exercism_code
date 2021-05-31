import re
from collections import Counter

def count_words(sentence):
    
    # [0-9a-z] -> matches characters from a-z and 0-9
    # + -> greedily matches the expression to its left 1 or more times
    # (?:A) -> matches expression as represented by A, but cannot be retrieved afterwards
    # * -> greedily matches the expression to its left 0 or more times
    words = re.findall(r"[0-9a-z]+(?:'[0-9a-z]+)*", sentence.lower())
    return Counter(words)