import sys
from stats import get_words
from stats import count_chars
from stats import sort_chars_by_count

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    # print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    # print("----------- Word Count ----------")
    get_words(book_text)
    # print("----------- Character Count ----------")
    chars = count_chars(book_text)
    sorted_chars = sort_chars_by_count(chars)
    for char_dict in sorted_chars:
        print(f"{char_dict['char']}: {char_dict['num']}")
    # print("============= END ===============")
main()