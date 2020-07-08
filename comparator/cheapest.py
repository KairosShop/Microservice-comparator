"""Get the cheapest option for all products."""


def get_total(all_products):
    """Generate the sum of the cheapest products."""
    total = 0

    for product in all_products:
        total += product[1]
    
    return total


def get_cheapest(df, supermarkets, products):
    """Generate the "cheapest list" data."""
    cheap_list = []

    for i in range(len(products)):
        cheap = [products[i], 10000]
        market = ''
        
        for j in range(len(supermarkets)):
            if cheap[1] > df.at[supermarkets[j],products[i]]:
                if df.at[supermarkets[j],products[i]] != 0.0:
                    cheap = [products[i], df.at[supermarkets[j],products[i]]]
                    market = supermarkets[j]

        cheap_list.append({market: cheap})

    cheapest = []
    for market in supermarkets:
        all_products = []

        for prod in cheap_list:
            if list(prod.keys())[0] == market:
                if prod not in all_products:
                    all_products.append(list(prod.values())[0])

        if all_products:
            length = len(all_products)

            total = get_total(all_products)

            cheapest.append({
                market: {
                    'total_products': length,
                    'total_sum': total,
                    'products': all_products
                }
            })

    return cheapest