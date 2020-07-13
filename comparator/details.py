"""Get all the supermarkets that offers a given product."""


def get_details(df, supermarkets, products, quantity, products_images, products_ids, markets_ids, markets_images):
    """Generate the "details list" data."""
    details = {}

    for i in range(len(products)):
        place = []
        aux = {}

        for j in range(len(supermarkets)):
            if df.at[supermarkets[j], products[i]]:
                aux['id'] = products_ids[products[i]]
                aux['name'] = products[j]
                aux['urlImage'] = products_images[products[i]]
                
                place.append({
                    'idSupermarket': markets_ids[supermarkets[j]],
                    'name': supermarkets[j],
                    'urlImage': markets_images[supermarkets[j]],
                    'price': df.at[supermarkets[j], products[i]],
                })
                aux['supermarkets'] = place
        
        details[products[i]] = aux
        place = []
        aux = []
    
    aux = []
    for _, value in details.items():
        aux.append(value)

    return aux
