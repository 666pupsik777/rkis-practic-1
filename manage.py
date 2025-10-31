#!/usr/bin/env python
"""Импортируются встроенные модули Python для взаимодействия с операционной системой и интерпретатором"""
import os
import sys


def main():

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')
    """Пытается импортировать функцию execute_from_command_line из ядра Django.
       Если Django не установлен или не находится в PYTHONPATH, возникает ошибка"""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    """(запуск административ. инструмента)"""
    execute_from_command_line(sys.argv)

""" точка входа. гарантирует что функция будет вызвана только в том случае если скрипт запускается напрямую"""

if __name__ == '__main__':
    main()
