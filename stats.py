def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
    return num_words


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

def sort_on(dict):
    return dict['value']

def character_list(filepath):
    character_dict = {}
    with open(filepath) as f:
        file_contents = f.read()
        lowercase_contents = file_contents.lower()
        for i in lowercase_contents:
            if i in character_dict:
                character_dict[i] += 1
            else:
                character_dict[i] = 1
    char_list = []
    for key in character_dict:
        if key.isalpha():
            char_list.append({ 'char': key, 'value': character_dict[key] })
    char_list.sort(reverse=True, key=sort_on)
    return char_list

