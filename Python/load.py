import pandas as pd
from google.cloud import bigquery

class Load:
    #initialize nested dictionary object
    def __init__(self, dicts):
        self.dicts = dicts

    #loading function
    def load_data_bq(self):
        #return copy of dictionary
        data = self.dicts.copy()
        #create GCP BQ client
        client = bigquery.Client()

        #iterates through nested dictionary
        for key, value in data.items():
            #defines table id name
            table_id = 'fifth-byte-392819.shelter_data_eng.{}'.format(key)
            #sets load job to appends data
            job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
            #defines load job
            job = client.load_table_from_dataframe(pd.DataFrame(value), table_id, job_config=job_config)
            job.result()

            #retrieves table if exists
            table = client.get_table(table_id)