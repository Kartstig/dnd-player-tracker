#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Base import Base
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datetime

class Class(Base):

    __tablename__ = 'classes'
 
    id              = Column(Integer, primary_key=True)
    name            = Column(String(50), nullable=False)
    sub_class       = Column(String(50))
    min_str         = Column(Integer, nullable=False, default=0)
    min_dex         = Column(Integer, nullable=False, default=0)
    min_con         = Column(Integer, nullable=False, default=0)
    min_int         = Column(Integer, nullable=False, default=0)
    min_wis         = Column(Integer, nullable=False, default=0)
    min_char        = Column(Integer, nullable=False, default=0)
    created_at      = Column(DateTime, nullable=False)
    updated_at      = Column(DateTime, nullable=False)


    def __init__(self, name, sub_class=None, min_str=0, min_dex=0, 
                    min_con=0, min_int=0, min_wis=0, min_char=0):
        timestamp = datetime.now()
        self.name           = name
        self.created_at     = timestamp
        self.updated_at     = timestamp

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.name)
