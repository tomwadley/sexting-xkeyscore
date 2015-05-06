from ..lib.transformer import Transformer
import utils

class DebitCard(Transformer):

    def can_handle_character(self, character):
        return utils.is_character_digit1(character)

    def can_handle_contact(self, contact, clock):
        return True

    def num_required_contacts(self):
        return 1

    def transform(self, character, contacts, clock):
        contact = contacts[0]
        supermarket, begin_range, end_range = utils.digit1_character_transform(character)

        return 'Character: {0}, At: {1}, Debit card purchase by: {2}, At a supermarket: {3}, Amount ending in pence range: {4}-{5}'.format(character, clock.block_range_str(), contact.get('name'), supermarket, begin_range, end_range)

