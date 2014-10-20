#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Base import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class Armor(Base):

    __tablename__ = 'armor'

    id              = Column(Integer, primary_key=True)
    name            = Column(Boolean, nullable=False)
    cost            = Column(Integer, nullable=False)
    weight          = Column(Integer, nullable=False)
    armor_class     = Column(Integer, nullable=False)
    created_at      = Column(DateTime, nullable=False)
    updated_at      = Column(DateTime, nullable=False)

    def __init__(self, name, cost, weight, armor_class):
        timestamp = datetime.now()
        self.name           = name
        self.cost           = cost
        self.weight         = weight
        self.armor_class    = armor_class
        self.created_at     = timestamp
        self.updated_at     = timestamp

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.name)