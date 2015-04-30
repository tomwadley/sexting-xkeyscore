from sexting.transformer import Transformer

class Email(Transformer):

    __characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "r", "s", "t", "u", "w", "y"]

    def can_handle_character(self, character):
        return character in Email.__characters

    def can_handle_contact(self, contact):
        return contact.has('email')

    def num_required_contacts(self):
        return 2

    def transform(self, character, contacts):
        contact_from, contact_to = contacts

        contact_val = self.__encode_str_to_int(contact_to.get('email'), len(Email.__characters))
        char_val = Email.__characters.index(character)
        length, first_half = self.__map_to_halved_range(contact_val, char_val, len(Email.__characters), 10)

        return 'Character: {0}, Email From: {1}, To: {2}, Even minute: {3}, Length: {4}'.format(character, contact_from.get('name'), contact_to.get('name'), first_half, length)

    def __encode_str_to_int(self, string, mod):
        return reduce(lambda accum, c: accum + ord(c), string, 0) % mod

    def __map_to_halved_range(self, from_val, to_val, original_limit, reduced_limit):
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
        
