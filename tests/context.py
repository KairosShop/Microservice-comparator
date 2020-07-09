"""Data for the unittests."""


# Python modules imports
import numpy as np


def set_user():
    """User ID and location."""
    return ['Usuario', [0, 0]]


def set_quantity():
    return [1, 8, 2, 2, 6, 1, 4, 5, 3, 3]


def set_markets():
    """Supermarkets ID."""
    return [
        'Walmart',
        'Aurrera',
        'Soriana',
        'Sams Club',
        'Mercado Soriana'
    ]


def set_markets_loc():
    """Supermarkets location."""
    return dict({
        'Walmart': [1, 3],
        'Aurrera': [5, 4],
        'Soriana': [6, 2],
        'Sams Club': [1, 4],
        'Mercado Soriana': [6, 1],
    })


def set_products():
    """All products."""
    return [
        'Sabritas',
        'Yoplait',
        'Coca Cola',
        'Oreos',
        'Victoria',
        'Pepsi',
        'Nescafé',
        'Emperador',
        'Pan Bimbo',
        'Zote'
    ]


def full_prod():
    """All supermarkets with all products."""
    return [
        [10, 8, 12, 20, 16, 11, 40, 15, 34, 23],
        [9, 9, 12, 22, 15, 10, 42, 16, 32, 22],
        [11, 10, 11, 21, 17, 15, 45, 14, 33, 26],
        [12, 7, 13, 21, 15, 13, 38, 14, 35, 24],
        [11, 7, 13, 22, 14, 12, 40, 15, 34, 22],
    ]


def half_prod():
    """All supermarkets with half products."""
    return [
        [10, np.nan, 12, 20, np.nan, 11, np.nan, np.nan, 34, np.nan],
        [np.nan, 9, np.nan, np.nan, 15, 10, np.nan, 16, np.nan, 22],
        [11, np.nan, np.nan, np.nan, 17, np.nan, np.nan, 14, 33, 26],
        [12, 7, 13, np.nan, np.nan, 13, 38, np.nan, np.nan, np.nan],
        [np.nan, 7, 13, np.nan, np.nan, 12, np.nan, 15, np.nan, 22],
    ]


def one_market_all_prod():
    """One supermarket with all products."""
    return [
        [10, 8, 12, 20, 16, 11, 40, 15, 34, 23],
        [9, 9, np.nan, np.nan, 15, np.nan, 42, np.nan, 32, 22],
        [11, 10, np.nan, 21, np.nan, np.nan, 45, 14, np.nan, 26],
        [np.nan, 7, 13, np.nan, 15, np.nan, 38, 14, 35, 24],
        [np.nan, np.nan, 15, np.nan, 15, np.nan, 38, 13, np.nan, 24],
    ]


def two_markets_all_prod():
    """Two supermarket with all products and same prices."""
    return [
        [10, 8, 12, 20, 16, 11, 40, 15, 34, 23],
        [9, 9, np.nan, np.nan, 15, np.nan, 42, np.nan, 32, 22],
        [11, 10, np.nan, 21, np.nan, np.nan, 45, 14, np.nan, 26],
        [np.nan, 7, 13, np.nan, 15, np.nan, 38, 14, 35, 24],
        [10, 8, 12, 20, 16, 11, 40, 15, 34, 23],
    ]


def some_prod():
    """All supermarkets with some products."""
    return [
        [np.nan, 8, np.nan, 20, 16, np.nan, np.nan, np.nan, 34, 23],
        [9, 9, 12, np.nan, 15, 10, np.nan, np.nan, np.nan, 22],
        [11, 10, np.nan, np.nan, np.nan, 15, 45, 14, np.nan, 26],
        [np.nan, 7, np.nan, np.nan, np.nan, 13, np.nan, np.nan, 35, 24],
        [11, 7, 13, np.nan, 14, np.nan, 40, 15, np.nan, np.nan],
    ]


def no_prod():
    """All supermarkets with no products."""
    return [
        [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    ]

def one_same_prod():
    """All supermarkets with one same product."""
    return [
        [10, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [9, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [11, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [12, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [11, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    ]


def one_dif_prod():
    """All supermarkets with one diferent product."""
    return [
        [10, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [np.nan, 9, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [np.nan, np.nan, 11, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [np.nan, np.nan, np.nan, 21, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [np.nan, np.nan, np.nan, np.nan, 14, np.nan, np.nan, np.nan, np.nan, np.nan],
    ]
