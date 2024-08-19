def apt_search1(city, max_rent, min_beds, pets_allowed):
    # Top
    apartment_listings = [
        {'city': 'New York', 'rent': 2500, 'beds': 2, 'pets_allowed': True},
        {'city': 'New York', 'rent': 3000, 'beds': 3, 'pets_allowed': False},
        {'city': 'Miami', 'rent': 3200, 'beds': 2, 'pets_allowed': True},
        {'city': 'Miami', 'rent': 1850, 'beds': 1, 'pets_allowed': True},
        {'city': 'Austin', 'rent': 2200, 'beds': 2, 'pets_allowed': False},
        {'city': 'Austin', 'rent': 1900, 'beds': 2, 'pets_allowed': True},
        # More listings...
    ]

    # Filter based on the user input
    filtered_listings = [
        apt for apt in apartment_listings
        if (apt['city'] == city and
            apt['rent'] <= max_rent and
            apt['beds'] >= min_beds and
            apt['pets_allowed'] == pets_allowed)
    ]

    return filtered_listings

result = apt_search1('Miami', 2000, 1, True)
print(result)

print(apt_search2('Miami', 2000))

# Call with just min_beds and no pets_allowed
print(apt_search2('Miami', 2000, min_beds=1))

# Call with pets_allowed specified but not min_beds
print(apt_search2('Miami', 2000, pets_allowed=True))

plus_one_hundred = lambda x: x + 100
square_num = lambda x: x * x
concatenate = lambda s: "- " + s
divide_by_three = lambda x: x / 3
print(plus_one_hundred(50))      # Output: 150
print(square_num(4))             # Output: 16
print(concatenate("hello"))      # Output: "- hello"
print(divide_by_three(9))        #should be 3
