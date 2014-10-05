#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Base import Base
from bcrypt import hashpw, gensalt
from sqlalchemy import Column, Integer, String, DateTime, Enum
from datetime import datetime
from flask.ext.login import UserMixin

class User(Base, UserMixin):

    __tablename__ = 'users'

    user_roles = ('user', 'admin', 'operator')

    id              = Column(Integer, primary_key=True)
    username        = Column(String(50), unique=True, nullable=False)
    password        = Column(String(60), nullable=False)
    first_name      = Column(String(50))
    last_name       = Column(String(50))
    phone_number    = Column(String(15))
    role            = Column(Enum(*user_roles), default='user', nullable=False)
    created_at      = Column(DateTime, nullable=False)
    updated_at      = Column(DateTime, nullable=False)

    def __init__(self, username, password, first_name=None, last_name=None, 
                 phone_number=None, role='user'):
        timestamp = datetime.now()
        self.username       = username
        self.password       = (self.pass_hash(password)) if password else None
        self.first_name     = first_name
        self.last_name      = last_name
        self.phone_number   = phone_number
        self.role           = role
        self.created_at     = timestamp
        self.updated_at     = timestamp

    @staticmethod
    def pass_hash(password):
        return hashpw(password.encode('utf-8'), gensalt())

    def valid_password(self, attempt):
        return (attempt and self.password 
            and hashpw(attempt.encode('utf-8'), self.password.encode('utf-8')) == self.password)

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.username)
        