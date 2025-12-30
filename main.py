def get_book_text(file_path):
    with open(file_path) as f:
        files_contents = f.read()
    return files_contents

def get_word_count(string):
    words_list = string.split()
    word_count = len(words_list)
    return word_count

def main():
    word_count = get_word_count(get_book_text("books/frankenstein.txt"))
    print(f"Found {word_count} total words")

main()
