from contact import Contact

class ContactLoader:

    def load(self):
        return [
            Contact({'name': 'testname', 'email': 'some@email.com'}),
            Contact({'name': 'foobar', 'email': 'foo@bar.com'}),
        ]
