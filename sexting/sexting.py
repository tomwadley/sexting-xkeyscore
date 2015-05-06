import sys
from random import shuffle
from transformers import all_transformers
from lib.transformer import Transformer
from lib.contactloader import ContactLoader
from lib.clock import Clock

class Sexting():

    def __init__(self, message, start_hour):
        self.message = message
        self.transformers = all_transformers()
        self.contacts = ContactLoader().load()
        self.clock = Clock(int(start_hour))

    def process(self):
        for character in self.message:
            transformersWithContacts = list(self.__possible_transformers_and_contacts(character))

            if transformersWithContacts:

                transformer, contacts = self.__choose_transformer_and_contacts(transformersWithContacts)

                instruction = transformer.transform(character, contacts, self.clock)
                yield instruction

            else:
                yield "NO TRANSFORMER FOR '{0}'".format(character)

            self.clock = self.clock.next_block()

    def __possible_transformers_and_contacts(self, character):
        for t in self.transformers:
            if not t.can_handle_character(character):
                continue

            viableContacts = filter(lambda c: not c.is_busy(self.clock) and t.can_handle_contact(c, self.clock), self.contacts)

            if len(viableContacts) < t.num_required_contacts():
                continue

            yield (t, viableContacts)

    def __choose_transformer_and_contacts(self, transformersWithContacts):
        shuffle(transformersWithContacts)

        transformer, possibleContacts = transformersWithContacts[0]

        shuffle(possibleContacts)

        contacts = possibleContacts[:transformer.num_required_contacts()]

        return (transformer, contacts)


def main():
    if len(sys.argv) <= 2:
        print 'Usage: {0} MESSAGE START_HOUR'.format(sys.argv[0])
        sys.exit(1)

    message = sys.argv[1]
    start_hour = sys.argv[2]

    for i in Sexting(message, start_hour).process():
        print i

if __name__ == '__main__':
    main()

