from stats import get_num_words
from stats import get_num_characters
from stats import get_list_dict
from stats import sort_on
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    text = get_book_text(book_path)
    get_num_words(text)
    print("--------- Character Count -------")
    original_dict = get_num_characters(text)
    list_dict = get_list_dict(original_dict)
    list_dict.sort(reverse=True, key=sort_on)
    for item in list_dict:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")    
    print("============= END ===============")

main()