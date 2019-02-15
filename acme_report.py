#!/usr/bin/env python
"""
Creates inventory reports for Acme corp
"""

import random
from acme import Product


def generate_products(n=30):
    """
    Randomly generates a specified number of products
    """
    adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

    return [Product(name=random.choice(adjectives) + ' ' +
            random.choice(nouns),
            price=random.randint(5, 100),
            weight=random.randint(5, 100),
            flammability=random.uniform(0.0, 2.5)) for _ in range(n)]


def inventory_report(products):
    """
    Takes a list of Acme products and prints a summary

    Summary will incldue:

        * Number of unique product names
        * Average price
        * Average weight
        * Average flammability
    """
    def most_common(lst):
        """
        Returns most common item in a list
        """
        return max(set(lst), key=lst.count)
    count = float(len(products))
    unique = len(set([prod.name for prod in products]))
    avg_price = sum([prod.price for prod in products]) / count
    avg_weight = sum([prod.weight for prod in products]) / count
    avg_flammability = sum([prod.flammability for prod in products]) / count

    print ('Number of Unique Product Names: %d' % unique)
    print ('Most Popular Product: %s' %
           most_common([prod.name for prod in products]))
    print ('Average Price: %.2f' % avg_price)
    print ('Average Weight: %.2f' % avg_weight)
    print ('Average Flammability: %.2f' % avg_flammability)


if __name__ == '__main__':
    inventory_report(generate_products())
