from app import houses


USER_CHOICE = '''
Please enter one of the following:

- 'b' to view all houses
- 'n' to view next book in catalogue
- 'c' to view 10 cheapest houses
- 'q' to quit

---->
'''


def print_houses():
    '''house_prices = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10]'''
    for house in houses:
        print(f'Vivienda de {house.bedrooms}, {house.bathrooms} y {house.surface} por un precio de {house.price}')


def print_cheapest_houses():
    cheapest_houses = sorted(houses, key=lambda x: x.price)[:10]
    for house in cheapest_houses:
        print(house)


houses_generator = (x for x in houses)


def next_house():
    print(next(houses_generator))


choices = {
    "b": print_houses,
    "n": next_house,
    "c": print_cheapest_houses
}


def menu():
    choice = input(USER_CHOICE)
    while choice != 'q':
        if choice in choices:
            choices[choice]()
        else:
            print("Please enter a valid option")
        choice = input(USER_CHOICE)


menu()