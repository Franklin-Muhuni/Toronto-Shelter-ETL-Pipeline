import io
import requests
import pandas as pd

class Extract:
    #retrieves dataset from GC storage & converts to dataframe
    def extract_data_gcp(self):
        url = 'https://storage.googleapis.com/fm-data-eng/Shelter%20Data.csv'
        r = requests.get(url)
        df = pd.read_csv(io.StringIO(r.text), sep=',')

        return df
