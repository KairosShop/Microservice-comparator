"""Product Comparation Algorithm."""


# Comparator functions imports
from .basics import get_df, get_context, get_location
from .all_in_one import get_all_in_one
from .cheapest import get_cheapest
from .details import get_details


def the_comparator(user_info, supermarkets, markets_loc, products, quantity, prices, markets_images, products_images, markets_ids, products_ids):
    """The Comparator main function."""
    user = user_info[0]
    user_loc = user_info[1]

    best_loc = []
    for loc in markets_loc:
        best_loc.append([loc, get_location(user_loc, markets_loc[loc])])

    best_loc = sorted(best_loc, key = lambda x: x[1])[0:3]

    best_markets = []
    for loc in best_loc:
        best_markets.append(loc[0])
    
    best_prices = []
    for market in best_markets:
        best_prices.append(prices[market])

    df = get_df(best_markets, products, best_prices, quantity)

    all_in_one = get_all_in_one(df, best_markets, user_loc, markets_loc, products, quantity, products_images, products_ids)
    cheapest = get_cheapest(df, best_markets, products, quantity, products_images, products_ids)
    details = get_details(df, best_markets, products, quantity, products_images, products_ids, markets_ids, markets_images)

    context = get_context(user, best_markets, all_in_one, cheapest, details, markets_images, markets_ids, products_ids)

    return context
