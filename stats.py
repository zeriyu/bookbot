def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    character_count = {}  # Initialize the dictionary
    for char in text:
        if char in character_count:  # Check if char is in character_count directly
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def format_character_count(character_count):
    sorted_characters = []
    for char, count in character_count.items():
        if char.isalpha():
            sorted_characters.append({"char": char, "num": count})
    sorted_characters.sort(key=lambda x: x["num"], reverse=True)
    return sorted_characters