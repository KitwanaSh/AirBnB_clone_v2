#!/usr/bin/python3
"""
Fabrci script that generate a archive of type tgz
of all files in the 'web_static'
"""

from collections.abc import Mapping
import fabric.api
import tarfile
import os.path
import re
from datetime import datetime

def do_pack():
	""" Generates a tgz archive """
    target = local("mkdir -p versions")
    name = str(datetime.now()).replace(" ", '')
    opt = re.sub(r'[^\w\s]', '', name)
    tar = local('tar -cvzf versions/web_static_{}.tgz web_static'.format(opt))
    if os.path.exists("./versions/web_static_{}.tgz".format(opt)):
        return os.path.normpath("/versions/web_static_{}.tgz".format(opt))
    else:
        return None
