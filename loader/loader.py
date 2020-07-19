"""Loads the database information for the products comparison."""


import tests.context as ctx


def load_context(price):
    load = [
        ctx.set_user(),
        ctx.set_markets(),
        ctx.set_markets_loc(),
        ctx.set_products(),
        ctx.set_quantity(),
        price,
        ctx.set_markets_images(),
        ctx.set_products_images(),
        ctx.set_markets_ids(),
        ctx.set_products_ids()
    ]
    return load


def load_price(id):
    prices = {
        '0001': ctx.full_prod(),
        '0002': ctx.half_prod(),
        '0003': ctx.one_market_all_prod(),
        '0004': ctx.two_markets_all_prod(),
        '0005': ctx.some_prod(),
        '0006': ctx.no_prod(),
        '0007': ctx.one_same_prod(),
        '0008': ctx.one_dif_prod()
    }
    return prices[id]


def test_loader(data):
    """Loads the data for the test cases."""
    context = load_context(data['id'][0])
    
    return context


def loader(id, lat, lon):
    """Loads the data from the database."""
    price = load_price(id)
    context = load_context(price)
    
    return context
