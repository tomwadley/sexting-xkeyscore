from ..lib.transformer import Transformer
from ..lib.instruction import Instruction
import utils

class Phone(Transformer):

    def can_handle_character(self, character):
        return utils.is_character_rare1(character)

    def can_handle_contact(self, contact, clock):
        return contact.has('phone')

    def num_required_contacts(self):
        return 2

    def transform(self, character, contacts, clock):
        contact_from, contact_to, odd = utils.rare1_character_transform(character, contacts, 'phone')

        return Instruction('phone', character, clock, contact_from, {'to': contact_to, 'odd_duration': odd})

