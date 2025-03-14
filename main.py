from stats import count_words, number_of_characters, sorted_list, pretty_picture
# import stats

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    # print(get_book_text("books/frankenstein.txt"))
    count=count_words(get_book_text("books/frankenstein.txt"))
    # number_of_characters(get_book_text("books/frankenstein.txt"))
    number_of = number_of_characters(get_book_text("books/frankenstein.txt"))
    sorted = sorted_list
    # pretty = pretty_picture(sorted_list(number_of))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    pretty_picture(sorted_list(number_of))


main()