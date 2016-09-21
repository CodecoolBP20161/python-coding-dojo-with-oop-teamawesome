class ContactList(list):

    def search(self, keyword):
        matches = []
        for contacts in self:
            if keyword in contacts.name:
                matches.append(contacts.name)
        return matches

    def longest_name(self):
        longest = None
        if len(self) == 0:
            return longest
        else:
            longest = self[0].name
            for contacts in self:
                if len(contacts.name) > len(longest):
                    longest = contacts.name
            return longest


class Contact:

    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        del cls.all_contacts[:]


class Supplier(Contact):

    all_orders = {}

    def order(self, order):
        key = self.email
        value = [order]
        if key in self.all_orders:
            self.all_orders[key].append(value)
        else:
            self.all_orders[key] = value


