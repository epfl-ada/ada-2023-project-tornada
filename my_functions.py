"""
This file contains the functions created by the team for the project

(For the BA analysis)


"""

import pandas as pd 
import numpy as np


def csv_to_df(CSV_FILE_PATH, columns = None):

    '''
    Reads a .csv file into a dataframe and specifies the datatype of each column based on the dtypes dictionary.

    Parameters:
    CSV_FILE_PATH (str): The path to the .csv file.
    columns (list of str, optional): A list of column names to include in the DataFrame. 
                                     If None, all columns are included.

    Returns:
    pandas.DataFrame: A DataFrame containing the data from the csv file.
    
    '''

    dtypes = {  'beer_name': 'object',
                  'beer_id': 'uint32',
                  'brewery_name': 'object',
                  'brewery_id': 'uint32',
                  'style': 'object',
                  'abv': 'float32',
                  'date' : 'uint64',
                  'user_name': 'object',
                  'user_id': 'object',
                  'appearance':'float32',
                  'aroma': 'float32',
                  'palate': 'float32',
                  'taste':'float32',
                  'overall': 'float32',
                  'rating': 'float32',
                  'text': 'object',
                  'review': 'bool_',
                  'nbr_ratings': 'uint32',
                  'nbr_reviews': 'uint32',
                  'joined': 'uint64',
                  'location': 'object',
                  'id': 'uint32',
                  'name': 'object',	
                  'nbr_beers': 'uint32',
                  'avg': 'float32',							
                  'ba_score':'float32',	
                  'bros_score': 'float32',	
                  'avg_computed': 'float32',	
                  'zscore':'float32',	
                  'nbr_matched_valid_ratings': 'uint32',
                  'avg_matched_valid_ratings': 'float32'}
    
    if columns is not None:

        df = pd.read_csv(CSV_FILE_PATH, columns= columns)
        selected_dtypes = {k: dtypes[k] for k in columns}

    else:

        df = pd.read_csv(CSV_FILE_PATH)
        selected_dtypes = {k: dtypes[k] for k in list(df.columns)}

    
    df = df.astype(selected_dtypes)

    return df

def map_style_to_family(style, restructured_dict):

    '''
    Checks if beer substyle string is conatined in the key of a dictionary mapping
    and returns the family style value 

    Parameters:
    substyle (str): Beer style
    restructured_dict (dict): Dictionary with key = style : value = family
    
    Returns:
    family (str): Family of the beer style
    

    '''
    
    # Iterating through the keys
     
    for key, value in restructured_dict.items():
        if key in style:
            return value
        
        elif 'IPA' in style:

            return 'India Pale Ales'
        
    
    return np.NAN  # or any default value you prefer

