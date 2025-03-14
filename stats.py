def count_words(text):
    words = text.split()
    wc = str(len(words))
    # print(f"{wc} words found in the document")
    return wc

def number_of_characters(text):
    words = text.split()
    unique_characters = set()
    character_count_dict = {}
    # count = 0 #Need this for a loop so that every time I count a character, it will increment.
    for word in words:
        # print(word)
        for c in word:
            unique_characters.add(c.lower())
    for c in unique_characters:
        character_count_dict[c] = 0
    for word in words:
        # print(word)
        for c in word:
            if c.lower() in unique_characters:
                character_count_dict[c.lower()] +=1
            # have something create a dict from the key of the character and a value starting at 1 then +1
    return character_count_dict


# I need to alter the dict to have a character key and a count key in a list of dicts
# [{character = w, count = 12345}, {character = x, count = 2456}]

# for d in my_dicts:
#     d.update((k, "value3") for k, v in d.items() if v == "value2")


def sort_on(dict):
    return dict["count"]

def sorted_list(character_count):
    new_dict = []
    for k,v in character_count.items():
        new_dict.append({"character":k, "count": v})
    new_dict.sort(reverse=True, key=sort_on)
    return new_dict

def pretty_picture(sorted_dict):
    sort_me = sorted_dict
    for item in sort_me:
        if item["character"].isalpha():
            print(f"{item["character"]}: {item["count"]}")



# def get_chars_dict(text):
#     chars = {}
#     for c in text:
#         lowered = c.lower()
#         if lowered in chars:
#             chars[lowered] += 1
#         else:
#             chars[lowered] = 1
#     return chars

