# -*- coding: utf-8 -*-
__author__ = 'teros'

from gluon import *

#get track event record from database
def getTrackEventRecord(event):
    db = current.db
    recordRow = db((db.sport.name == event) & (db.sport.result != 0.0)).select(db.sport.athlete_id,
                                                                                 db.sport.result,
                                                                                 db.sport.points,
                                                                                 orderby=db.sport.result).first()
    return recordRow

#get field event record from database
def getFieldEventRecord(event):
    db = current.db
    recordRow = db((db.sport.name == event) & (db.sport.result != 0.0)).select(db.sport.athlete_id,
                                                                                 db.sport.result,
                                                                                 db.sport.points,
                                                                                 orderby=~db.sport.result).first()
    return recordRow

def getRecordNameAndYear(id):
    db = current.db
    nameAndYear = db(db.athlete.id == id).select(db.athlete.name, db.athlete.year).first()
    return nameAndYear



