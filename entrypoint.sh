#!/bin/sh

# エラー発生時にスクリプトを停止
set -e

echo "Running database migrations..."
python manage.py migrate --noinput

# echo "Collecting static files..."
# python manage.py collectstatic --noinput

echo "Starting application..."
exec "$@"
