import sys
from stats import get_char_count, sort_char_count, get_word_count

print("Usage: python3 main.py <path_to_book>")

def main():
    num_words = get_word_count("books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    list_of_char_count = sort_char_count(get_char_count(sys.argv[1]))
    for item in list_of_char_count:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

main()