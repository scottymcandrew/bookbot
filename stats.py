def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_characters(text):
    char_count = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in char_count:
            char_count[char_lower] += 1
        else:
            char_count[char_lower] = 1
    return char_count

def chars_dict_to_sorted_list(char_count_dict):
    # Convert dictionary to list of dictionaries, filtering alphabetical characters only
    char_list = []
    for char, count in char_count_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    # Sort by count in descending order (greatest to least)
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list

