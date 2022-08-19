"""Restaurant rating lister."""

import sys 

def tokenize(filename):
    """Create a list of restaurant profiles--including the name and score."""

    with open(filename) as input_file:
        for line in input_file:
            restaurant_profiles = line.rstrip().split(':')
            restaurant_name, restaurant_score = restaurant_profiles
    
    return restaurant_profiles       

def restaurant_rating_dict(restaurant_profiles):
    """Sort restaurant ratings from a created list in alphabetical order."""

    restaurant_ratings = {}

        for restaurant_profile in restaurant_profiles:
            restaurant_ratings[restaurant_name] = restaurant_score  
    
    restaurant_ratings = dict(sorted(restaurant_ratings.items()))

    return restaurant_ratings

# def restaurant_ratings(filename):

#     # with for opening files https://www.pythonforbeginners.com/files/with-statement-in-python
#     ratings = {}

#     open_file = open(filename)

#     for line in open_file:
#         line = line.rstrip()
#         restaurant_profiles = line.split(':')
#         restaurant_name, restaurant_score = restaurant_profiles

#     return restaurant_profiles 

dictionary = restaurant_ratings('scores.txt')

def take_restaurant_profile_input(dictionary_name):

    user_restaurant_prompt = input("Enter restaurant name: ")

    user_score_prompt = input("Enter your score for the restaurant: ")

    dictionary_name[user_restaurant_prompt] = user_score_prompt

    dictionary_name = dict(sorted(dictionary_name.items()))

    print(dictionary_name)

# restaurant_ratings('scores.txt')
# take_restaurant_and_score_input(dictionary)

filename = sys.argv[1]
restaurant_profiles = tokenize(filename)
restaurant_ratings = restaurant_rating_dict(restaurant_profiles)