import pandas as pd
import numpy as np 


def GetCityArray(path):
    """
    imports pandas data from path and extracts city information (start city is assumed to be the first entry)
    """
    df = pd.read_csv(path)
    cities = GetArrayDataFromDF(df)
    
    return(cities)



def GetArrayDataFromDF(df):
    """
    Takes df and extracts numpy arrays for city positions, primes.
    """
    cities = df[['X','Y','prime']].values
    #primes = df['prime'].values
    
    return(cities)

def RemoveCityFromArray(cities,index=0):
    "pops top city from city array using index for city row: default =0, i.e. first city in array"
    #### get city and prime data for city being popped
    #start_city = cities[index,:]
    #start_prime = primes[index]
    
    #### pop city and prime from each array
    new_cities = np.delete(cities,[index],axis=0)
    #new_primes = np.delete(primes,[index],axis=0)
    
    return(new_cities)

def GetStartCityFromArray(cities,index=0):
    "gets details for start city based on array index, default=0, i.e. first city in array"
    start_city = cities[index,:]
    #start_prime = primes[index]
    return(start_city)
    