from ..lib.transformer import Transformer
import utils

class Paypal(Transformer):

    def can_handle_character(self, character):
        return utils.is_character_rare3(character)

    def can_handle_contact(self, contact, clock):
        return contact.has('email')

    def num_required_contacts(self):
        return 2

    def transform(self, character, contacts, clock):
        contact_from, contact_to, odd = utils.rare3_character_transform(character, contacts, 'email')

        return 'Character: {0}, At: {1}, Paypal transfer From: {2}, To: {3}, Odd number of pence: {4}'.format(character, clock.block_range_str(), contact_from.get('name'), contact_to.get('name'), odd)

