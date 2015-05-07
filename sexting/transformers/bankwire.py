from ..lib.transformer import Transformer
from ..lib.instruction import Instruction
import utils

class BankWire(Transformer):

    def can_handle_character(self, character):
        return utils.is_character_rare2(character)

    def can_handle_contact(self, contact, clock):
        return contact.has('name')

    def num_required_contacts(self):
        return 2

    def transform(self, character, contacts, clock):
        contact_from, contact_to, odd = utils.rare2_character_transform(character, contacts, 'name')

        return Instruction('bankwire', character, clock, contact_from, {'to': contact_to, 'odd_pence': odd})
