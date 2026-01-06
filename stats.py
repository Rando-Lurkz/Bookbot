def get_word_count(file_path):
    with open(file_path) as f:
        file_content = f.read()
    words_list = file_content.split()
    word_count = len(words_list)
    return word_count

def get_char_count(file_path):
    with open(file_path) as f:
        book_text = f.read()
    char_count = {}
    for letter in book_text:
        l = letter.lower()
        if l not in char_count:
            char_count[l] = {"char": l, "num": 0}
        char_count[l]["num"] += 1
    return char_count

def sort_char_count(char_count):
    to_sort = []
    for item in char_count:
        to_sort.append(char_count[item])
    def sort_by(char_dict):
        return char_dict["num"]
    to_sort.sort(reverse=True, key=sort_by)
    return to_sort