import os
from django.core.wsgi import get_wsgi_application

# 设置默认的 Django 设置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campus_portal.settings')

# 创建 WSGI 应用实例
application = get_wsgi_application()
