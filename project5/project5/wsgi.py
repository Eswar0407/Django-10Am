"""
WSGI config for project5 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
>>>>>>> e01526900fb7b26f31a5b9d957298f9b577a70e4
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project5.settings')

application = get_wsgi_application()
