#!/usr/bin/ python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Config import *

def get_session():
    engine = create_engine(DevelopmentConfig.SQLALCHEMY_DATABASE_URI)
    return sessionmaker(bind=engine)()

if __name__ == '__main__':
    pass