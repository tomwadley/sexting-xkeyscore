
__common_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "r", "s", "t", "u", "w", "y"]
__common_upper_characters = map(lambda c: c.upper(), __common_characters)
__rare1_characters = ["j", "k"]
__rare1_upper_characters = map(lambda c: c.upper(), __rare1_characters)
__rare2_characters = ["q", "v"]
__rare2_upper_characters = map(lambda c: c.upper(), __rare2_characters)
__rare3_characters = ["x", "z"]
__rare3_upper_characters = map(lambda c: c.upper(), __rare3_characters)
__digit1_characters = ["0", "2", "4", "6", "8"]
__digit2_characters = ["1", "3", "5", "7", "9"]

def is_character_common(character):
    return character in __common_characters or character in __common_upper_characters

def is_character_rare1(character):
    return character in __rare1_characters or character in __rare1_upper_characters

def is_character_rare2(character):
    return character in __rare2_characters or character in __rare2_upper_characters

def is_character_rare3(character):
    return character in __rare3_characters or character in __rare3_upper_characters

def is_character_digit1(character):
    return character in __digit1_characters

def is_character_digit2(character):
    return character in __digit2_characters

def common_character_transform(character, contacts, contact_field):
    contact_from, contact_to = __get_from_and_to(character, contacts, contact_field)
    contact_val, char_val = __encode_for_character_transform(character, __common_characters, contact_to, contact_field)

    length, first_half = __map_to_halved_range(contact_val, char_val, len(__common_characters), 10)

    return contact_from, contact_to, first_half, length

def rare1_character_transform(character, contacts, contact_field):
    return __rare_character_transform(character, __rare1_characters, contacts, contact_field)

def rare2_character_transform(character, contacts, contact_field):
    return __rare_character_transform(character, __rare2_characters, contacts, contact_field)

def rare3_character_transform(character, contacts, contact_field):
    return __rare_character_transform(character, __rare3_characters, contacts, contact_field)

def digit1_character_transform(character):
    return __digit_character_transform(character, __digit1_characters)

def digit2_character_transform(character):
    return __digit_character_transform(character, __digit2_characters)

def __rare_character_transform(character, character_set, contacts, contact_field):
    contact_from, contact_to = __get_from_and_to(character, contacts, contact_field)
    contact_val, char_val = __encode_for_character_transform(character, character_set, contact_to, contact_field)

    odd = True if contact_val != char_val else False

    return contact_from, contact_to, odd

def __map_to_halved_range(from_val, to_val, original_limit, reduced_limit):
    half_limit = original_limit / 2
    first_half = True if to_val < half_limit else False

    to_val %= half_limit
    from_val %= half_limit

    if to_val < from_val:
        result = to_val + half_limit - from_val
    else:
        result = to_val - from_val

    reduced_result = (reduced_limit / half_limit) * result

    return (reduced_result, first_half)

def __digit_character_transform(character, character_set):
    index = character_set.index(character)

    supermarket = True if index < 3 else False
    if supermarket:
        begin_range = index * 33
        end_range = begin_range + 32
        if index == 2:
            end_range += 1
    else:
        begin_range = (index - 3) * 50
        end_range = begin_range + 49

    return supermarket, begin_range, end_range

def __get_from_and_to(character, contacts, contact_field):
    is_upper_case = character.isupper()

    sorted_contacts = sorted(contacts, cmp = __cmp_contact_by(contact_field), reverse = is_upper_case)
    contact_from, contact_to = sorted_contacts

    return contact_from, contact_to

def __encode_for_character_transform(character, character_set, contact_to, contact_field):
    contact_val = __encode_str_to_int(contact_to.get(contact_field)) % len(character_set)
    char_val = character_set.index(character.lower())

    return contact_val, char_val

def __cmp_contact_by(prop):
    return lambda x, y: cmp(__encode_str_to_int(x.get(prop)), __encode_str_to_int(y.get(prop)))

def __encode_str_to_int(string):
    return reduce(lambda accum, c: accum + ord(c), string, 0)

