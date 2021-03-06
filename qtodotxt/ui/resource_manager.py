import os
import sys
from PySide.QtGui import QIcon


def __getResourcesRoot():
    root = ''
    if sys.argv[0].lower().endswith('.exe'):
        root = os.path.dirname(sys.argv[0])
    elif getattr(sys, 'frozen', False):
        root = os.environ['RESOURCEPATH']
    else:
        file = None
        try:
            file = __file__
        except NameError:
            file = sys.argv[0]
        root = os.path.dirname(os.path.abspath(file))

    return os.path.join(root, 'resources')

resources_root = __getResourcesRoot()

def getResourcePath(resource_name):
    return os.path.join(resources_root, resource_name)

def getIcon(resource_name):
    return QIcon(getResourcePath(resource_name))
    
