### Make model changes
1. Change your models (in models.py).

2. Run python manage.py makemigrations to create migrations for those changes
- we can see the changes in the migrations folder in the file with the correct initials

3. The sqlmigrate command takes migration names and returns their SQL for checking:
python manage.py sqlmigrate polls 0001 (initials)

4. Run python manage.py migrate to apply those changes to the database.



