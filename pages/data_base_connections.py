import pandas as pd
from google.cloud import bigquery
import pydata_google_auth

# connecting to bigquery
credentials = pydata_google_auth.get_user_credentials(
   ['https://www.googleapis.com/auth/bigquery'],
)
project_id = 'peak-essence-367304'



def get_mysql_data(query):
    try:
        df = pd.read_gbq(query,project_id='peak-essence-367304',credentials=credentials)
        return df
    except Exception as e:
        print(str(e))
        print("unable to fetch data")
        return None




