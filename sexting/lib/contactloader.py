from contact import Contact
import json

class ContactLoader:

    def load(self, contacts_file):
        with open(contacts_file) as f:
            raw_contacts = json.load(f)
            for r in raw_contacts:
                yield Contact(r['name'], r['data'])

