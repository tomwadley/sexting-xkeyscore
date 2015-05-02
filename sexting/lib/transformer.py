
class Transformer(object):

    def can_handle_character(self, character):
        False

    def can_handle_contact(self, contact):
        False

    def num_required_contacts(self):
        0

    def transform(self, character, contacts, clock):
        return 'Character: {0}'.format(character)
