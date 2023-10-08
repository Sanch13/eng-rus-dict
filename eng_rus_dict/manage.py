#!/usr/bin/env python
<<<<<<< HEAD
"""Django's command-line utility for administrative tasks."""
=======
"""Django's command-line utility for administrative tasks.!!!"""
>>>>>>> 6031d00315c76a9d653cc8a9bcd0dedef69ad018
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eng_rus_dict.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
