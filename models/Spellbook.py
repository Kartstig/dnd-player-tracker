#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Base import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class Spellbook(Base):

    __tablename__ = 'spellbooks'

    school = ('conjuration', 'destruction', 'alteration')

    id              = Column(Integer, primary_key=True)
    character_id    = Column(Boolean, nullable=False)
    spell_id        = Column(Boolean, nullable=False)
    created_at      = Column(DateTime, nullable=False)
    updated_at      = Column(DateTime, nullable=False)

    def __init__(self, character_id, spell_id):
        timestamp = datetime.now()
        self.character_id   = character_id
        self.spell_id       = spell_id
        self.created_at     = timestamp
        self.updated_at     = timestamp

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.id)
        