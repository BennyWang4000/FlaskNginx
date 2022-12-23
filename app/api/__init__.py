import os
import sys
if '..' not in sys.path:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from .views import *