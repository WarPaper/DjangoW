import os  
from waitress import serve  
from django.core.wsgi import get_wsgi_application
from DjangoW.wsgi import application  

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoW.settings")
    serve(application, host="0.0.0.0", port=os.environ["PORT"])