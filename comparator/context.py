"""Here is where the magic begins"""


def get_context():
    context = {
                'user': 'user_id',
                'all_in_one': {
                    'supermarket1': {'total_products': 5, 'total_sum': 10},
                    'supermarket2': {'total_products': 5, 'total_sum': 12},
                    'supermarket3': {'total_products': 4, 'total_sum': 13}
                },
                'cheapest': {
                    'supermarket1': {'total_products': 2, 'total_sum': 3},
                    'supermarket2': {'total_products': 2, 'total_sum': 4},
                    'supermarket3': {'total_products': 1, 'total_sum': 1}
                },
                'details': {
                    'product1': {'supermarket1': 5, 'supermarket2': 4, 'supermarket3': 5},
                    'product2': {'supermarket1': 4, 'supermarket2': 5, 'supermarket3': 6},
                    'product3': {'supermarket1': 6, 'supermarket2': 4, 'supermarket3': 5},
                    'product4': {'supermarket1': 7, 'supermarket2': 3, 'supermarket3': 7},
                    'product5': {'supermarket1': 5, 'supermarket2': 6, 'supermarket3': 8}
                }
            }
    
    return context