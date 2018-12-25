# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:54:08 2018

@author: evill
"""

import pandas
import numpy as np
import utils 
import solvers_greedy
#%% Import data
fileName= 'C:\\Users\\evill\\Documents\\Santa\\data\\clean_s100.csv'

data =np.array(pandas.read_csv(fileName))
#data = GetCityArray(fileName)
# [number, X, Y, prime]

#%% call greedy
    
pathway_simpleGreedy, total_distance_simpleGreedy = solvers_greedy.simpleGreedy(data, 0)

# add the distance to come back to the NP
total_distance_simpleGreedy= total_distance_simpleGreedy+    \
    np.sqrt( (pathway_simpleGreedy[0,1]-pathway_simpleGreedy[-1,1])**2 + \
            (pathway_simpleGreedy[0,2]-pathway_simpleGreedy[-1,2])**2)

#%% Greedy with prime constraint
pathway_greedy, total_distance_greedy = solvers_greedy.greedyPrimeConstraint(data, 0)

# add the distance to come back to the NP
total_distance_greedy = total_distance_greedy +   \
     np.sqrt( (pathway_greedy[0,1]-pathway_greedy[-1,1])**2 + \
             (pathway_greedy[0,2]-pathway_greedy[-1,2])**2)
