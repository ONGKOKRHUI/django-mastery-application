### Make model changes
Change your models (in models.py).

Run python manage.py makemigrations to create migrations for those changes

Run python manage.py migrate to apply those changes to the database.

The sqlmigrate command takes migration names and returns their SQL:
python manage.py sqlmigrate polls 0001 (initials)

