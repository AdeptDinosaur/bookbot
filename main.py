def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def book_words(get_book_text, path_to_file):
    words = get_book_text(path_to_file).split()
    num_words = len(words)
    print(f"{num_words} words found in the document")

def main():
    book_words(get_book_text, "./books/frankenstein.txt")
    

main()