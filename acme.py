#!/usr/bin/env python
"""
Classes representing products sold by Acme Corp
"""

import numpy as np


class Product:
    """
    Generic class for items sold by Acme Corp
    """
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        if not isinstance(name, str):
            raise AttributeError("'name' of Product must be a string")
        if not isinstance(price, int):
            raise AttributeError("'price' of Product must be an int")
        if not isinstance(weight, int):
            raise AttributeError("'weight' of Product must be an int")
        if not isinstance(flammability, float):
            raise AttributeError("'flammability' of Product must be a float")
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = np.random.randint(1000000, 10000000)

    def stealability(self):
        """"
        Returns a message indicating stealability of a Product
        """
        stealability_score = float(self.price) / float(self.weight)
        print (stealability_score)

        if stealability_score < 0.5:
            return 'Not so stealable...'
        elif stealability_score >= 0.5 and stealability_score < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):

        """
        Returns a message indicating explosion potential of Product
        """
        flammability_score = float(self.flammability) * float(self.weight)

        if flammability_score < 10.0:
            return '...fizzle.'
        elif flammability_score >= 10.0 and flammability_score < 50.0:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    """
    Boxing glove object sold by Acme corp
    """
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = np.random.randint(1000000, 10000000)

    def explode(self):
        """
        Returns a message indicating non-explosive potential of boxing gloves
        """
        return "...it's a glove."

    def punch(self):
        """
        Punches someone with boxing glove and returns their reaction based
        on glove weight
        """
        if self.weight < 5.0:
            return 'That tickles.'
        elif self.weight >= 5.0 and self.weight < 15.0:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
