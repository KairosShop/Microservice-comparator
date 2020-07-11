"""Basic functions for the Comparator Algorithm."""


# Pandas imports
import pandas as pd


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


def get_context(user, all_in_one, cheapest, details):
    """Generate the JSON string with the data to export.""" 
    context = {
        'user': user,
        'all_in_one': str(all_in_one),
        'cheapest': str(cheapest),
        'details': str(details)
    }

    return context