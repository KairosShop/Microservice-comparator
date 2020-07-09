"""Get the best option for buying all product in one place."""


# Python modules imports
from math import sqrt


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
        length.append(all_in_one[supermarkets[i]][0])

    if len(set(length)) == 1:
        all_in_one = dict(sorted(all_in_one.items(), key=lambda x: x[1][1]))

        count = 0
        for _, value in all_in_one.items():
            if value[1] == all_in_one[next(iter(all_in_one))][1]:
                count += 1
        
        if count >= 2:
            locations = []
            for key, value in all_in_one.items():
                if value[1] == all_in_one[next(iter(all_in_one))][1]:
                    locations.append(key)

            best_loc = []
            for loc in locations:
                best_loc.append([loc, get_location(user_loc, markets_loc[loc])])

            aux = {}
            for key, value in all_in_one.items():
                if best_loc:
                    aux[best_loc[0][0]] = all_in_one[best_loc[0][0]]
                    del best_loc[0]
                else:
                    aux[key] = all_in_one[key]

            return aux

        else:
            return all_in_one

    else:
        all_in_one = dict(sorted(all_in_one.items(), key=lambda x: x[1][0], reverse=True))
    
        aux = {}
        repeated_keys = []
        for i in range(len(supermarkets)):
            if str(all_in_one[supermarkets[i]][0]) not in aux:
                aux[str(all_in_one[supermarkets[i]][0])] = 1
            else:
                aux[str(all_in_one[supermarkets[i]][0])] += 1
                repeated_keys.append(all_in_one[supermarkets[i]][0])

        count = 0
        for _, value in all_in_one.items():
            if value[0] == all_in_one[next(iter(all_in_one))][0]:
                count += 1
        
        if count >= 2:
            locations = []
            for key, value in all_in_one.items():
                if value[1] == all_in_one[next(iter(all_in_one))][1]:
                    locations.append(key)

            best_loc = []
            for loc in locations:
                best_loc.append([loc, get_location(user_loc, markets_loc[loc])])

            aux = {}
            for key, value in all_in_one.items():
                if best_loc:
                    aux[best_loc[0][0]] = all_in_one[best_loc[0][0]]
                    del best_loc[0]
                else:
                    aux[key] = all_in_one[key]

            return aux

        else:
            return all_in_one


def get_all_in_one(df, supermarkets, user_loc, markets_loc):
    """Generate the "all in one list" data."""
    all_in_one = {}

    for i in range(len(supermarkets)):
        length = get_products_length(df, supermarkets[i])

        all_in_one[supermarkets[i]] = [length, df.loc[supermarkets[i]].values[-1]]
    
    all_in_one = get_sorted_values(all_in_one, supermarkets, user_loc, markets_loc)

    return all_in_one