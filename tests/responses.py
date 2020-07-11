"""All the test responses to compare."""


def res_redirect():
    """Root redirection response"""
    return dict({
        "body": {
            "message": "Welcome to the Comparator Microservice",
            "method": "Try again with the POST method",
            "value": "/comparator/?cart=<cart_id>"
        },
        "error": "false",
        "status": "200"
    })


def res_full_prod():
    """All supermarkets with all products response."""
    return dict()


def res_half_prod():
    """All supermarkets with half products response."""
    return dict()


def res_one_market_all_prod():
    """One supermarket with all products response."""
    return dict()


def res_two_markets_all_prod():
    """Two supermarket with all products and same prices response."""
    return dict()


def res_some_prod():
    """All supermarkets with some products response."""
    return dict()


def res_no_prod():
    """All supermarkets with no products response."""
    return dict()


def res_one_same_prod():
    """All supermarkets with one same product response."""
    return dict()


def res_one_dif_prod():
    """All supermarkets with one diferent product response."""
    return dict()
