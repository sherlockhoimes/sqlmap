#!/usr/bin/env python

"""
$Id$

This file is part of the sqlmap project, http://sqlmap.sourceforge.net.

Copyright (c) 2007-2010 Bernardo Damele A. G. <bernardo.damele@gmail.com>
Copyright (c) 2006 Daniele Bellucci <daniele.bellucci@gmail.com>

sqlmap is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free
Software Foundation version 2 of the License.

sqlmap is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along
with sqlmap; if not, write to the Free Software Foundation, Inc., 51
Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

import threading

from lib.core.data import logger

def timeout(func, args=(), kwargs={}, duration=1, default=None):
    class InterruptableThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = None

        def run(self):
            try:
                self.result = func(*args, **kwargs)
            except Exception, msg:
                logger.log(8, msg)
                self.result = default

    thread = InterruptableThread()
    thread.start()
    thread.join(duration)

    if thread.isAlive():
        return default
    else:
        return thread.result
