from ..lib.transformer import Transformer
import utils

class Tweet(Transformer):

    def can_handle_character(self, character):
        return character == ' '

    def can_handle_contact(self, contact, clock):
        return contact.has('twitter')

    def num_required_contacts(self):
        return 1

    def transform(self, character, contacts, clock):
        contact = contacts[0]

        return 'Character: {0}, At: {1}, Tweet by: {2}'.format(character, clock.block_range_str(), contact.get('name'))

