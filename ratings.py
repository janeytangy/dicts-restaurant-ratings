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
    #sorted(ratings.keys())

    #ratings = {restaurant : ratings[restaurant] for restaurant in ratings}
            
    
    ratings = dict(sorted(ratings.items()))
    
    print(ratings)

restaurant_ratings('scores.txt')