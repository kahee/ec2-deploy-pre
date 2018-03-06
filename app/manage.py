#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # 장고가 돌아가고 있는 환경에서 ./manage.py 를 실행되면 아래 코드가 실행 됨

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
