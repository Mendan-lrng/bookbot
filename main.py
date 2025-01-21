def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    characters = get_char_count(text)
    sorted_chars = get_sorted_chars(characters)
    print_report(book_path, num_words, sorted_chars)

def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    low_text = text.lower()
    char_count = {}
    for char in low_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_on(dict):
    return dict["number"]


def get_sorted_chars(characters):
    char_list = []
    for char in characters:
        if char.isalpha():
            char_list.append({"letter": char, "number": characters[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def print_report(book_path, num_words, sorted_chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for entry in sorted_chars:
        print(f"The '{entry["letter"]}' character was found {entry["number"]} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()