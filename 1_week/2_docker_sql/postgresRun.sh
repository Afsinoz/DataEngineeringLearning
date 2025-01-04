#!/opt/homebrew/bin/bash

POSTGRES_USER="root"
POSTGRES_PASSWORD="root"
POSTGRES_DB="ny_taxi"
HOST_PORT=5433
CONTAINER_PORT=5432
DATA_DIR="$(pwd)/ny_taxi_postgres_data"
NETWORK="pg-network"
NAME="pg-database"
# Docker Command


docker run -it \
 -e POSTGRES_USER=$POSTGRES_USER \
 -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
 -e POSTGRES_DB=$POSTGRES_DB \
 -v $DATA_DIR:/var/lib/postgresql/data \
 -p $HOST_PORT:$CONTAINER_PORT \
 --network=$NETWORK \
 --name $NAME \
postgres:13



