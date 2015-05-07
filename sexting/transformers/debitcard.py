from ..lib.transformer import Transformer
from ..lib.instruction import Instruction
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

        return Instruction('debitcard', character, clock, contact, {'is_supermarket': supermarket, 'begin_pence_range': begin_range, 'end_pence_range': end_range})

