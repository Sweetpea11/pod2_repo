print("Challenge: Favourite Restaurants")

print()

print("Question 1")

'''
Below is a dictionary consisting of details of 1 restaurant fetched from Yelp. 

Go through the dictionary and print out the following 3 pieces of information about the restaurant: 
1. The latitude and longitude of Four Barrel Coffee 
2. The complete address of Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code. 
3. The website of Four Barrel Coffee
'''


restaurant = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "address2": "",
    "address3": "",
    "state": "CA",
    "address1": "375 Valencia St",
    "zip_code": "94103",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}

print(restaurant)

# TODO: Write code to print the latitude and .longitude of Four Barrel Coffee
print(f'latitude of Four Barrel Coffee {restaurant["latitude"]}longitude of Four Barrel Coffee {restaurant["longitude"]}')
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
print(f'address of the Four barrel\n{restaurant["address1"]}\n{restaurant["city"]}\n{restaurant["state"]}\n{restaurant["zip_code"]}')
# TODO: Write code to print the URL of the website of Four Barrel Coffee.
print("https://www.yelp.com/biz/four-barrel-coffee-san-francisco")


print()

print("Question 2")

# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
restaurant_myfav1 = {
    "name": "cheesecakefactory",
    "address": "520 concord ave, Bronx, NY",
    "favorite_dish": "strawberry_cheesecake"
}
print(restaurant_myfav1)
restaurant_myfav2 = {
    'name': 'chima',
    'address': '8010 Towers Cres Plaza, Tysons, VA',
    'favorite_dish': 'lamb cooked rare'
}
print(restaurant_myfav2)
restaurant_myfav3 = {
    'name': 'China_House',
    'address' : '337-U Hospital Drive, Glen_Burnie, MD',
    'favorite_dish' : '6 wings fried hard & french fries'
}
print(restaurant_myfav3)
#         1. name : name of the resturant (string)
#         2. address: address of the restaurant (string)
#         3. favourite_dish: your favourite thing to order at the restaurant (string)

# TODO: Print each dictionary

# The dictionary for each restaurant should look something like this

'''
restaurant_1  = {
    "name": "Subway",
    "address" : "116th & Broadway, NY 10016",
    "favourite_dish" : "Chicken BLT Sandwich" }
'''

print()

print("Question 3")
'''
Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there. 
Remove the 'favourite_dish' key value pair from that restaurant's dictionary
'''

# TODO: Remove the 'favourite_dish' key-value pair from one of your 3 restaurants)
restaurant_myfav1.pop('favorite_dish')
restaurant_myfav2.pop('favorite_dish')
restaurant_myfav3.pop('favorite_dish')
# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant
print(restaurant_myfav1)
print(restaurant_myfav2)
print(restaurant_myfav3)
print()

print("Question 4")
'''
Imagine that another one of your most favourite restaurants modified its address. 
Update just this value in that restaurant's dictionary
'''

# TODO: Update the address field of 1 restaurant
restaurant_myfav1["address"] = '180th & bard, NY,NY'
# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary
print(restaurant_myfav1["address"])
# TODO: Print the updated dictionary.
print(restaurant_myfav1)

print()
