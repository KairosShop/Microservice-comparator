"""Get the best option for buying all product in one place."""


# Python modules imports
from math import sqrt
from operator import getitem


def get_products_length(df, market):
    """Get the number of products that a supermarket offers."""
    length = 0

    for i in range(0, len(df.loc[market].values)-1):
        if df.loc[market].values[i] != 0.0:
            length += 1

    return length


def get_location(user_loc, market_loc):
    """Get the distance between the user and a given supermarket."""
    location = sqrt(
        ((user_loc[0] - market_loc[0])**2)
        + ((user_loc[1] - market_loc[1])**2)
    )
    
    return location


def get_sorted_values(all_in_one, supermarkets, user_loc, markets_loc):
    """Get the sorted values of every supermarket."""
    
    length = []
    for i in range(len(supermarkets)):
        length.append(all_in_one[supermarkets[i]]['total_products'])

    # If all supermarkets have the same number of products
    if len(set(length)) == 1:
        aux = dict(sorted(
            all_in_one.items(),
            key=lambda x: getitem(x[1],'total_sum')
        ))

    # If not all supermarkets have the same number of products
    else:
        sort = dict(sorted(
            all_in_one.items(),
            key=lambda x: getitem(x[1], 'total_products'), reverse=True
        ))
        
        max_products = all_in_one[next(iter(all_in_one))]['total_products']
        
        aux = {}
        for key, value in all_in_one.items():
            if value['total_products'] == max_products:
                aux[key] = value

        sort_aux = dict(sorted(
            aux.items(),
            key=lambda x: getitem(x[1], 'total_sum')
        ))

        aux = {}
        for key, value in sort.items():
            if sort_aux:
                aux[list(sort_aux.keys())[0]] = sort_aux[next(iter(sort_aux))]
                del sort_aux[next(iter(sort_aux))]
            else:
                aux[key] = value

    # Check if there are more than one first-place supermarkets with the same total
    count = 0
    for _, value in aux.items():
        if value['total_products'] == aux[next(iter(aux))]['total_products']:
            count += 1
    
    # If there are more than two supermarkets with the same total
    if count >= 2:
        locations = []
        for key, value in aux.items():
            if value['total_products'] == aux[next(iter(aux))]['total_products']:
                locations.append(key)

        # Get the location and select the nearest supermarket
        best_loc = []
        for loc in locations:
            best_loc.append([loc, get_location(user_loc, markets_loc[loc])])

        sort_aux = {}
        for key, value in aux.items():
            if best_loc:
                sort_aux[best_loc[0][0]] = aux[best_loc[0][0]]
                del best_loc[0]
            else:
                sort_aux[key] = aux[key]

        return sort_aux

    else:
        return aux


def get_all_in_one(df, supermarkets, user_loc, markets_loc):
    """Generate the "all in one list" data."""
    all_in_one = {}

    for i in range(len(supermarkets)):
        length = get_products_length(df, supermarkets[i])

        all_in_one[supermarkets[i]] = {
            'total_products': length,
            'total_sum': df.loc[supermarkets[i]].values[-1]
        }
    
    all_in_one = get_sorted_values(all_in_one, supermarkets, user_loc, markets_loc)

    return all_in_one