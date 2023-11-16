#!/bin/bash

set -e
source .env

docker-compose build --build-arg POSTGRES_PASSWORD=$POSTGRES_PASSWORD --build-arg POSTGRES_DB=$POSTGRES_DB --build-arg POSTGRES_USER=$POSTGRES_USER
docker-compose up --remove-orphans
