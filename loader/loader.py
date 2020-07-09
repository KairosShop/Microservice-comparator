"""Loads the database information for the products comparison."""


def json_loader(id, get_json_cart):
    """Loads the data from the json example."""
    products = []
    quantity = []

    if get_json_cart()['body'][0]['id'] == id:
        raw = get_json_cart()['body'][0]['detail']
        
        for product in raw:
            products.append(product['productId'])
            quantity.append(product['quantity'])

    else:
        products.append(0)
        quantity.append(0)

    return products, quantity


def loader(id):
    """Loads the data from the database."""
    pass