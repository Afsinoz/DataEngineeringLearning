import argparse
import os
from time import time 
import pandas as pd
from sqlalchemy import create_engine



def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    # download the csv!!!
    csv_name = 'output.csv'
    
    os.system(f"wget {url} -O {csv_name}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()

    df_iter = pd.read_csv(csv_name,compression="gzip", iterator=True, chunksize=100000)
    df = next(df_iter)


    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime =  pd.to_datetime(df.tpep_dropoff_datetime)


    # This is for creating the table
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    # Adding the current chunk
    df.to_sql(name=table_name, con=engine, if_exists='append')


    while True:
        t_start = time()
        df = next(df_iter)

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime =  pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(name=table_name, con=engine, if_exists='append')

        t_end = time()

        print("appended another chunk... took %3f seconds" % (t_end - t_start))



if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Ingest CSV Data to PostGres')

    # Arguments needed
    # user, password, host, port, database name, table name,
    # URL for the CSV file

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database for postgres')
    parser.add_argument('--table_name', help='table name for postgres')
    parser.add_argument('--url', help='URL for the csv')

    args = parser.parse_args()


    main(args)



