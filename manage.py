#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    # Configurações específicas para o Djongo/MongoDB
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Ajuste para o Django + MongoDB
    from mongoengine import connect
    from django.conf import settings

    # Conecta ao MongoDB antes de executar comandos
    if 'runserver' in sys.argv or 'migrate' in sys.argv:
        connect(
            db=settings.DATABASES['default']['NAME'],
            host=settings.DATABASES['default']['CLIENT']['host']
        )
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()