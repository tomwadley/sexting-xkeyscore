from contact import Contact
import json

class ContactLoader:

    def all_from_file(self, contacts_file):
        return list(self.from_file(contacts_file))

    def from_file(self, contacts_file):
        with open(contacts_file) as f:
            dicts = json.load(f)
            return self.from_dicts(dicts)

    def all_from_dicts(self, dicts):
        return list(self.from_dicts(dicts))

    def from_dicts(self, dicts):
        for r in dicts:
            yield Contact(r['name'], r['data'])

