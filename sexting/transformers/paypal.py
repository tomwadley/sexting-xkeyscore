from ..lib.transformer import Transformer
from ..lib.instruction import Instruction
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

        return Instruction('paypal', character, clock, contact_from, {'to': contact_to, 'odd_pence': odd})

