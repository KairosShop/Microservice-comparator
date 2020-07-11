"""Get all the supermarkets that offers a given product."""


def get_details(df, supermarkets, products):
    """Generate the "details list" data."""
    details = {}

    for i in range(len(products)):
        place = []

        for j in range(len(supermarkets)):
            if df.at[supermarkets[j], products[i]]:
                place.append({
                    supermarkets[j]:
                    df.at[supermarkets[j], products[i]]
                })

        details[products[i]] = place
    
    return details