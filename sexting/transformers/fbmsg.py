from ..lib.transformer import Transformer
import utils

class FBMsg(Transformer):

    def can_handle_character(self, character):
        return utils.is_character_common(character)

    def can_handle_contact(self, contact, clock):
        return contact.has('fbname')

    def num_required_contacts(self):
        return 2

    def transform(self, character, contacts, clock):
        contact_from, contact_to, first_half, length = utils.common_character_transform(character, contacts, 'fbname')

        return 'Character: {0}, At: {1}, Facebook Msg From: {2}, To: {3}, Even minute: {4}, Length: {5}'.format(character, clock.block_range_str(), contact_from.get('name'), contact_to.get('name'), first_half, length)

