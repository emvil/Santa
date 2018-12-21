from utils import GetCityArray
import numpy as np

cities = GetCityArray('./data/clean_s100.csv')

def make_random_tour(cities):
    """
    given cities array input (with start and end given as first point), create a random tour.
    """
    
    from utils import GetCityArray, GetStartCityFromArray, RemoveCityFromArray
    start_city = GetStartCityFromArray(cities) # get first city
    cities = RemoveCityFromArray(cities) # remove first city from array
    
    np.random.shuffle(cities) # random shuffle of remaining cities
    
    start_city = start_city.reshape(1,-1) # must reshape to be able to concatonate
    
    tour = np.concatenate((start_city,cities,start_city),axis=0) # add start and end together
    
    return(tour)

random_tour = make_random_tour(cities)
