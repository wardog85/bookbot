def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
    return f"{num_words} words found in the document"


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def get_num_characters(filepath):
    character_dict = {}
    with open(filepath) as f:
        file_contents = f.read()
        lowercase_contents = file_contents.lower()
        for i in lowercase_contents:
            if i in character_dict:
                character_dict[i] += 1
            else:
                character_dict[i] = 1
    return character_dict