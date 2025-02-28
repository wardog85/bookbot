from stats import get_num_words

from stats import get_num_characters

def main():
    words = get_num_words("/home/chris/projects/github.com/wardog85/bookbot/books/frankenstein.txt")
    characters = get_num_characters("/home/chris/projects/github.com/wardog85/bookbot/books/frankenstein.txt")
    print(words, characters)

main()