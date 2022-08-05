#! /usr/bin/env bash
# Let the DB start
# python backend_pre_start.py

# Run migrations
# alembic upgrade head

# Create initial data in DB
# python initial_data.py

# export HOST_UVICORN=0.0.0.0

python main.py 
