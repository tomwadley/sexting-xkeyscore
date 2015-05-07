from ..lib.transformer import Transformer
from ..lib.instruction import Instruction
import utils

class FBStatus(Transformer):

    def can_handle_character(self, character):
        return character == ' '

    def can_handle_contact(self, contact, clock):
        return contact.has('fbname')

    def num_required_contacts(self):
        return 1

    def transform(self, character, contacts, clock):
        contact = contacts[0]

        return Instruction('fbstatus', character, clock, contact)

