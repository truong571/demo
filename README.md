# demo
Django Requires Python

  Cách cài đặt Python: https://realpython.com/installing-python/
  
  Cách cài đặt Pip: https://pip.pypa.io/en/stable/installation/
  
  Check installed
  
    python --version
    pip --version

Bước 1: Cài đặt Django

  Đảm bảo bạn đã cài đặt Python 3.6 trở lên. Sau đó, cài đặt Django bằng pip:

    py -m pip install Django

  Check installed

    django-admin --version

Bước 2: Tạo project Django

  Mở terminal và di chuyển đến thư mục muốn lưu trữ project Django. Sau đó, chạy lệnh sau:

    django-admin startproject myproject

  Lệnh này sẽ tạo ra một project Django mới với tên myproject.

Bước 3: Tạo app Django

  Di chuyển đến thư mục myproject và chạy lệnh sau:

    python manage.py startapp myapp

  Lệnh này sẽ tạo ra một app Django mới với tên myapp bên trong thư mục.

Bước 4: Cấu hình View

  cấu hình View trong đường dẫn myproject\myapp\views.py

    from django.http import HttpResponse

    def members(request):
        return HttpResponse("Hello world!")

Bước 5: Tạo URLS.py

  Tạo urls.py trong đường dẫn myproject\myapp

    from django.urls import path
    from . import views

    urlpatterns = [
        path('members/', views.members, name='members'),
    ]

  Cấu hình trong myproject\myproject\urls.py

    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path('', include('myapp.urls')),
        path('admin/', admin.site.urls),
    ]

Bước 5: Cấu hình Templates

  Tạo folder temolates trong myproject\myapp sau đó tạo một my_template.html trong myproject\myapp\templates

  Trong myproject\myapp\views.py 

    from django.template import loader

    def my_view(request):
      template = loader.get_template('my_template.html')
      return HttpResponse(template.render())

  Trong myproject\myapp\urls.py

    path('view/', views.my_view, name='my_view'),
  
  Trong myproject\myproject\settings.py thêm myapp

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'myapp',
    ]

  Sau đó chạy terminal 

    py manage.py migrate

Bước 6: Cấu hình Models

  Trong myproject\myapp\models.py

    from django.db import models

    class MyModel(models.Model):
        name = models.CharField(max_length=255)
    
  Sau đó chạy terminal 
    
    py manage.py makemigrations
    py manage.py migrate

Bước 7: Chạy server Django

  Chạy lệnh sau để khởi động server Django:
     
      python manage.py runserver
      
  Mở trình duyệt web và truy cập địa chỉ http://localhost:8000/. Bạn sẽ thấy trang web hiển thị nội dung của view my_view.
