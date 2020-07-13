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
    return dict({"body": {"headers": [
      {
        "all": "{'total_products': 10, 'total_sum': 651, 'products': [{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10, 'count': 1}, {'id': 2, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 8, 'count': 8}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12, 'count': 2}, {'id': 4, 'name': 'Oreos', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 20, 'count': 2}, {'id': 5, 'name': 'Victoria', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 16, 'count': 6}, {'id': 6, 'name': 'Pepsi', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11, 'count': 1}, {'id': 7, 'name': 'Nescafé', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 40, 'count': 4}, {'id': 8, 'name': 'Emperador', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15, 'count': 5}, {'id': 9, 'name': 'Pan Bimbo', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 34, 'count': 3}, {'id': 10, 'name': 'Zote', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 23, 'count': 3}]}",
        "cheapest": "{'total_products': 5, 'total_sum': 0, 'products': [{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10, 'count': 1}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12, 'count': 2}, {'id': 4, 'name': 'Oreos', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 20, 'count': 2}, {'id': 6, 'name': 'Pepsi', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11, 'count': 1}, {'id': 9, 'name': 'Pan Bimbo', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 34, 'count': 3}]}",
        "id": 1,
        "supermarket": "Walmart",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      },
      {
        "all": "{'total_products': 10, 'total_sum': 638, 'products': [{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12, 'count': 1}, {'id': 2, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7, 'count': 8}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13, 'count': 2}, {'id': 4, 'name': 'Oreos', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 21, 'count': 2}, {'id': 5, 'name': 'Victoria', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15, 'count': 6}, {'id': 6, 'name': 'Pepsi', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13, 'count': 1}, {'id': 7, 'name': 'Nescafé', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 38, 'count': 4}, {'id': 8, 'name': 'Emperador', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 14, 'count': 5}, {'id': 9, 'name': 'Pan Bimbo', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 35, 'count': 3}, {'id': 10, 'name': 'Zote', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 24, 'count': 3}]}",
        "cheapest": "{'total_products': 3, 'total_sum': 0, 'products': [{'id': 2, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7, 'count': 8}, {'id': 7, 'name': 'Nescafé', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 38, 'count': 4}, {'id': 8, 'name': 'Emperador', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 14, 'count': 5}]}",
        "id": 4,
        "supermarket": "Sams Club",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      },
      {
        "all": "{'total_products': 10, 'total_sum': 636, 'products': [{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11, 'count': 1}, {'id': 2, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7, 'count': 8}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13, 'count': 2}, {'id': 4, 'name': 'Oreos', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 22, 'count': 2}, {'id': 5, 'name': 'Victoria', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 14, 'count': 6}, {'id': 6, 'name': 'Pepsi', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12, 'count': 1}, {'id': 7, 'name': 'Nescafé', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 40, 'count': 4}, {'id': 8, 'name': 'Emperador', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15, 'count': 5}, {'id': 9, 'name': 'Pan Bimbo', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 34, 'count': 3}, {'id': 10, 'name': 'Zote', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 22, 'count': 3}]}",
        "cheapest": "{'total_products': 2, 'total_sum': 0, 'products': [{'id': 5, 'name': 'Victoria', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 14, 'count': 6}, {'id': 10, 'name': 'Zote', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 22, 'count': 3}]}",
        "id": 5,
        "supermarket": "Mercado Soriana",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      }
    ],
    "products": "[{'id': 1, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11}]}, {'id': 2, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 8}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7}]}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13}]}, {'id': 4, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 20}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 21}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 22}]}, {'id': 5, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 16}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 14}]}, {'id': 6, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12}]}, {'id': 7, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 40}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 38}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 40}]}, {'id': 8, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 14}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15}]}, {'id': 9, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 34}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 35}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 34}]}, {'id': 10, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 23}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 24}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 22}]}]"
  },
  "error": "false",
  "status": "200"
})


def res_half_prod():
    """All supermarkets with half products response."""
    return dict({"body": {"headers": [
      {
        "all": "{'total_products': 5, 'total_sum': 187.0, 'products': [{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10.0, 'count': 1}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12.0, 'count': 2}, {'id': 4, 'name': 'Oreos', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 20.0, 'count': 2}, {'id': 6, 'name': 'Pepsi', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11.0, 'count': 1}, {'id': 9, 'name': 'Pan Bimbo', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 34.0, 'count': 3}]}",
        "cheapest": "{'total_products': 5, 'total_sum': 0, 'products': [{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10.0, 'count': 1}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12, 'count': 2}, {'id': 4, 'name': 'Oreos', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 20.0, 'count': 2}, {'id': 6, 'name': 'Pepsi', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11, 'count': 1}, {'id': 9, 'name': 'Pan Bimbo', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 34.0, 'count': 3}]}",
        "id": 1,
        "supermarket": "Walmart",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      },
      {
        "all": "{'total_products': 5, 'total_sum': 259.0, 'products': [{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12.0, 'count': 1}, {'id': 2, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7.0, 'count': 8}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13.0, 'count': 2}, {'id': 6, 'name': 'Pepsi', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13.0, 'count': 1}, {'id': 7, 'name': 'Nescafé', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 38.0, 'count': 4}]}",
        "cheapest": "{'total_products': 2, 'total_sum': 0, 'products': [{'id': 2, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7.0, 'count': 8}, {'id': 7, 'name': 'Nescafé', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 38.0, 'count': 4}]}",
        "id": 4,
        "supermarket": "Sams Club",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      },
      {
        "all": "{'total_products': 5, 'total_sum': 235.0, 'products': [{'id': 2, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7.0, 'count': 8}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13.0, 'count': 2}, {'id': 6, 'name': 'Pepsi', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12.0, 'count': 1}, {'id': 8, 'name': 'Emperador', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15.0, 'count': 5}, {'id': 10, 'name': 'Zote', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 22.0, 'count': 3}]}",
        "cheapest": "{'total_products': 2, 'total_sum': 0, 'products': [{'id': 8, 'name': 'Emperador', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15.0, 'count': 5}, {'id': 10, 'name': 'Zote', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 22.0, 'count': 3}]}",
        "id": 5,
        "supermarket": "Mercado Soriana",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      }
    ],
    "products": "[{'id': 1, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10.0}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12.0}]}, {'id': 2, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7.0}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7.0}]}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13}]}, {'id': 4, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 20.0}]}, {}, {'id': 6, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12}]}, {'id': 7, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 38.0}]}, {'id': 8, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15.0}]}, {'id': 9, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 34.0}]}, {'id': 10, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 22.0}]}]"
  },
  "error": "false",
  "status": "200"
})


def res_one_market_all_prod():
    """One supermarket with all products response."""
    return dict({"body": {"headers": [
      {
        "all": "{'total_products': 10, 'total_sum': 651.0, 'products': [{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10.0, 'count': 1}, {'id': 2, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 8.0, 'count': 8}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12.0, 'count': 2}, {'id': 4, 'name': 'Oreos', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 20.0, 'count': 2}, {'id': 5, 'name': 'Victoria', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 16.0, 'count': 6}, {'id': 6, 'name': 'Pepsi', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11.0, 'count': 1}, {'id': 7, 'name': 'Nescafé', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 40.0, 'count': 4}, {'id': 8, 'name': 'Emperador', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15.0, 'count': 5}, {'id': 9, 'name': 'Pan Bimbo', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 34.0, 'count': 3}, {'id': 10, 'name': 'Zote', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 23.0, 'count': 3}]}",
        "cheapest": "{'total_products': 6, 'total_sum': 0, 'products': [{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10.0, 'count': 1}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12, 'count': 2}, {'id': 4, 'name': 'Oreos', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 20.0, 'count': 2}, {'id': 6, 'name': 'Pepsi', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11.0, 'count': 1}, {'id': 9, 'name': 'Pan Bimbo', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 34.0, 'count': 3}, {'id': 10, 'name': 'Zote', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 23, 'count': 3}]}",
        "id": 1,
        "supermarket": "Walmart",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      },
      {
        "all": "{'total_products': 7, 'total_sum': 571.0, 'products': [{'id': 2, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7.0, 'count': 8}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13.0, 'count': 2}, {'id': 5, 'name': 'Victoria', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15.0, 'count': 6}, {'id': 7, 'name': 'Nescafé', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 38.0, 'count': 4}, {'id': 8, 'name': 'Emperador', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 14.0, 'count': 5}, {'id': 9, 'name': 'Pan Bimbo', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 35.0, 'count': 3}, {'id': 10, 'name': 'Zote', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 24.0, 'count': 3}]}",
        "cheapest": "{'total_products': 3, 'total_sum': 0, 'products': [{'id': 2, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7.0, 'count': 8}, {'id': 5, 'name': 'Victoria', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15, 'count': 6}, {'id': 7, 'name': 'Nescafé', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 38, 'count': 4}]}",
        "id": 4,
        "supermarket": "Sams Club",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      },
      {
        "all": "{'total_products': 5, 'total_sum': 409.0, 'products': [{'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15.0, 'count': 2}, {'id': 5, 'name': 'Victoria', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15.0, 'count': 6}, {'id': 7, 'name': 'Nescafé', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 38.0, 'count': 4}, {'id': 8, 'name': 'Emperador', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13.0, 'count': 5}, {'id': 10, 'name': 'Zote', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 24.0, 'count': 3}]}",
        "cheapest": "{'total_products': 1, 'total_sum': 0, 'products': [{'id': 8, 'name': 'Emperador', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13, 'count': 5}]}",
        "id": 5,
        "supermarket": "Mercado Soriana",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      }
    ],
    "products": "[{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10.0}]}, {'id': 2, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 8.0}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7.0}]}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15}]}, {'id': 4, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 20.0}]}, {'id': 5, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 16}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15}]}, {'id': 6, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11.0}]}, {'id': 7, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 40}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 38}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 38}]}, {'id': 8, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 14}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13}]}, {'id': 9, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 34.0}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 35.0}]}, {'id': 10, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 23}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 24}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 24}]}]"
  },
  "error": "false",
  "status": "200"
})


def res_two_markets_all_prod():
    """Two supermarket with all products and same prices response."""
    return dict({"body": {"headers": [
      {
        "all": "{'total_products': 10, 'total_sum': 651.0, 'products': [{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10.0, 'count': 1}, {'id': 2, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 8.0, 'count': 8}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12.0, 'count': 2}, {'id': 4, 'name': 'Oreos', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 20.0, 'count': 2}, {'id': 5, 'name': 'Victoria', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 16.0, 'count': 6}, {'id': 6, 'name': 'Pepsi', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11.0, 'count': 1}, {'id': 7, 'name': 'Nescafé', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 40.0, 'count': 4}, {'id': 8, 'name': 'Emperador', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15.0, 'count': 5}, {'id': 9, 'name': 'Pan Bimbo', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 34.0, 'count': 3}, {'id': 10, 'name': 'Zote', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 23.0, 'count': 3}]}",
        "cheapest": "{'total_products': 6, 'total_sum': 0, 'products': [{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10.0, 'count': 1}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12, 'count': 2}, {'id': 4, 'name': 'Oreos', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 20.0, 'count': 2}, {'id': 6, 'name': 'Pepsi', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11.0, 'count': 1}, {'id': 9, 'name': 'Pan Bimbo', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 34, 'count': 3}, {'id': 10, 'name': 'Zote', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 23, 'count': 3}]}",
        "id": 1,
        "supermarket": "Walmart",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      },
      {
        "all": "{'total_products': 7, 'total_sum': 571.0, 'products': [{'id': 2, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7.0, 'count': 8}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13.0, 'count': 2}, {'id': 5, 'name': 'Victoria', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15.0, 'count': 6}, {'id': 7, 'name': 'Nescafé', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 38.0, 'count': 4}, {'id': 8, 'name': 'Emperador', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 14.0, 'count': 5}, {'id': 9, 'name': 'Pan Bimbo', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 35.0, 'count': 3}, {'id': 10, 'name': 'Zote', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 24.0, 'count': 3}]}",
        "cheapest": "{'total_products': 4, 'total_sum': 0, 'products': [{'id': 2, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7, 'count': 8}, {'id': 5, 'name': 'Victoria', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15, 'count': 6}, {'id': 7, 'name': 'Nescafé', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 38, 'count': 4}, {'id': 8, 'name': 'Emperador', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 14, 'count': 5}]}",
        "id": 4,
        "supermarket": "Sams Club",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      },
      {
        "all": "{'total_products': 10, 'total_sum': 651.0, 'products': [{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10.0, 'count': 1}, {'id': 2, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 8.0, 'count': 8}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12.0, 'count': 2}, {'id': 4, 'name': 'Oreos', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 20.0, 'count': 2}, {'id': 5, 'name': 'Victoria', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 16.0, 'count': 6}, {'id': 6, 'name': 'Pepsi', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11.0, 'count': 1}, {'id': 7, 'name': 'Nescafé', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 40.0, 'count': 4}, {'id': 8, 'name': 'Emperador', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15.0, 'count': 5}, {'id': 9, 'name': 'Pan Bimbo', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 34.0, 'count': 3}, {'id': 10, 'name': 'Zote', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 23.0, 'count': 3}]}",
        "cheapest": "{}",
        "id": 5,
        "supermarket": "Mercado Soriana",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      }
    ],
    "products": "[{'id': 1, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10.0}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10.0}]}, {'id': 2, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 8}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 8}]}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12}]}, {'id': 4, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 20.0}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 20.0}]}, {'id': 5, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 16}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 16}]}, {'id': 6, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11.0}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11.0}]}, {'id': 7, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 40}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 38}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 40}]}, {'id': 8, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 14}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15}]}, {'id': 9, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 34}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 35}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 34}]}, {'id': 10, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 23}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 24}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 23}]}]"
  },
  "error": "false",
  "status": "200"
})


def res_some_prod():
    """All supermarkets with some products response."""
    return dict({"body": {"headers": [
      {
        "all": "{'total_products': 5, 'total_sum': 371.0, 'products': [{'id': 2, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 8.0, 'count': 8}, {'id': 4, 'name': 'Oreos', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 20.0, 'count': 2}, {'id': 5, 'name': 'Victoria', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 16.0, 'count': 6}, {'id': 9, 'name': 'Pan Bimbo', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 34.0, 'count': 3}, {'id': 10, 'name': 'Zote', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 23.0, 'count': 3}]}",
        "cheapest": "{'total_products': 3, 'total_sum': 0, 'products': [{'id': 4, 'name': 'Oreos', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 20.0, 'count': 2}, {'id': 9, 'name': 'Pan Bimbo', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 34.0, 'count': 3}, {'id': 10, 'name': 'Zote', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 23.0, 'count': 3}]}",
        "id": 1,
        "supermarket": "Walmart",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      },
      {
        "all": "{'total_products': 4, 'total_sum': 246.0, 'products': [{'id': 2, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7.0, 'count': 8}, {'id': 6, 'name': 'Pepsi', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13.0, 'count': 1}, {'id': 9, 'name': 'Pan Bimbo', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 35.0, 'count': 3}, {'id': 10, 'name': 'Zote', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 24.0, 'count': 3}]}",
        "cheapest": "{'total_products': 2, 'total_sum': 0, 'products': [{'id': 2, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7, 'count': 8}, {'id': 6, 'name': 'Pepsi', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13.0, 'count': 1}]}",
        "id": 4,
        "supermarket": "Sams Club",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      },
      {
        "all": "{}",
        "cheapest": "{'total_products': 5, 'total_sum': 0, 'products': [{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11.0, 'count': 1}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13.0, 'count': 2}, {'id': 5, 'name': 'Victoria', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 14.0, 'count': 6}, {'id': 7, 'name': 'Nescafé', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 40.0, 'count': 4}, {'id': 8, 'name': 'Emperador', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15.0, 'count': 5}]}",
        "id": 5,
        "supermarket": "Mercado Soriana",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      }
    ],
    "products": "[{'id': 1, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11.0}]}, {'id': 2, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 8}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 7}]}, {'id': 3, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13.0}]}, {'id': 4, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 20.0}]}, {'id': 5, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 16.0}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 14.0}]}, {'id': 6, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 13.0}]}, {'id': 7, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 40.0}]}, {'id': 8, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 15.0}]}, {'id': 9, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 34.0}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 35.0}]}, {'id': 10, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 23.0}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 24.0}]}]"
  },
  "error": "false",
  "status": "200"
})


def res_no_prod():
    """All supermarkets with no products response."""
    return dict({"body": {"headers": [
      {
        "all": "{'total_products': 0, 'total_sum': 0.0, 'products': []}",
        "cheapest": "{}",
        "id": 1,
        "supermarket": "Walmart",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      },
      {
        "all": "{'total_products': 0, 'total_sum': 0.0, 'products': []}",
        "cheapest": "{}",
        "id": 4,
        "supermarket": "Sams Club",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      },
      {
        "all": "{'total_products': 0, 'total_sum': 0.0, 'products': []}",
        "cheapest": "{}",
        "id": 5,
        "supermarket": "Mercado Soriana",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      }
    ],
    "products": "[{}, {}, {}, {}, {}, {}, {}, {}, {}, {}]"
  },
  "error": "false",
  "status": "200"
})


def res_one_same_prod():
    """All supermarkets with one same product response."""
    return dict({"body": {"headers": [
      {
        "all": "{'total_products': 1, 'total_sum': 10.0, 'products': [{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10.0, 'count': 1}]}",
        "cheapest": "{'total_products': 1, 'total_sum': 0, 'products': [{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10, 'count': 1}]}",
        "id": 1,
        "supermarket": "Walmart",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      },
      {
        "all": "{'total_products': 1, 'total_sum': 12.0, 'products': [{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12.0, 'count': 1}]}",
        "cheapest": "{}",
        "id": 4,
        "supermarket": "Sams Club",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      },
      {
        "all": "{'total_products': 1, 'total_sum': 11.0, 'products': [{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11.0, 'count': 1}]}",
        "cheapest": "{}",
        "id": 5,
        "supermarket": "Mercado Soriana",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      }
    ],
    "products": "[{'id': 1, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10}, {'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 12}, {'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 11}]}, {}, {}, {}, {}, {}, {}, {}, {}, {}]"
  },
  "error": "false",
  "status": "200"
})


def res_one_dif_prod():
    """All supermarkets with one diferent product response."""
    return dict({"body": {"headers": [
        {
        "all": "{'total_products': 1, 'total_sum': 10.0, 'products': [{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10.0, 'count': 1}]}",
        "cheapest": "{'total_products': 1, 'total_sum': 0, 'products': [{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10.0, 'count': 1}]}",
        "id": 1,
        "supermarket": "Walmart",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      },
      {
        "all": "{'total_products': 1, 'total_sum': 42.0, 'products': [{'id': 4, 'name': 'Oreos', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 21.0, 'count': 2}]}",
        "cheapest": "{'total_products': 1, 'total_sum': 0, 'products': [{'id': 4, 'name': 'Oreos', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 21.0, 'count': 2}]}",
        "id": 4,
        "supermarket": "Sams Club",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      },
      {
        "all": "{'total_products': 1, 'total_sum': 84.0, 'products': [{'id': 5, 'name': 'Victoria', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 14.0, 'count': 6}]}",
        "cheapest": "{'total_products': 1, 'total_sum': 0, 'products': [{'id': 5, 'name': 'Victoria', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 14.0, 'count': 6}]}",
        "id": 5,
        "supermarket": "Mercado Soriana",
        "urlImage": "http://dummyimage.com/229x104.png/dddddd/000000"
      }
    ],
    "products": "[{'id': 1, 'name': 'Sabritas', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 1, 'name': 'Walmart', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 10.0}]}, {}, {}, {'id': 4, 'name': 'Yoplait', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 4, 'name': 'Sams Club', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 21.0}]}, {'id': 5, 'name': 'Coca Cola', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'supermarkets': [{'idSupermarket': 5, 'name': 'Mercado Soriana', 'urlImage': 'http://dummyimage.com/229x104.png/dddddd/000000', 'price': 14.0}]}, {}, {}, {}, {}, {}]"
  },
  "error": "false",
  "status": "200"
})
