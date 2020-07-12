"""Get all the supermarkets that offers a given product."""


def get_details(df, supermarkets, products, quantity, products_images):
    """Generate the "details list" data."""
    details = {}

    for i in range(len(products)):
        place = []
        aux = {}

        for j in range(len(supermarkets)):
            if df.at[supermarkets[j], products[i]]:
                aux['id'] = products[i]
                aux['urlImage'] = products_images[products[i]]
                
                place.append({'idSupermarket': supermarkets[j], 'price': df.at[supermarkets[j], products[i]], 'count': quantity[products[i]]})
                aux['supermarkets'] = place
        
        details[products[i]] = aux
        place = []
        aux = []
    
    aux = []
    for _, value in details.items():
        aux.append(value)

    return aux