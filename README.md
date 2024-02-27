# demo

Bước 1: Cài đặt Django

  Đảm bảo bạn đã cài đặt Python 3.6 trở lên. Sau đó, cài đặt Django bằng pip:

    pip install django

Bước 2: Tạo project Django

  Mở terminal và di chuyển đến thư mục bạn muốn lưu trữ project Django. Sau đó, chạy lệnh sau:

    django-admin startproject myproject

  Lệnh này sẽ tạo ra một project Django mới với tên myproject.

Bước 3: Tạo app Django

  Di chuyển đến thư mục myproject và chạy lệnh sau:

    python manage.py startapp myapp

  Lệnh này sẽ tạo ra một app Django mới với tên myapp bên trong thư mục.

Bước 4: Cấu hình project Django

  Mở file settings.py trong thư mục myproject và thêm app myapp vào danh sách INSTALLED_APPS:

    INSTALLED_APPS = [
    ...
    'myapp',
    ]

Bước 5: Tạo model Django

  Mở file models.py trong thư mục myapp và tạo model Django đầu tiên:

    from django.db import models

    class MyModel(models.Model):
        name = models.CharField(max_length=255)
        
Bước 6: Tạo view Django

  Mở file views.py trong thư mục myapp và tạo view Django đầu tiên:

    from django.shortcuts import render

    def my_view(request):
        context = {}
        return render(request, 'my_template.html', context)

Bước 7: Tạo template Django

  Tạo một thư mục templates trong thư mục myapp và tạo file my_template.html bên trong:

    <h1>My View</h1>

    <p>This is my first Django view.</p>

Bước 8: Chạy server Django

  Chạy lệnh sau để khởi động server Django:

      python manage.py migrate
      python manage.py makemigrations
      python manage.py runserver
      
  Mở trình duyệt web và truy cập địa chỉ http://localhost:8000/. Bạn sẽ thấy trang web hiển thị nội dung của view my_view.
