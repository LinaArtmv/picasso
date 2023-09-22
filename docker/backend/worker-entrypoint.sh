until cd /app/picasso/
do
    echo "Waiting for server volume..."
done

python -m celery -A picasso worker -l info --concurrency 1 -E
