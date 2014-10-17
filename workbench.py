#!/usr/bin/ python
# -*- coding: utf-8 -*-

import csv
import re
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Config import *
from models import *

def import_data():
    bootstrap_races()
    bootstrap_classes()
    bootstrap_users()
    bootstrap_characters()
    bootstrap_spells()

def bootstrap_spells():
    spells_import = csv_import('libs/resources/spells.csv')
    try:
        print "Building test spells..."
        for spell in spells_import:
            print "Spell: {}".format(spell['name'])
            session.add(Spell(**spell))
    except:
        print "Failed."
    c = session.query(Character).first()
    for s in session.query(Spell).all():
        c.spells.append(s)

def bootstrap_classes():
    class_import = csv_import('libs/resources/classes.csv')
    try:
        print "Building test classes..."
        for _class in class_import:
            print "Class: {}".format(_class['name'])
            session.add(Class(**_class))
    except:
        print "Failed."

def bootstrap_characters():
    characters = [
        {
            "name":         "Talos",
            "xp":           3719,
            "level":        2,
            "strength":     9,
            "dexterity":    12,
            "constitution": 12,
            "intelligence": 18,
            "wisdom":       15,
            "charisma":     9,
            "sex":          "M",
            "alignment":    "good",
            "behavior":     "chaotic",
            "height":       163,
            "weight":       77,
            "hair_color":   "gray",
            "age":          70,
            "race_id":      session.query(Race).first().id,
            "user_id":      session.query(User).first().id,
            "class_id":     session.query(Class).first().id
        },
        {
            "name":         "Apollonius",
            "xp":           10115,
            "level":        4,
            "strength":     11,
            "dexterity":    12,
            "constitution": 12,
            "intelligence": 18,
            "wisdom":       15,
            "charisma":     9,
            "sex":          "M",
            "alignment":    "good",
            "behavior":     "chaotic",
            "height":       163,
            "weight":       77,
            "hair_color":   "gray",
            "age":          70,
            "race_id":      session.query(Race).first().id,
            "user_id":      session.query(User).first().id,
            "class_id":     session.query(Class).first().id
        },
        {
            "name":         "Count Augustus",
            "xp":           1130,
            "level":        1,
            "strength":     2,
            "dexterity":    12,
            "constitution": 12,
            "intelligence": 18,
            "wisdom":       15,
            "charisma":     9,
            "sex":          "M",
            "alignment":    "evil",
            "behavior":     "chaotic",
            "height":       163,
            "weight":       77,
            "hair_color":   "gray",
            "age":          70,
            "race_id":      session.query(Race).first().id,
            "user_id":      session.query(User).first().id,
            "class_id":     session.query(Class).first().id
        },
        {
            "name":         "Cartinonus VI",
            "xp":           830,
            "level":        1,
            "strength":     3,
            "dexterity":    12,
            "constitution": 12,
            "intelligence": 18,
            "wisdom":       15,
            "charisma":     9,
            "sex":          "M",
            "alignment":    "evil",
            "behavior":     "Lawful",
            "height":       163,
            "weight":       77,
            "hair_color":   "gray",
            "age":          70,
            "race_id":      session.query(Race).first().id,
            "user_id":      session.query(User).first().id,
            "class_id":     session.query(Class).first().id
        }
    ]
    try:
        print "Building test characters..."
        for c in characters:
            session.add(Character(**c))
    except:
        print "Failed."




def bootstrap_races():
    races = csv_import('libs/resources/raceDBs.csv')
    try:
        print "Building test races..."
        for r in races:
            (race, subrace) = strip_race(r['Race'])
            r['Race'] = race
            r['SubRace'] = subrace
            r['Str'] = strip_sign(r['Str'])
            r['Dex'] = strip_sign(r['Dex'])
            r['Con'] = strip_sign(r['Con'])
            r['Int'] = strip_sign(r['Int'])
            r['Wis'] = strip_sign(r['Wis'])
            r['Cha'] = strip_sign(r['Cha'])
            print "Race:{}:{}  {}/{}/{}/{}/{}".format(
                r['Race'], r['SubRace'], r['Str'], r['Con'], 
                r['Int'], r['Wis'], r['Cha']
            )
            session.add(Race(
                name=r['Race'],
                sub_race=r['SubRace'],
                strength=r['Str'],
                dexterity=r['Dex'],
                constitution=r['Con'],
                intelligence=r['Int'],
                wisdom=r['Wis'],
                charisma=r['Cha']
                )
            )
    except:
        print "Failed."


def bootstrap_users():
    users = [
        {
            "username":     "kartstig@gmail.com",
            "password":     "1234",
            "first_name":   "Herman",
            "last_name":    "Singh",
            "phone_number": "4105416360",
            "role":         "admin"
        }
    ]

    try:
        print "Building test users..."
        for user in users:
            session.add(User(**user))
    except:
        print "Failed."

def strip_sign(text):
    text = str(text)
    neg = re.search(r"(–)", text)
    m = re.search(r"([\d]+)", text)
    if m:
        res = m.group(0)
        if neg:
            return int('-{}'.format(res))
        else:
            return int(res)
    else:
        return 0

def strip_race(text):
    text = str(text)
    r = re.search(r"^([a-zA-Z]+)", text)
    sr = re.search(r"^[a-zA-Z]+,[^\w]([a-zA-Z]+)",text)
    return (
            (r.group(0) if r is not None else ""),
            (sr.group(1) if sr is not None else "")
            )

def csv_import(filename):

    container = []
    with open(filename,'r') as csvfile:
        reader = csv.DictReader(
            csvfile, delimiter=','
        )
        for r in reader:
            container.append(r)
        return container

if __name__ == '__main__':
    engine = create_engine(DevelopmentConfig.SQLALCHEMY_DATABASE_URI)
    session = sessionmaker(bind=engine)()

