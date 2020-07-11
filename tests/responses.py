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
    return dict({
        "body": {
            "all_in_one": "{'Mercado Soriana': {'total_products': 10, 'total_sum': 636}, 'Sams Club': {'total_products': 10, 'total_sum': 638}, 'Walmart': {'total_products': 10, 'total_sum': 651}, 'Aurrera': {'total_products': 10, 'total_sum': 659}, 'Soriana': {'total_products': 10, 'total_sum': 699}}",
            "cheapest": "[{'Walmart': {'total_products': 1, 'total_sum': 40, 'products': {'Oreos': 20}}}, {'Aurrera': {'total_products': 4, 'total_sum': 181, 'products': {'Sabritas': 9, 'Pepsi': 10, 'Pan Bimbo': 32, 'Zote': 22}}}, {'Soriana': {'total_products': 2, 'total_sum': 92, 'products': {'Coca Cola': 11, 'Emperador': 14}}}, {'Sams Club': {'total_products': 2, 'total_sum': 208, 'products': {'Yoplait': 7, 'Nescafé': 38}}}, {'Mercado Soriana': {'total_products': 1, 'total_sum': 84, 'products': {'Victoria': 14}}}]",
            "details": "{'Sabritas': [{'Walmart': 10}, {'Aurrera': 9}, {'Soriana': 11}, {'Sams Club': 12}, {'Mercado Soriana': 11}], 'Yoplait': [{'Walmart': 8}, {'Aurrera': 9}, {'Soriana': 10}, {'Sams Club': 7}, {'Mercado Soriana': 7}], 'Coca Cola': [{'Walmart': 12}, {'Aurrera': 12}, {'Soriana': 11}, {'Sams Club': 13}, {'Mercado Soriana': 13}], 'Oreos': [{'Walmart': 20}, {'Aurrera': 22}, {'Soriana': 21}, {'Sams Club': 21}, {'Mercado Soriana': 22}], 'Victoria': [{'Walmart': 16}, {'Aurrera': 15}, {'Soriana': 17}, {'Sams Club': 15}, {'Mercado Soriana': 14}], 'Pepsi': [{'Walmart': 11}, {'Aurrera': 10}, {'Soriana': 15}, {'Sams Club': 13}, {'Mercado Soriana': 12}], 'Nescafé': [{'Walmart': 40}, {'Aurrera': 42}, {'Soriana': 45}, {'Sams Club': 38}, {'Mercado Soriana': 40}], 'Emperador': [{'Walmart': 15}, {'Aurrera': 16}, {'Soriana': 14}, {'Sams Club': 14}, {'Mercado Soriana': 15}], 'Pan Bimbo': [{'Walmart': 34}, {'Aurrera': 32}, {'Soriana': 33}, {'Sams Club': 35}, {'Mercado Soriana': 34}], 'Zote': [{'Walmart': 23}, {'Aurrera': 22}, {'Soriana': 26}, {'Sams Club': 24}, {'Mercado Soriana': 22}]}",
            "user": "Usuario"
            },
        "error": "false",
        "status": "200"
    })


def res_half_prod():
    """All supermarkets with half products response."""
    return dict({
        "body": {
            "all_in_one": "{'Walmart': {'total_products': 5, 'total_sum': 187.0}, 'Mercado Soriana': {'total_products': 5, 'total_sum': 235.0}, 'Sams Club': {'total_products': 5, 'total_sum': 259.0}, 'Aurrera': {'total_products': 5, 'total_sum': 318.0}, 'Soriana': {'total_products': 5, 'total_sum': 360.0}}",
            "cheapest": "[{'Walmart': {'total_products': 3, 'total_sum': 74.0, 'products': {'Sabritas': 10.0, 'Coca Cola': 12.0, 'Oreos': 20.0}}}, {'Aurrera': {'total_products': 3, 'total_sum': 166.0, 'products': {'Victoria': 15.0, 'Pepsi': 10.0, 'Zote': 22.0}}}, {'Soriana': {'total_products': 2, 'total_sum': 169.0, 'products': {'Emperador': 14.0, 'Pan Bimbo': 33.0}}}, {'Sams Club': {'total_products': 2, 'total_sum': 208.0, 'products': {'Yoplait': 7.0, 'Nescafé': 38.0}}}]",
            "details": "{'Sabritas': [{'Walmart': 10.0}, {'Soriana': 11.0}, {'Sams Club': 12.0}], 'Yoplait': [{'Aurrera': 9.0}, {'Sams Club': 7.0}, {'Mercado Soriana': 7.0}], 'Coca Cola': [{'Walmart': 12.0}, {'Sams Club': 13.0}, {'Mercado Soriana': 13.0}], 'Oreos': [{'Walmart': 20.0}], 'Victoria': [{'Aurrera': 15.0}, {'Soriana': 17.0}], 'Pepsi': [{'Walmart': 11.0}, {'Aurrera': 10.0}, {'Sams Club': 13.0}, {'Mercado Soriana': 12.0}], 'Nescafé': [{'Sams Club': 38.0}], 'Emperador': [{'Aurrera': 16.0}, {'Soriana': 14.0}, {'Mercado Soriana': 15.0}], 'Pan Bimbo': [{'Walmart': 34.0}, {'Soriana': 33.0}], 'Zote': [{'Aurrera': 22.0}, {'Soriana': 26.0}, {'Mercado Soriana': 22.0}]}",
            "user": "Usuario"
        },
        "error": "false",
        "status": "200"
    })


def res_one_market_all_prod():
    """One supermarket with all products response."""
    return dict({
        "body": {
            "all_in_one": "{'Walmart': {'total_products': 10, 'total_sum': 651.0}, 'Sams Club': {'total_products': 7, 'total_sum': 571.0}, 'Aurrera': {'total_products': 6, 'total_sum': 501.0}, 'Soriana': {'total_products': 6, 'total_sum': 461.0}, 'Mercado Soriana': {'total_products': 5, 'total_sum': 409.0}}",
            "cheapest": "[{'Walmart': {'total_products': 3, 'total_sum': 75.0, 'products': {'Coca Cola': 12.0, 'Oreos': 20.0, 'Pepsi': 11.0}}}, {'Aurrera': {'total_products': 4, 'total_sum': 261.0, 'products': {'Sabritas': 9.0, 'Victoria': 15.0, 'Pan Bimbo': 32.0, 'Zote': 22}}}, {'Sams Club': {'total_products': 2, 'total_sum': 208.0, 'products': {'Yoplait': 7.0, 'Nescafé': 38}}}, {'Mercado Soriana': {'total_products': 1, 'total_sum': 65.0, 'products': {'Emperador': 13.0}}}]",
            "details": "{'Sabritas': [{'Walmart': 10.0}, {'Aurrera': 9.0}, {'Soriana': 11.0}], 'Yoplait': [{'Walmart': 8.0}, {'Aurrera': 9.0}, {'Soriana': 10.0}, {'Sams Club': 7.0}], 'Coca Cola': [{'Walmart': 12.0}, {'Sams Club': 13.0}, {'Mercado Soriana': 15.0}], 'Oreos': [{'Walmart': 20.0}, {'Soriana': 21.0}], 'Victoria': [{'Walmart': 16.0}, {'Aurrera': 15.0}, {'Sams Club': 15.0}, {'Mercado Soriana': 15.0}], 'Pepsi': [{'Walmart': 11.0}], 'Nescafé': [{'Walmart': 40}, {'Aurrera': 42}, {'Soriana': 45}, {'Sams Club': 38}, {'Mercado Soriana': 38}], 'Emperador': [{'Walmart': 15.0}, {'Soriana': 14.0}, {'Sams Club': 14.0}, {'Mercado Soriana': 13.0}], 'Pan Bimbo': [{'Walmart': 34.0}, {'Aurrera': 32.0}, {'Sams Club': 35.0}], 'Zote': [{'Walmart': 23}, {'Aurrera': 22}, {'Soriana': 26}, {'Sams Club': 24}, {'Mercado Soriana': 24}]}",
            "user": "Usuario"
        },
        "error": "false",
        "status": "200"
    })


def res_two_markets_all_prod():
    """Two supermarket with all products and same prices response."""
    return dict({
        "body": {
            "all_in_one": "{'Walmart': {'total_products': 10, 'total_sum': 651.0}, 'Mercado Soriana': {'total_products': 10, 'total_sum': 651.0}, 'Sams Club': {'total_products': 7, 'total_sum': 571.0}, 'Aurrera': {'total_products': 6, 'total_sum': 501.0}, 'Soriana': {'total_products': 6, 'total_sum': 461.0}}",
            "cheapest": "[{'Walmart': {'total_products': 3, 'total_sum': 75.0, 'products': {'Coca Cola': 12.0, 'Oreos': 20.0, 'Pepsi': 11.0}}}, {'Aurrera': {'total_products': 4, 'total_sum': 261.0, 'products': {'Sabritas': 9.0, 'Victoria': 15.0, 'Pan Bimbo': 32.0, 'Zote': 22}}}, {'Soriana': {'total_products': 1, 'total_sum': 70.0, 'products': {'Emperador': 14.0}}}, {'Sams Club': {'total_products': 2, 'total_sum': 208, 'products': {'Yoplait': 7, 'Nescafé': 38}}}]",
            "details": "{'Sabritas': [{'Walmart': 10.0}, {'Aurrera': 9.0}, {'Soriana': 11.0}, {'Mercado Soriana': 10.0}], 'Yoplait': [{'Walmart': 8}, {'Aurrera': 9}, {'Soriana': 10}, {'Sams Club': 7}, {'Mercado Soriana': 8}], 'Coca Cola': [{'Walmart': 12.0}, {'Sams Club': 13.0}, {'Mercado Soriana': 12.0}], 'Oreos': [{'Walmart': 20.0}, {'Soriana': 21.0}, {'Mercado Soriana': 20.0}], 'Victoria': [{'Walmart': 16.0}, {'Aurrera': 15.0}, {'Sams Club': 15.0}, {'Mercado Soriana': 16.0}], 'Pepsi': [{'Walmart': 11.0}, {'Mercado Soriana': 11.0}], 'Nescafé': [{'Walmart': 40}, {'Aurrera': 42}, {'Soriana': 45}, {'Sams Club': 38}, {'Mercado Soriana': 40}], 'Emperador': [{'Walmart': 15.0}, {'Soriana': 14.0}, {'Sams Club': 14.0}, {'Mercado Soriana': 15.0}], 'Pan Bimbo': [{'Walmart': 34.0}, {'Aurrera': 32.0}, {'Sams Club': 35.0}, {'Mercado Soriana': 34.0}], 'Zote': [{'Walmart': 23}, {'Aurrera': 22}, {'Soriana': 26}, {'Sams Club': 24}, {'Mercado Soriana': 23}]}",
            "user": "Usuario"
        },
        "error": "false",
        "status": "200"
    })


def res_some_prod():
    """All supermarkets with some products response."""
    return dict({
        "body": {
            "all_in_one": "{'Walmart': {'total_products': 5, 'total_sum': 371.0}, 'Soriana': {'total_products': 6, 'total_sum': 434.0}, 'Mercado Soriana': {'total_products': 6, 'total_sum': 412.0}, 'Sams Club': {'total_products': 4, 'total_sum': 246.0}}",
            "cheapest": "[{'Walmart': {'total_products': 2, 'total_sum': 142.0, 'products': {'Oreos': 20.0, 'Pan Bimbo': 34.0}}}, {'Aurrera': {'total_products': 4, 'total_sum': 109.0, 'products': {'Sabritas': 9.0, 'Coca Cola': 12.0, 'Pepsi': 10.0, 'Zote': 22.0}}}, {'Soriana': {'total_products': 1, 'total_sum': 70.0, 'products': {'Emperador': 14.0}}}, {'Sams Club': {'total_products': 1, 'total_sum': 56, 'products': {'Yoplait': 7}}}, {'Mercado Soriana': {'total_products': 2, 'total_sum': 244.0, 'products': {'Victoria': 14.0, 'Nescafé': 40.0}}}]",
            "details": "{'Sabritas': [{'Aurrera': 9.0}, {'Soriana': 11.0}, {'Mercado Soriana': 11.0}], 'Yoplait': [{'Walmart': 8}, {'Aurrera': 9}, {'Soriana': 10}, {'Sams Club': 7}, {'Mercado Soriana': 7}], 'Coca Cola': [{'Aurrera': 12.0}, {'Mercado Soriana': 13.0}], 'Oreos': [{'Walmart': 20.0}], 'Victoria': [{'Walmart': 16.0}, {'Aurrera': 15.0}, {'Mercado Soriana': 14.0}], 'Pepsi': [{'Aurrera': 10.0}, {'Soriana': 15.0}, {'Sams Club': 13.0}], 'Nescafé': [{'Soriana': 45.0}, {'Mercado Soriana': 40.0}], 'Emperador': [{'Soriana': 14.0}, {'Mercado Soriana': 15.0}], 'Pan Bimbo': [{'Walmart': 34.0}, {'Sams Club': 35.0}], 'Zote': [{'Walmart': 23.0}, {'Aurrera': 22.0}, {'Soriana': 26.0}, {'Sams Club': 24.0}]}",
            "user": "Usuario"
        },
        "error": "false",
        "status": "200"
    })


def res_no_prod():
    """All supermarkets with no products response."""
    return dict({
        "body": {
            "all_in_one": "{'Walmart': {'total_products': 0, 'total_sum': 0.0}, 'Aurrera': {'total_products': 0, 'total_sum': 0.0}, 'Soriana': {'total_products': 0, 'total_sum': 0.0}, 'Sams Club': {'total_products': 0, 'total_sum': 0.0}, 'Mercado Soriana': {'total_products': 0, 'total_sum': 0.0}}",
            "cheapest": "[]",
            "details": "{'Sabritas': [], 'Yoplait': [], 'Coca Cola': [], 'Oreos': [], 'Victoria': [], 'Pepsi': [], 'Nescafé': [], 'Emperador': [], 'Pan Bimbo': [], 'Zote': []}",
            "user": "Usuario"
        },
        "error": "false",
        "status": "200"
    })


def res_one_same_prod():
    """All supermarkets with one same product response."""
    return dict({
        "body": {
            "all_in_one": "{'Aurrera': {'total_products': 1, 'total_sum': 9.0}, 'Walmart': {'total_products': 1, 'total_sum': 10.0}, 'Soriana': {'total_products': 1, 'total_sum': 11.0}, 'Mercado Soriana': {'total_products': 1, 'total_sum': 11.0}, 'Sams Club': {'total_products': 1, 'total_sum': 12.0}}",
            "cheapest": "[{'Aurrera': {'total_products': 1, 'total_sum': 9, 'products': {'Sabritas': 9}}}]",
            "details": "{'Sabritas': [{'Walmart': 10}, {'Aurrera': 9}, {'Soriana': 11}, {'Sams Club': 12}, {'Mercado Soriana': 11}], 'Yoplait': [], 'Coca Cola': [], 'Oreos': [], 'Victoria': [], 'Pepsi': [], 'Nescafé': [], 'Emperador': [], 'Pan Bimbo': [], 'Zote': []}",
            "user": "Usuario"
        },
        "error": "false",
        "status": "200"
    })


def res_one_dif_prod():
    """All supermarkets with one diferent product response."""
    return dict({
        "body": {
            "all_in_one": "{'Walmart': {'total_products': 1, 'total_sum': 10.0}, 'Soriana': {'total_products': 1, 'total_sum': 22.0}, 'Sams Club': {'total_products': 1, 'total_sum': 42.0}, 'Aurrera': {'total_products': 1, 'total_sum': 72.0}, 'Mercado Soriana': {'total_products': 1, 'total_sum': 84.0}}",
            "cheapest": "[{'Walmart': {'total_products': 1, 'total_sum': 10.0, 'products': {'Sabritas': 10.0}}}, {'Aurrera': {'total_products': 1, 'total_sum': 72.0, 'products': {'Yoplait': 9.0}}}, {'Soriana': {'total_products': 1, 'total_sum': 22.0, 'products': {'Coca Cola': 11.0}}}, {'Sams Club': {'total_products': 1, 'total_sum': 42.0, 'products': {'Oreos': 21.0}}}, {'Mercado Soriana': {'total_products': 1, 'total_sum': 84.0, 'products': {'Victoria': 14.0}}}]",
            "details": "{'Sabritas': [{'Walmart': 10.0}], 'Yoplait': [{'Aurrera': 9.0}], 'Coca Cola': [{'Soriana': 11.0}], 'Oreos': [{'Sams Club': 21.0}], 'Victoria': [{'Mercado Soriana': 14.0}], 'Pepsi': [], 'Nescafé': [], 'Emperador': [], 'Pan Bimbo': [], 'Zote': []}",
            "user": "Usuario"
        },
        "error": "false",
        "status": "200"
    })
