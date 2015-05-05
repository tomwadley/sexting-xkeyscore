from ..lib.transformer import Transformer
import utils

class ContactlessCard(Transformer):

    def can_handle_character(self, character):
        return utils.is_character_digit2(character)

    def can_handle_contact(self, contact):
        return (contact.has('contactless') and contact.get('contactless') == True)

    def num_required_contacts(self):
        return 1

    def transform(self, character, contacts, clock):
        contact = contacts[0]
        supermarket, begin_range, end_range = utils.digit2_character_transform(character)

        return 'Character: {0}, At: {1}, Contactless card purchase by: {2}, At a supermarket: {3}, Amount ending in pence range: {4}-{5}'.format(character, clock.block_range_str(), contact.get('name'), supermarket, begin_range, end_range)

