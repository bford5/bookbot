def get_words(text):
    words = text.split()
    word_count = len(words)
    print(f"Found {word_count} total words")




def count_chars(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_chars_by_count(char_counts):
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list 