from ..lib.transformer import Transformer
from ..lib.instruction import Instruction
import utils

class Email(Transformer):

    def can_handle_character(self, character):
        return utils.is_character_common(character)

    def can_handle_contact(self, contact, clock):
        return contact.has('email')

    def num_required_contacts(self):
        return 2

    def transform(self, character, contacts, clock):
        contact_from, contact_to, first_half, length = utils.common_character_transform(character, contacts, 'email')

        return Instruction('email', character, clock, contact_from, {'to': contact_to, 'even_minute': first_half, 'last_length_digit': length})

