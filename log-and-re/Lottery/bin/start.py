#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Michaeldong
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from core import src

if __name__ == '__main__':
    src.run()
