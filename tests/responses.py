"""All the test responses to compare."""


def res_redirect():
    """Root redirection response"""
    return dict({
        'body': {
            'message': 'Welcome to the Comparator Microservice',
            'method': 'Try again with the POST method',
            'value': '/comparator/?cart=<cart_id>'
        }
    })


def res_full_prod():
    """All supermarkets with all products response."""
    return dict({
        "body": {
            "all_in_one": "{'Walmart': [10, 189], 'Aurrera': [10, 189], 'Mercado Soriana': [10, 190], 'Sams Club': [10, 192], 'Soriana': [10, 203]}",
            "cheapest": "[{'Walmart': {'total_products': 1, 'total_sum': 20, 'products': [['Oreos', 20]]}}, {'Aurrera': {'total_products': 4, 'total_sum': 73, 'products': [['Sabritas', 9], ['Pepsi', 10], ['Pan Bimbo', 32], ['Zote', 22]]}}, {'Soriana': {'total_products': 2, 'total_sum': 25, 'products': [['Coca Cola', 11], ['Emperador', 14]]}}, {'Sams Club': {'total_products': 2, 'total_sum': 45, 'products': [['Yoplait', 7], ['Nescafé', 38]]}}, {'Mercado Soriana': {'total_products': 1, 'total_sum': 14, 'products': [['Victoria', 14]]}}]",
            "details": "{'Sabritas': [['Walmart', 10], ['Aurrera', 9], ['Soriana', 11], ['Sams Club', 12], ['Mercado Soriana', 11]], 'Yoplait': [['Walmart', 8], ['Aurrera', 9], ['Soriana', 10], ['Sams Club', 7], ['Mercado Soriana', 7]], 'Coca Cola': [['Walmart', 12], ['Aurrera', 12], ['Soriana', 11], ['Sams Club', 13], ['Mercado Soriana', 13]], 'Oreos': [['Walmart', 20], ['Aurrera', 22], ['Soriana', 21], ['Sams Club', 21], ['Mercado Soriana', 22]], 'Victoria': [['Walmart', 16], ['Aurrera', 15], ['Soriana', 17], ['Sams Club', 15], ['Mercado Soriana', 14]], 'Pepsi': [['Walmart', 11], ['Aurrera', 10], ['Soriana', 15], ['Sams Club', 13], ['Mercado Soriana', 12]], 'Nescafé': [['Walmart', 40], ['Aurrera', 42], ['Soriana', 45], ['Sams Club', 38], ['Mercado Soriana', 40]], 'Emperador': [['Walmart', 15], ['Aurrera', 16], ['Soriana', 14], ['Sams Club', 14], ['Mercado Soriana', 15]], 'Pan Bimbo': [['Walmart', 34], ['Aurrera', 32], ['Soriana', 33], ['Sams Club', 35], ['Mercado Soriana', 34]], 'Zote': [['Walmart', 23], ['Aurrera', 22], ['Soriana', 26], ['Sams Club', 24], ['Mercado Soriana', 22]]}",
            "user": "Usuario"
        }
    })


def res_half_prod():
    """All supermarkets with half products response."""
    return dict({
        "body": {
            "all_in_one": "{'Mercado Soriana': [5, 69.0], 'Aurrera': [5, 72.0], 'Sams Club': [5, 83.0], 'Walmart': [5, 87.0], 'Soriana': [5, 101.0]}",
            "cheapest": "[{'Walmart': {'total_products': 3, 'total_sum': 42.0, 'products': [['Sabritas', 10.0], ['Coca Cola', 12.0], ['Oreos', 20.0]]}}, {'Aurrera': {'total_products': 3, 'total_sum': 47.0, 'products': [['Victoria', 15.0], ['Pepsi', 10.0], ['Zote', 22.0]]}}, {'Soriana': {'total_products': 2, 'total_sum': 47.0, 'products': [['Emperador', 14.0], ['Pan Bimbo', 33.0]]}}, {'Sams Club': {'total_products': 2, 'total_sum': 45.0, 'products': [['Yoplait', 7.0], ['Nescafé', 38.0]]}}]",
            "details": "{'Sabritas': [['Walmart', 10.0], ['Soriana', 11.0], ['Sams Club', 12.0]], 'Yoplait': [['Aurrera', 9.0], ['Sams Club', 7.0], ['Mercado Soriana', 7.0]], 'Coca Cola': [['Walmart', 12.0], ['Sams Club', 13.0], ['Mercado Soriana', 13.0]], 'Oreos': [['Walmart', 20.0]], 'Victoria': [['Aurrera', 15.0], ['Soriana', 17.0]], 'Pepsi': [['Walmart', 11.0], ['Aurrera', 10.0], ['Sams Club', 13.0], ['Mercado Soriana', 12.0]], 'Nescafé': [['Sams Club', 38.0]], 'Emperador': [['Aurrera', 16.0], ['Soriana', 14.0], ['Mercado Soriana', 15.0]], 'Pan Bimbo': [['Walmart', 34.0], ['Soriana', 33.0]], 'Zote': [['Aurrera', 22.0], ['Soriana', 26.0], ['Mercado Soriana', 22.0]]}",
            "user": "Usuario"
        }
    })


def res_one_market_all_prod():
    """One supermarket with all products response."""
    return dict({
        "body": {
            "all_in_one": "{'Walmart': [10, 189.0], 'Sams Club': [7, 146.0], 'Aurrera': [6, 129.0], 'Soriana': [6, 127.0], 'Mercado Soriana': [5, 105.0]}",
            "cheapest": "[{'Walmart': {'total_products': 3, 'total_sum': 43.0, 'products': [['Coca Cola', 12.0], ['Oreos', 20.0], ['Pepsi', 11.0]]}}, {'Aurrera': {'total_products': 4, 'total_sum': 78.0, 'products': [['Sabritas', 9.0], ['Victoria', 15.0], ['Pan Bimbo', 32.0], ['Zote', 22]]}}, {'Sams Club': {'total_products': 2, 'total_sum': 45.0, 'products': [['Yoplait', 7.0], ['Nescafé', 38]]}}, {'Mercado Soriana': {'total_products': 1, 'total_sum': 13.0, 'products': [['Emperador', 13.0]]}}]",
            "details": "{'Sabritas': [['Walmart', 10.0], ['Aurrera', 9.0], ['Soriana', 11.0]], 'Yoplait': [['Walmart', 8.0], ['Aurrera', 9.0], ['Soriana', 10.0], ['Sams Club', 7.0]], 'Coca Cola': [['Walmart', 12.0], ['Sams Club', 13.0], ['Mercado Soriana', 15.0]], 'Oreos': [['Walmart', 20.0], ['Soriana', 21.0]], 'Victoria': [['Walmart', 16.0], ['Aurrera', 15.0], ['Sams Club', 15.0], ['Mercado Soriana', 15.0]], 'Pepsi': [['Walmart', 11.0]], 'Nescafé': [['Walmart', 40], ['Aurrera', 42], ['Soriana', 45], ['Sams Club', 38], ['Mercado Soriana', 38]], 'Emperador': [['Walmart', 15.0], ['Soriana', 14.0], ['Sams Club', 14.0], ['Mercado Soriana', 13.0]], 'Pan Bimbo': [['Walmart', 34.0], ['Aurrera', 32.0], ['Sams Club', 35.0]], 'Zote': [['Walmart', 23], ['Aurrera', 22], ['Soriana', 26], ['Sams Club', 24], ['Mercado Soriana', 24]]}",
            "user": "Usuario"
        }
    })


def res_two_markets_all_prod():
    """Two supermarket with all products and same prices response."""
    return dict({
        "body": {
            "all_in_one": "{'Walmart': [10, 189.0], 'Mercado Soriana': [10, 189.0], 'Sams Club': [7, 146.0], 'Aurrera': [6, 129.0], 'Soriana': [6, 127.0]}",
            "cheapest": "[{'Walmart': {'total_products': 3, 'total_sum': 43.0, 'products': [['Coca Cola', 12.0], ['Oreos', 20.0], ['Pepsi', 11.0]]}}, {'Aurrera': {'total_products': 4, 'total_sum': 78.0, 'products': [['Sabritas', 9.0], ['Victoria', 15.0], ['Pan Bimbo', 32.0], ['Zote', 22]]}}, {'Soriana': {'total_products': 1, 'total_sum': 14.0, 'products': [['Emperador', 14.0]]}}, {'Sams Club': {'total_products': 2, 'total_sum': 45, 'products': [['Yoplait', 7], ['Nescafé', 38]]}}]",
            "details": "{'Sabritas': [['Walmart', 10.0], ['Aurrera', 9.0], ['Soriana', 11.0], ['Mercado Soriana', 10.0]], 'Yoplait': [['Walmart', 8], ['Aurrera', 9], ['Soriana', 10], ['Sams Club', 7], ['Mercado Soriana', 8]], 'Coca Cola': [['Walmart', 12.0], ['Sams Club', 13.0], ['Mercado Soriana', 12.0]], 'Oreos': [['Walmart', 20.0], ['Soriana', 21.0], ['Mercado Soriana', 20.0]], 'Victoria': [['Walmart', 16.0], ['Aurrera', 15.0], ['Sams Club', 15.0], ['Mercado Soriana', 16.0]], 'Pepsi': [['Walmart', 11.0], ['Mercado Soriana', 11.0]], 'Nescafé': [['Walmart', 40], ['Aurrera', 42], ['Soriana', 45], ['Sams Club', 38], ['Mercado Soriana', 40]], 'Emperador': [['Walmart', 15.0], ['Soriana', 14.0], ['Sams Club', 14.0], ['Mercado Soriana', 15.0]], 'Pan Bimbo': [['Walmart', 34.0], ['Aurrera', 32.0], ['Sams Club', 35.0], ['Mercado Soriana', 34.0]], 'Zote': [['Walmart', 23], ['Aurrera', 22], ['Soriana', 26], ['Sams Club', 24], ['Mercado Soriana', 23]]}",
            "user": "Usuario"
        }
    })


def res_some_prod():
    """All supermarkets with some products response."""
    return dict({
        "body": {
            "all_in_one": "{'Aurrera': [6, 77.0], 'Soriana': [6, 121.0], 'Mercado Soriana': [6, 100.0], 'Walmart': [5, 101.0], 'Sams Club': [4, 79.0]}",
            "cheapest": "[{'Walmart': {'total_products': 2, 'total_sum': 54.0, 'products': [['Oreos', 20.0], ['Pan Bimbo', 34.0]]}}, {'Aurrera': {'total_products': 4, 'total_sum': 53.0, 'products': [['Sabritas', 9.0], ['Coca Cola', 12.0], ['Pepsi', 10.0], ['Zote', 22.0]]}}, {'Soriana': {'total_products': 1, 'total_sum': 14.0, 'products': [['Emperador', 14.0]]}}, {'Sams Club': {'total_products': 1, 'total_sum': 7, 'products': [['Yoplait', 7]]}}, {'Mercado Soriana': {'total_products': 2, 'total_sum': 54.0, 'products': [['Victoria', 14.0], ['Nescafé', 40.0]]}}]",
            "details": "{'Sabritas': [['Aurrera', 9.0], ['Soriana', 11.0], ['Mercado Soriana', 11.0]], 'Yoplait': [['Walmart', 8], ['Aurrera', 9], ['Soriana', 10], ['Sams Club', 7], ['Mercado Soriana', 7]], 'Coca Cola': [['Aurrera', 12.0], ['Mercado Soriana', 13.0]], 'Oreos': [['Walmart', 20.0]], 'Victoria': [['Walmart', 16.0], ['Aurrera', 15.0], ['Mercado Soriana', 14.0]], 'Pepsi': [['Aurrera', 10.0], ['Soriana', 15.0], ['Sams Club', 13.0]], 'Nescafé': [['Soriana', 45.0], ['Mercado Soriana', 40.0]], 'Emperador': [['Soriana', 14.0], ['Mercado Soriana', 15.0]], 'Pan Bimbo': [['Walmart', 34.0], ['Sams Club', 35.0]], 'Zote': [['Walmart', 23.0], ['Aurrera', 22.0], ['Soriana', 26.0], ['Sams Club', 24.0]]}",
            "user": "Usuario"
        }
    })


def res_no_prod():
    """All supermarkets with no products response."""
    return dict({
        "body": {
            "all_in_one": "{'Walmart': [0, 0.0], 'Aurrera': [0, 0.0], 'Soriana': [0, 0.0], 'Sams Club': [0, 0.0], 'Mercado Soriana': [0, 0.0]}",
            "cheapest": "[]",
            "details": "{'Sabritas': [], 'Yoplait': [], 'Coca Cola': [], 'Oreos': [], 'Victoria': [], 'Pepsi': [], 'Nescafé': [], 'Emperador': [], 'Pan Bimbo': [], 'Zote': []}",
            "user": "Usuario"
        }
    })


def res_one_same_prod():
    """All supermarkets with one same product response."""
    return dict({
        "body": {
            "all_in_one": "{'Aurrera': [1, 9.0], 'Walmart': [1, 10.0], 'Soriana': [1, 11.0], 'Mercado Soriana': [1, 11.0], 'Sams Club': [1, 12.0]}",
            "cheapest": "[{'Aurrera': {'total_products': 1, 'total_sum': 9, 'products': [['Sabritas', 9]]}}]",
            "details": "{'Sabritas': [['Walmart', 10], ['Aurrera', 9], ['Soriana', 11], ['Sams Club', 12], ['Mercado Soriana', 11]], 'Yoplait': [], 'Coca Cola': [], 'Oreos': [], 'Victoria': [], 'Pepsi': [], 'Nescafé': [], 'Emperador': [], 'Pan Bimbo': [], 'Zote': []}",
            "user": "Usuario"
        }
    })


def res_one_dif_prod():
    """All supermarkets with one diferent product response."""
    return dict({
        "body": {
            "all_in_one": "{'Aurrera': [1, 9.0], 'Walmart': [1, 10.0], 'Soriana': [1, 11.0], 'Mercado Soriana': [1, 14.0], 'Sams Club': [1, 21.0]}",
            "cheapest": "[{'Walmart': {'total_products': 1, 'total_sum': 10.0, 'products': [['Sabritas', 10.0]]}}, {'Aurrera': {'total_products': 1, 'total_sum': 9.0, 'products': [['Yoplait', 9.0]]}}, {'Soriana': {'total_products': 1, 'total_sum': 11.0, 'products': [['Coca Cola', 11.0]]}}, {'Sams Club': {'total_products': 1, 'total_sum': 21.0, 'products': [['Oreos', 21.0]]}}, {'Mercado Soriana': {'total_products': 1, 'total_sum': 14.0, 'products': [['Victoria', 14.0]]}}]",
            "details": "{'Sabritas': [['Walmart', 10.0]], 'Yoplait': [['Aurrera', 9.0]], 'Coca Cola': [['Soriana', 11.0]], 'Oreos': [['Sams Club', 21.0]], 'Victoria': [['Mercado Soriana', 14.0]], 'Pepsi': [], 'Nescafé': [], 'Emperador': [], 'Pan Bimbo': [], 'Zote': []}",
            "user": "Usuario"
        }
    })
