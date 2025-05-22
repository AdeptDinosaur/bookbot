def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
        

def book_words(text):
    words = text.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")

def main():
    text = get_book_text("books/frankenstein.txt")
    book_words(text)

main()