### command
start project `django-admin startprogect project_name`
create app `python manage.py startapp app_name`
runserver `python manage.py runserver`

create migration `python manage.py makemigrations`
run migration `python manage.py migrate`

create username for admin `python manage.py createsuperuser`
if have this error
```
Superuser creation skipped due to not running in a TTY. You can run `manage.py createsuperuser` in your project to create one manually.
```
run `winpty python manage.py createsuperuser`

see sql code `python manage.py sqlmigrate blog 0001` app_name and migration number

install `pip install --user django-crispy-forms` to styling form


## Node
- find `BlogConfig` in the `apps.py` 


```
###Object-relational Mappers (ORMs)
An object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational databases tables into objects that are more commonly used in application code.
```

- `python manage.py shell`
- `from blog.models import Post` import models
- `from django.contrib.auth.models import User` import user
- `User.objects.all()` see all user
- `user = User.objects.get(id=1)`  get user by id in python shell
- ` post_2 = Post(title='New Years Day', content='Jackie was sleeping on the bed', author=user)` make new post from user
- `post_2.save()` seve it to DB
- `Post.objects.all()` 
-  `user.post_set.all()` see post by user
- `user.post_set.create(title='post 3', content='Third post')` create post by user
- 




### Doc
- `https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#date` Django date format