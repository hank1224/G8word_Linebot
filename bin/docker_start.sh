#!/usr/bin/env bash
NAME="G8word" # Name of the application
DJANGODIR=/code/G8word # Django project directory
USER=root # the user to run as
GROUP=root # the group to run as

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR

export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Wait for the database to be ready
echo "Waiting for database to be ready..."
until PGPASSWORD=$POSTGRES_PASSWORD psql -h db -U $POSTGRES_USER -d $POSTGRES_DB -c '\q' > /dev/null 2>&1; do
  sleep 1
done
echo "Database is ready!"

python manage.py makemigrations && \
  python manage.py migrate && \
  # exec "$@"` 會執行 `command` 定義的指令
  exec "$@"