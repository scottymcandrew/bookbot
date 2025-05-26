from stats import number_of_words, number_of_characters, chars_dict_to_sorted_list
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
book = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return(file_contents)

def main():
    
    # text = get_book_text("books/frankenstein.txt")
    text = get_book_text(book)
    num_words = number_of_words(text)
    num_chars = number_of_characters(text)
    sorted_chars = chars_dict_to_sorted_list(num_chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        print(f"{char}: {count}")
    
    print("============= END ===============")

main()
