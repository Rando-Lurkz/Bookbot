def get_word_count(file_path):
    with open(file_path) as f:
        file_content = f.read()
    words_list = file_content.split()
    word_count = len(words_list)
    return word_count

def get_char_count(file_path):
    with open(file_path) as f:
        book_text = f.read().lstrip("\ufeff")
    char_count = {}
    for letter in book_text:
        l = letter.lower()
        if l not in char_count:
            char_count[l] = 0
        char_count[l] += 1
    return char_count