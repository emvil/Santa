# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 19:14:55 2018

@author: emvil
"""
import numpy as np
import utils 

def simpleGreedy(data,start_index=0):
    """The solver looks for the pathway with the shortest length. It computes 
    one pathway with the Greedy algorithm, by minimising the distance from the 
    current city to the next one. """
    remaining_cities= data
    # coordinates of the starting point
    x_last = remaining_cities[start_index,1]
    y_last = remaining_cities[start_index,2]
    # record start point in the pathway
    pathway = [remaining_cities[start_index,:]]
    # remove starting point from remaining to visit
    remaining_cities = utils.RemoveCityFromArray(remaining_cities, start_index)
    distance = 0
    while len(remaining_cities)>0:
        # compute distances between current location and remaining cities to be visited
        distances =  (remaining_cities[:,1]-x_last)**2 + (remaining_cities[:,2]-y_last)**2
        closest_index = np.argmin(distances)
        # record city ID in list
        pathway = np.concatenate((pathway,[remaining_cities[closest_index,:]]), axis=0)
        # pathway = pathway +remaining_cities[closest_index,:]
        # update total distance
        distance = distance +np.sqrt(distances[closest_index])
        # update the coordinates of the last visited city
        x_last = remaining_cities[closest_index,1]
        y_last = remaining_cities[closest_index,2]
        # remove closest city from remaining to visit
        remaining_cities = utils.RemoveCityFromArray(remaining_cities, closest_index)
        #remaining_cities=np.delete(remaining_cities,[closest_index] , axis= 0)
    return pathway, distance


def greedyPrimeConstraint(data,start_index=0):
    """ The solver looks for the pathway with the shortest length. It computes 
    one pathway with the Greedy algorithm, by minimising the distance from the 
    current city to the next one. 
    One additional constraint is to go through a prime city exactly every 10 
    steps, or the next step is 10% longer. """
    remaining_cities= data
    # coordinates of the starting point
    x_last = remaining_cities[start_index,1]
    y_last = remaining_cities[start_index,2]
    # record start point in the pathway
    pathway = [remaining_cities[start_index,:]]
    # remove starting point from remaining to visit
    remaining_cities = utils.RemoveCityFromArray(remaining_cities, start_index)
    distance = 0
    # record number of cities visited since the last prime city
    sinceLastPrime = 0
    while len(remaining_cities)>0:
        # compute distances between current location and remaining cities to be visited
        distances =  (remaining_cities[:,1]-x_last)**2 + (remaining_cities[:,2]-y_last)**2
        # constraint on distances 
        if sinceLastPrime%10 ==0:
            distances = distances + (distances * np.logical_not(remaining_cities[:,3]) * 0.1)     
            
        closest_index = np.argmin(distances)
        # record city ID in list
        pathway = np.concatenate((pathway,[remaining_cities[closest_index,:]]), axis=0)
        # pathway = pathway +remaining_cities[closest_index,:]
        # update total distance
        distance = distance +np.sqrt(distances[closest_index])
        # update the coordinates of the last visited city
        x_last = remaining_cities[closest_index,1]
        y_last = remaining_cities[closest_index,2]
        # update prime counting
        if remaining_cities[closest_index,3]:
            sinceLastPrime = 0
        # remove closest city from remaining to visit
        remaining_cities = utils.RemoveCityFromArray(remaining_cities, closest_index)
        #remaining_cities=np.delete(remaining_cities,[closest_index] , axis= 0)
    return pathway, distance

