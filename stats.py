def get_num_words(text):
    words = text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def get_num_characters(text):
    characters = text.lower()
    char_dict = {}
    for character in characters:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    return char_dict

def get_list_dict(original_dict):
    list_dict = []
    for key in original_dict:
        count = original_dict[key]
        list_dict.append({"char": key, "num": count})
    return list_dict

def sort_on(dict):
    return dict["num"]