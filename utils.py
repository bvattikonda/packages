#!/usr/bin/env python
from datetime import datetime
import hashlib
import os

datehandler = lambda obj: obj.isoformat() if\
    isinstance(obj, datetime) else\
    None

def md5_for_file(filehandle, block_size=2**20):
    md5 = hashlib.md5()
    while True:
        data = filehandle.read(block_size)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()

def md5_for_string(message):
    md5 = hashlib.md5()
    md5.update(message)
    return md5.hexdigest()

def already_running(prog):
    procfiles = os.listdir('/proc') 
    for procfilename in procfiles:
        if not procfilename.isdigit():
            continue
        cmdlinefilename = os.path.join('/proc',\
                        procfilename, 'cmdline')
        if not os.path.exists(cmdlinefilename):
            continue
        cmdlinefile = open(cmdlinefilename)
        cmdline = cmdlinefile.readline()
        if prog in cmdline and int(procfilename) != os.getpid()\
            and cmdline.startswith('python'):
            return True
    return False

def total_mins(start, end):
    td = (end - start)
    return (td.seconds + td.days * 24 * 3600) / 60.0
