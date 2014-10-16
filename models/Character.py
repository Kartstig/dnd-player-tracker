#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Base import Base
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datetime

class Character(Base):

    __tablename__ = 'characters'
 
    sex = ('M','F')

    id              = Column(Integer, primary_key=True)
    name            = Column(String(50), nullable=False)
    xp              = Column(Integer, nullable=False)
    level           = Column(Integer, nullable=False)
    strength        = Column(Integer, nullable=False)
    dexterity       = Column(Integer, nullable=False)
    constitution    = Column(Integer, nullable=False)
    intelligence    = Column(Integer, nullable=False)
    wisdom          = Column(Integer, nullable=False)
    charisma        = Column(Integer, nullable=False)
    sex             = Column(Enum(*sex), nullable=False)
    alignment       = Column(String(50), nullable=False)
    behavior        = Column(String(50), nullable=False)
    height          = Column(Integer)
    weight          = Column(Integer)
    hair_color      = Column(String(50))
    age             = Column(String(50))
    race_id         = Column(Integer, ForeignKey('races.id'), nullable=False)
    user_id         = Column(Integer, ForeignKey('users.id'), nullable=False)
    user_id         = Column(Integer, ForeignKey('classes.id'), nullable=False)
    created_at      = Column(DateTime, nullable=False)
    updated_at      = Column(DateTime, nullable=False)

    spells          = relationship("Spell",
                        secondary="spellbooks", 
                        backref="casters")

    race            = relationship("Race",
                        backref="characters")

    def __init__(self, name, strength, dexterity, constitution, intelligence, wisdom, 
                    charisma, sex, alignment, behavior, race_id, user_id, height=0, 
                    weight=0, hair_color=None, age=None, xp=0, level=1):
        timestamp = datetime.now()
        self.name           = name
        self.xp             = xp
        self.level          = level
        self.strength       = strength
        self.dexterity      = dexterity
        self.constitution   = constitution
        self.intelligence   = intelligence
        self.wisdom         = wisdom
        self.charisma       = charisma
        self.sex            = sex
        self.alignment      = alignment
        self.behavior       = behavior
        self.height         = height
        self.weight         = weight
        self.hair_color     = hair_color
        self.age            = age
        self.race_id        = race_id
        self.user_id        = user_id
        self.created_at     = timestamp
        self.updated_at     = timestamp

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.name)
