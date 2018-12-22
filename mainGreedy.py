# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:54:08 2018

@author: evill
"""

import pandas
import numpy as np

#%% Import data
fileName= 'C:\\Users\\evill\\Documents\\Santa\\data\\clean_small.csv'

data =np.array(pandas.read_csv(fileName))

# [number, X, Y, prime]

#%% Greedy algorithm
# Let's assume the NP is situated at 
x_last = 50
y_last = 50
init = 0 # North Pole 
remaining_cities= data
pathway = np.array([[0,x_last, y_last, 0]])
for k in range(1,len(data)) :
    # compute distances between current location and remaining cities to be visited
    distances =  (data[:,1]-x_last)**2 + (data[:,2]-y_last)**2
    closest_index = np.argmin(distances)
    # record city ID in list
    pathway = np.concatenate((pathway,[remaining_cities[closest_index,:]]), axis=0)
    # pathway = pathway +remaining_cities[closest_index,:]
    # remove closest city from remaining to visit
    remaining_cities=np.delete(remaining_cities,[closest_index] , axis= 0)
