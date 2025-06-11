def get_number_of_words(book_text):
    words = book_text.split()
    return len(words)

def get_number_characters(book_text):
    characters = {}
    for character in book_text:
        char = character.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sorted_list(char_dict):
    dict_list = []

    for char, count in char_dict.items():
        dict_list.append({
            "char": char,
            "num": count
        })
    
    dict_list.sort(key=lambda x: x["char"])

    return dict_list

    