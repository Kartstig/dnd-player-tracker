#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Base import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class Spell(Base):

    __tablename__ = 'spells'

    schools = ('conjuration', 'destruction', 'alteration')

    id              = Column(Integer, primary_key=True)
    name            = Column(String(50), nullable=False)
    description     = Column(String(4000), nullable=False)
    school          = Column(Enum(*schools), nullable=False)
    level           = Column(Integer, nullable=False)
    range           = Column(Integer, nullable=False)
    duration        = Column(Integer, nullable=False)
    casting_time    = Column(Integer, nullable=False)
    area            = Column(Integer, nullable=False)
    saving_throw    = Column(Integer, nullable=False)
    is_reversible   = Column(Boolean, nullable=False)
    created_at      = Column(DateTime, nullable=False)
    updated_at      = Column(DateTime, nullable=False)

    def __init__(self, name, description, school, level, range, duration, casting_time,
                    area, saving_throw, is_reversible):
        timestamp = datetime.now()
        self.name           = name
        self.description    = description
        self.school         = school
        self.level          = level
        self.range          = range
        self.duration       = duration
        self.casting_time   = casting_time
        self.area           = area
        self.saving_throw   = saving_throw
        self.is_reversible  = is_reversible
        self.created_at     = timestamp
        self.updated_at     = timestamp

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.name)
        