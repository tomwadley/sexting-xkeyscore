import sys
from random import shuffle
from transformers import *
from sexting.transformer import Transformer
from sexting.contactloader import ContactLoader
from sexting.clock import Clock

class Sexting():

    def __init__(self, message, start_hour):
        self.message = message
        self.transformers = self.__load_transformers()
        self.contacts = ContactLoader().load()
        self.clock = Clock(int(start_hour))
        self.__process()

    def __load_transformers(self):
        return [
            Email(),
            SMS()
        ]

    def __process(self):
        for character in self.message:
            transformersWithContacts = list(self.__possible_transformers_and_contacts(character))

            if not transformersWithContacts:
                print "NO TRANSFORMER FOR '{0}'".format(character)
                continue

            transformer, contacts = self.__choose_transformer_and_contacts(transformersWithContacts)

            instruction = transformer.transform(character, contacts, self.clock)

            self.clock = self.clock.next_block()

            print instruction

    def __possible_transformers_and_contacts(self, character):
        for t in self.transformers:
            if not t.can_handle_character(character):
                continue

            viableContacts = filter(lambda c: t.can_handle_contact(c), self.contacts)

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

    Sexting(message, start_hour)

if __name__ == '__main__':
    main()

