"""Product Comparation Algorithm."""


# Comparator functions imports
from .basics import get_df, get_context
from .all_in_one import get_all_in_one
from .cheapest import get_cheapest
from .details import get_details


def the_comparator(user_info, supermarkets, markets_loc, products, quantity, prices):
    """The Comparator main function."""
    user = user_info[0]
    user_loc = user_info[1]

    df = get_df(supermarkets, products, prices, quantity)

    all_in_one = get_all_in_one(df, supermarkets, user_loc, markets_loc)
    cheapest = get_cheapest(df, supermarkets, products)
    details = get_details(df, supermarkets, products)

    context = get_context(user, all_in_one, cheapest, details)
    
    return dict(context)
