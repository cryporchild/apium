# -*- coding: utf-8 -*-

"""
.. module: apium
    :platform: Unix, Windows
    :synopsis: User facing imports.

.. moduleauthor:: Christian Boelsen <christianboelsen+github@gmail.com>
"""


from concurrent.futures import (
    wait,
    as_completed,
    FIRST_COMPLETED,
    FIRST_EXCEPTION,
    ALL_COMPLETED,
)
from .exceptions import *   # pylint: disable=W0401
from .executor import TaskExecutor, Future
from .worker import register_task, schedule_task

# TODO:
# - Authentication
# - Encryption
# - Private tasks
# - More error checking:
#   - Problems unpickling task on the server.
#   - Problems unpickling results on the client.
#   - Chaining task to non existent parent.
# - Possible to backport a better chaining implementation to concurrent.futures??
#   - Probably not. Would need a reference to the executor in the future.
