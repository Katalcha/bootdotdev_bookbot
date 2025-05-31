from sys import exit, argv
from stats import get_num_words, get_chars_dict, sort_chars_dict, print_report

def check_argv():
    return len(argv) > 1

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if not check_argv():
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    print_report(
        argv[1],
        get_num_words(get_book_text(argv[1])),
        sort_chars_dict(get_chars_dict(get_book_text(argv[1])))
    )
    exit(0)

main()
