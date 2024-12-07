#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    
    # Setting the default settings module for Django
    # You might want to replace 'moviereview.settings' with your own settings file
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviereview.settings')

    try:
        # Importing Django's execute_from_command_line function
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Adding command-line arguments to execute Django management commands
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    # Execute the management commands
    main()
