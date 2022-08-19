"""Restaurant rating lister."""


# put your code here 
def restaurant_ratings(filename):
    """
    sort restaurant ratings from a file in alphabetical order
    """
    # with for opening files https://www.pythonforbeginners.com/files/with-statement-in-python
    ratings = {}

    open_file = open(filename)

    for line in open_file:
        line = line.rstrip()
        restaurant_scores = line.split(':')
        restaurant, rating = restaurant_scores
        for restaurant_score in restaurant_scores:
            ratings[restaurant] = rating   
    
    ratings = dict(sorted(ratings.items()))

    #print(ratings)
    return ratings

dictionary = restaurant_ratings('scores.txt')

def take_restaurant_and_score_input(dictionary_name):

    user_restaurant_prompt = input("Enter restaurant name: ")

    user_score_prompt = input("Enter your score for the restaurant: ")

    dictionary_name[user_restaurant_prompt] = user_score_prompt

    dictionary_name = dict(sorted(dictionary_name.items()))

    print(dictionary_name)

#restaurant_ratings('scores.txt')
take_restaurant_and_score_input(dictionary)