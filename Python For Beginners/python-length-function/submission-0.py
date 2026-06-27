def get_longer_word(word1: str, word2: str) -> str:
    result = word1 
    if (len(word2) > len(word1)):
        result = word2
    return result

# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
