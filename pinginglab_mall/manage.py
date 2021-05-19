#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    # 原来的设置：通过工程直接找到settings.py文件（settings.py文件在工程主目录下）
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pinginglab_mall.settings')
    # 现在需要设置为：找到settings目录下的dev.py这个设置文件
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pinginglab_mall.settings.dev')
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
