#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "valustat_prototype.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

    # if is_testing:
    #         import coverage
    #         cov = coverage.coverage(source=['package1', 'package2'], omit=['*/tests/*'])
    #         cov.erase()
    #         cov.start()
    #
    # execute_from_command_line(sys.argv)
    #
    # if is_testing:
    #     cov.stop()
    #     cov.save()
    #     cov.report()
