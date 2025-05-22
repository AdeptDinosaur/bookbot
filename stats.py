def get_num_words(text):
    words = text.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")

def get_num_characters(text):
    characters = text.lower()
    char_dict = {}
    for character in characters:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    return char_dict