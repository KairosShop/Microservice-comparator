"""Get the cheapest option for all products."""


def get_total(all_products, products, quantity):
    """Generate the sum of the cheapest products."""
    total = 0

    for i in range(len(all_products)):
        for key, value in all_products[i].items():
            if key in products:
                total += (value * quantity[key])
    
    return total


def get_cheapest(df, supermarkets, products, quantity, products_images, products_ids):
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

    cheapest = {}
    for market in supermarkets:
        all_products = []
        
        for prod in cheap_list:
            
            for key, value in prod.items():
                if key == market:
                    if key not in all_products:
                        all_products.append({
                            'id': products_ids[value[0]],
                            'name': value[0],
                            'urlImage': products_images[value[0]],
                            'price': value[1],
                            'count': quantity[value[0]]
                        })

        if all_products:
            length = len(all_products)

            total = get_total(all_products, products, quantity)

            cheapest[market] = {
                    'total_products': length,
                    'total_sum': total,
                    'products': all_products
            }

    return cheapest
