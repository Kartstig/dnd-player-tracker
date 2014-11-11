#!/usr/bin/ python
# -*- coding: utf-8 -*-

import os
from Config import *

def get_config():
    env = os.environ.get('ENV', 'Dev')
    if env == 'Dev':
        return DevelopmentConfig
    elif env == 'Test':
        return TestConfig
    elif env == 'Prod':
        return ProductionConfig
