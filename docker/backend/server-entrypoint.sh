until cd /app/picasso/
do
    echo "Waiting for server volume..."
done


until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done


python manage.py collectstatic --noinput

gunicorn picasso.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4