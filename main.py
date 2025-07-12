import sys
from stats import count_words, count_characters, format_character_count

def get_book_text(path):
    with open(path, encoding='utf-8') as f:  # Specify encoding
        file_contents = f.read()
    return file_contents

def main(book_path):
    book = get_book_text(book_path) 
    word_count = count_words(book)
    character_count = count_characters(book)
    formatted_character_count = format_character_count(character_count)

    print(f'============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print(f'----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print(f'--------- Character Count -------')
    for char in formatted_character_count:
        print(f'{char["char"]}: {char["num"]}')
    print(f'============= END ===============')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(book_path=sys.argv[1])

