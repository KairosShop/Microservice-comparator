"""Information for the cart test."""


def get_json_cart():
    return dict({
        "error":'false',
        "status":200,
        "body":[{
            "id":1,
            "userId":4,
            "status":"Stand by",
            "createdAt":"2020-05-19 19:45:44",
            "updatedAt":"2020-06-14 11:35:23",
            "detail":[{
                "cartId":1,
                "productId":24,
                "quantity":2,
                "supermarketId":"",
                "price":"",
                "createdAt":"2020-06-24 06:09:24",
                "updatedAt":""
            },
            {
                "cartId":1,
                "productId":28,
                "quantity":2,
                "supermarketId":"",
                "price":"",
                "createdAt":"2020-05-13 20:07:46",
                "updatedAt":""
            },
            {
                "cartId":1,
                "productId":34,
                "quantity":2,
                "supermarketId":"",
                "price":"",
                "createdAt":"2020-05-17 14:30:52",
                "updatedAt":""
            }]
        }]
    })