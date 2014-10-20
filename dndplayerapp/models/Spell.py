#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Base import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime

class Spell(Base):

    __tablename__ = 'spells'

    id              = Column(Integer, primary_key=True)
    name            = Column(String(50), nullable=False)
    description     = Column(String(4000))
    school          = Column(String(50), nullable=False)
    components      = Column(String(50), nullable=False)
    level           = Column(String(50), nullable=False)
    range           = Column(String(50), nullable=False)
    damage          = Column(String(50), nullable=False)
    duration        = Column(String(50), nullable=False)
    casting_time    = Column(String(50), nullable=False)
    area            = Column(String(50), nullable=False)
    saving_throw    = Column(String(50), nullable=False)
    is_reversible   = Column(Boolean, nullable=False)
    created_at      = Column(DateTime, nullable=False)
    updated_at      = Column(DateTime, nullable=False)

    def __init__(self, name, school, components, level, range,
                damage, duration, casting_time, area, 
                saving_throw, is_reversible, description=None):
        timestamp = datetime.now()
        self.name           = name
        self.description    = description
        self.school         = school
        self.components     = components
        self.level          = level
        self.range          = range
        self.damage         = damage
        self.duration       = duration
        self.casting_time   = casting_time
        self.area           = area
        self.saving_throw   = saving_throw
        self.is_reversible  = is_reversible
        self.created_at     = timestamp
        self.updated_at     = timestamp

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.name)
        