#python manage.py collectstatic --noinput

python manage.py makemigrations mainapp
python manage.py migrate

#python manage.py flush --noinput

python manage.py fill_collections
python manage.py fill_products