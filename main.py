from stats import get_number_of_words, get_number_characters, sorted_list
import sys
def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_number_of_words(book_text)
    num_chars = get_number_characters(book_text)
    dict_num_chars = sorted_list(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words.")
    print("--------- Character Count -------")
    
    for entry in dict_num_chars:
        char = entry["char"]
        count = entry["num"]
        if entry["char"].isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

    #print(sys.argv)

main()