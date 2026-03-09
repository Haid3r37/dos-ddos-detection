import pandas as pd

def load_dataset(file_path):
    """
    Load a dataset from a given file path.
    """
    dataset = pd.read_csv(file_path)
    return dataset
