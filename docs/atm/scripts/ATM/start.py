import os
import sys
from core import src

BASE_PATH = os.path.dirname(__file__)
sys.path.append(BASE_PATH)

if __name__ == '__main__':
    src.run()
