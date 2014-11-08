#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Base import Base
from models.User import User

class UserService(Base):
    __model__ = User