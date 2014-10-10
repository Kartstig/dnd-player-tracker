#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Base import Base
from sqlalchemy import ForeignKey, Column, Integer, String, DateTime

class Spellbook(Base):

    __tablename__ = 'spellbooks'

    id              = Column(Integer, primary_key=True)
    character_id    = Column(Integer, ForeignKey('characters.id'), nullable=False)
    spell_id        = Column(Integer, ForeignKey('spells.id'), nullable=False)

    def __init__(self, character_id, spell_id):
        self.character_id   = character_id
        self.spell_id       = spell_id

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.id)
        