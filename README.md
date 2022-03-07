# Django-Token-Authentication
Demonstration of Token Authentication API &amp; it's consumption

## Registeration Model Serializer

<img src="https://raw.githubusercontent.com/Alexeino/Django-Token-Authentication/master/static/code.png" width=500px/>

## Registeration View

<img src="https://raw.githubusercontent.com/Alexeino/Django-Token-Authentication/master/static/rview.png" width=500px/>

## Settings.py

### Rest Framework
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',  # <-- And here
   ]
}
```

### Installed Apps

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    
    # Third Party
    'rest_framework',           #REST API
    'rest_framework.authtoken',  # <-- Here
]
```
