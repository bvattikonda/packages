#!/usr/bin/env python
import datetime
import hashlib

datehandler = lambda obj: obj.isoformat() if\
    isinstance(obj, datetime.datetime) else\
    None

def md5_for_file(filehandle, block_size=2**20):
    md5 = hashlib.md5()
    while True:
        data = filehandle.read(block_size)
        if not data:
            break
        md5.update(data)
    return md5.digest()
