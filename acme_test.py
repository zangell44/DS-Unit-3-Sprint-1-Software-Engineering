#!/usr/bin/env python
"""
Unit testing for Acme products and product reporting
"""

import unittest
from acme import Product, BoxingGlove
from acme_report import generate_products


class AcmeProductTests(unittest.TestCase):
    """
    Making sure Acme products are the tops!
    """
    def test_default_product_price(self):
        """
        Test default product price being 10.
        """
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """
        Test default product weight being 20.
        """
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        """
        Test default product flammability being 0.5.
        """
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_default_product_interactions(self):
        """
        Test default product stealability and explode
        """
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), 'Kinda stealable.')
        self.assertEqual(prod.explode(), '...boom!')

    def test_nondefault_product_interactions(self):
        """
        Test non-default product parameters stealability and explode.
        """
        prod = Product('Test Product', price=100, flammability=100.0)
        self.assertEqual(prod.stealability(), 'Very stealable!')
        self.assertEqual(prod.explode(), '...BABOOM!!')


class AcmeReportTests(unittest.TestCase):
    """
    Ensuring Acme reporting is top notch
    """

    def test_default_num_products(self):
        """
        Ensures we report on 30 products by default
        """
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """
        Ensures product names in reporting are valid
        """
        # valid lists of adjectives and nouns
        adjectives = set(['Awesome', 'Shiny', 'Impressive', 'Portable',
                         'Improved'])
        nouns = set(['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???'])
        # generate product names from report
        products = generate_products()
        # split into adjectives and nouns
        bad_adjectives = [prod.name.split()[0] for prod in products
                          if prod.name.split()[0] not in adjectives]
        bad_nouns = [prod.name.split()[1] for prod in products
                     if prod.name.split()[1] not in nouns]
        self.assertEqual(len(bad_adjectives), 0)
        self.assertEqual(len(bad_nouns), 0)

if __name__ == '__main__':
    unittest.main()
