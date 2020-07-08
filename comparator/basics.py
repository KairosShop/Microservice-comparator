"""Basic functions for the Comparator Algorithm."""


# Pandas imports
import pandas as pd


def set_df(supermarkets, products, prices):
    """Set the Data Frame with values."""
    df = pd.DataFrame(prices, index=supermarkets, columns=products)
    df = df.fillna(0)

    total = []
    for i in range(len(supermarkets)):
        total.append(df.loc[supermarkets[i]].sum())
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