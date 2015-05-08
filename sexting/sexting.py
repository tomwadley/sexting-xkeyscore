import sys
from random import shuffle
from transformers import all_transformers
from lib.transformer import Transformer
from lib.contactloader import ContactLoader
from lib.clock import Clock

class Sexting():

    def __init__(self, contacts_file, message, start_hour):
        self.message = message
        self.transformers = all_transformers()
        self.contacts = list(ContactLoader().load(contacts_file))
        self.clock = Clock(int(start_hour))

    def process(self):
        for character in self.message:
            transformersWithContacts = list(self.__possible_transformers_and_contacts(character))
            while (not transformersWithContacts):
                print "Nothing to do at {0}".format(self.clock.block_range_str())
                self.clock = self.clock.next_block()

                if (self.clock.day() > 10):
                    raise Exception("There doesn't seem to be anyone who can process {0}".format(character))

                transformersWithContacts = list(self.__possible_transformers_and_contacts(character))

            transformer, contacts = self.__choose_transformer_and_contacts(transformersWithContacts)

            instruction = transformer.transform(character, contacts, self.clock)
            yield instruction

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
    if len(sys.argv) <= 3:
        print 'Usage: {0} CONTACTS_FILE MESSAGE START_HOUR'.format(sys.argv[0])
        sys.exit(1)

    contacts_file = sys.argv[1]
    message = sys.argv[2]
    start_hour = sys.argv[3]

    for i in Sexting(contacts_file, message, start_hour).process():
        print i

if __name__ == '__main__':
    main()

