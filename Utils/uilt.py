import pandas as pd
from config import *


def save_dataframe_to_dick(data):
    assert type(data) is pd.DataFrame
    data.to_csv(PROCESSED_DATA_PATH, header=True, index=False)