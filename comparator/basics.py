"""Basic functions for the Comparator Algorithm."""


# Pandas imports
import pandas as pd

# Python modules imports
from math import sqrt


def get_location(user_loc, market_loc):
    """Get the distance between the user and a given supermarket."""
    location = sqrt(
        ((user_loc[0] - market_loc[0])**2)
        + ((user_loc[1] - market_loc[1])**2)
    )
    
    return location


def get_df(supermarkets, products, prices, quantity):
    """Get the Data Frame with values."""

    df = pd.DataFrame(prices, index=supermarkets, columns=products)
    df = df.fillna(0)

    total = []
    aux = []
    for i in range(len(supermarkets)):
        quant = dict(quantity)
        for j in range(len(quantity)):
            aux.append(df.loc[supermarkets[i]][j] * quant[next(iter(quant))])
            del quant[next(iter(quant))]
        total.append(sum(aux))
        aux = []

    df['total'] = total

    return df


def get_context(user, markets, all_in_one, cheapest, details, markets_images, markets_ids, products_ids):
    """Generate the JSON string with the data to export."""
    
    set_context = {}
    for market in markets:
        set_context[market] = all_in_one[market], cheapest[market]

    context = []
    for market in markets:
        context.append({
            'id': markets_ids[market],
            'supermarket': market,
            'urlImage': markets_images[market],
            'all': str(set_context[market][0]),
            'cheapest': str(set_context[market][1])
        })

    context = {'headers': context}
    context['products'] = str(details)
    
    return context