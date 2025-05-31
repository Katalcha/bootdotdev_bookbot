def get_num_words(book_text):
    return f"Found {len(book_text.split())} total words"

def get_chars_dict(book_text):
    char_dict = {}
    for c in book_text.lower():
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def sort_chars_dict(char_dict):
    def sort_on(dict):
        return dict["num"]

    char_list = []
    for k in char_dict:
        char_list.append({"char": k, "num": char_dict[k]})
    char_list.sort(key=sort_on, reverse=True)
    return char_list

def print_report(filepath, word_count, char_list):
    print()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    for d in char_list:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")
    print()
