# facing problems discription

- **Create venv**

``` bash
python -m venv .venv
```
- **Activate venv**

``` bash 
.venv\Scripts\activate
```
- **Install Django**

``` bash
pip install django
```
- **Install Requirements**
``` bash
pip install -r requirements.txt
```

- **Create Project**
``` bash 
django-admin startproject appname
```

- **Go to directry**
``` bash
cd appname
```

- **Start Project**

``` bash 
python manage.py runserver
```
# Jinja Templeting

``` bash
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Website{% endblock %}</title>
</head>
<body>
    {% block content %}
        <h1>Welcome to my website!</h1>
    {% endblock %}
    <footer>
        {% block footer %}
            <p>Copyright © 2021</p>
        {% endblock %}
    </footer>
</body>
</html>
```
- **Extend template**

``` bash
{% extends "base.html" %}

{% block title %}My Website{% endblock %}

{% block content %}
    <h1>Welcome to my website!</h1>
    <p>This is a child template.</p>
{% endblock %}
```

- **Include content**

``` bash
{% include "header.html" %}
```

- **Create new App**

``` bash
python manage.py startapp chai
```
- **Chek pip**

``` bash 
python -m ensurepip --upgrade
```

-**Alt**

``` bash
python -m pip install --upgrade pip
```

- **Install TailwindCss**

``` bash
pip install 'django-tailwind[reload]'
```

- **Add Tailwind to install apps**

``` bash
INSTALLED_APPS = [
    # ...
    'tailwind',
    # ...
]
```
- **Run Command to generate necessary files**

``` bash
python manage.py tailwind init
```

- **Add theme in install apps**

``` bash
INSTALLED_APPS = [
    # ...
    'theme',
    # ...
]
TAILWIND_APP_NAME = 'theme' # This is the name of the app that will be used to generate the tailwind files
INTERNAL_IPS = ['127.0.0.1']
```

## Now run the following command to generate the necessary files for your project:

``` bash 
python manage.py tailwind install
```

