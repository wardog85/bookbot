
import sys
from stats import get_num_words

from stats import get_num_characters

from stats import character_list

def main():
     # Check if the correct number of arguments were provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # Use the provided filepath instead of the hardcoded one
    filepath = sys.argv[1]
 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")  
    words = get_num_words(filepath)
    print("----------- Word Count ----------")
    print (f"Found {words} total words")
    print("--------- Character Count -------")
    characters = get_num_characters(filepath)
    char_count1 = character_list(filepath)
    for char in char_count1:
       print(f"{char['char']}: {char['value']}")

    print("============= END ===============")


    


main()