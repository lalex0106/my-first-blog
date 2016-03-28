# cmd: Create virtual environment
C:\Users\Name\djangogirls> C:\Python34\python -m venv myvenv

# Start your virtual environment by running:
C:\Users\Name\djangogirls> myvenv\Scripts\activate

# start a new Django project
(myvenv) C:\Users\Name\djangogirls> django-admin startproject mysite .

# Modify settings.py
TIME_ZONE = 'Asia/Shanghai'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# cmd:
python
# import sys
# sys.path.append(r'C:\Users\Administrator\AppData\Local\Programs\Python\Python35\Lib\site-packages\django\template\backends')
python manage.py migrate 
# 由于Python运行在venv环境，该环境未安装django，导致出错。应该进入venv环境后pip install django-admin

python manage.py runserver
#If you are on Windows and this fails with  UnicodeDecodeError , use this command instead:
#python manage.py runserver 0:8000

(myvenv) ~/djangogirls$ python manage.py startapp blog

#在mysite/settings.py中添加blog，如下：
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'blog',
]

python manage.py makemigrations blog

python manage.py migrate blog

#修改blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)

#创建管理员账户

