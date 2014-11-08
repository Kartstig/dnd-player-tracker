#!/usr/bin/ python
# -*- coding: utf-8 -*-

from db import get_session

class Base(object):
    __model__ = None

    session = get_session()

    def is_instance(self, model):
        return isinstance(model, self.__model__)

    def get(self, id):
        return self.session.query(self.__model__).filter_by(id=id).one()

    def save(self, model):
        session.add(model)
        session.commit()

    def delete(self, model):
        session.remove(model)
        session.commit()