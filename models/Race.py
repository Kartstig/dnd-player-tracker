#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Base import Base
from sqlalchemy import Column, Integer, String, DateTime, Enum
from datetime import datetime

class Race(Base):

    __tablename__ = 'races'

    id              = Column(Integer, primary_key=True)
    name            = Column(String(50), nullable=False)
    sub_race        = Column(String(50))
    lore            = Column(String(4000))
    strength        = Column(Integer, nullable=False)
    dexterity       = Column(Integer, nullable=False)
    constitution    = Column(Integer, nullable=False)
    intelligence    = Column(Integer, nullable=False)
    wisdom          = Column(Integer, nullable=False)
    charisma        = Column(Integer, nullable=False)
    special         = Column(String(50))
    created_at      = Column(DateTime, nullable=False)
    updated_at      = Column(DateTime, nullable=False)

    def __init__(self, name, strength, dexterity,
                    constitution, intelligence, wisdom,
                    charisma, sub_race=None, lore=None, special=None):
        timestamp = datetime.now()
        self.name           = name
        self.sub_race       = sub_race
        self.lore           = lore
        self.strength       = strength
        self.dexterity      = dexterity
        self.constitution   = constitution
        self.intelligence   = intelligence
        self.wisdom         = wisdom
        self.charisma       = charisma
        self.special        = special
        self.created_at     = timestamp
        self.updated_at     = timestamp

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.name)
        