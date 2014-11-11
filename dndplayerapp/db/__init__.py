#!/usr/bin/ python
# -*- coding: utf-8 -*-

from .. import get_config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_session():
    engine = create_engine(get_config().SQLALCHEMY_DATABASE_URI)
    return sessionmaker(bind=engine)()

if __name__ == '__main__':
    pass