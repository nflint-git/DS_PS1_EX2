import pandas as pd

def load_dataset(data):
    """
    load the dataset from a CSV
    
    
    """
    df = pd.read_csv(data, sep= ",")
    return df