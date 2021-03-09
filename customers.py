"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self, first, last, email, password):

        self.first = first
        self.last = last
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about 
        customer in console."""

        return f'customer first name: {self.first}, customer last name: {self.last}, customer email: {self.email}, customer password: {self.password} '

def read_customer_file(filepath):

    customer_dict = {}

    with open(filepath) as file:

        for line in file:
            (first,
            last,
            email,
            password) = line.strip().split("|")

            customer_dict[email] = Customer(first, last, email, password)
    
    return customer_dict

def get_by_email(email):
    return customer_info[email]

customer_info = read_customer_file("customers.txt")
