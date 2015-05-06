from ..lib.transformer import Transformer
import utils

class Voip(Transformer):

    def can_handle_character(self, character):
        return utils.is_character_rare1(character)

    def can_handle_contact(self, contact, clock):
        return contact.has('voipname')

    def num_required_contacts(self):
        return 2

    def transform(self, character, contacts, clock):
        contact_from, contact_to, odd = utils.rare1_character_transform(character, contacts, 'voipname')

        return 'Character: {0}, At: {1}, Skype From: {2}, To: {3}, Odd number of voip mins: {4}'.format(character, clock.block_range_str(), contact_from.get('name'), contact_to.get('name'), odd)

