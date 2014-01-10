# -*- coding: utf-8 -*-
__author__ = 'teros'

from gluon import *

def compoundForm():
    return FORM(P(INPUT(_type="integer", _name="year", requires=[IS_NOT_EMPTY("Anna vuosiluku !"), IS_INT_IN_RANGE(1998, 2015)])),
                P(INPUT(_type='checkbox', _name='calc'), 'Laske Pisteet'),
                P('', INPUT(_type="submit", _value="OK")))

#compound result calculation form (Yhteistulos)
#calculate compound result and update db
def getCompoundResults(form):
    db = current.db
    yearQuery = (db.athlete.year == form.vars['year'])
    writeCheck = form.vars['calc']
    #write db only if write tab checked
    if writeCheck == 'on':
        #calculate overall points and write db for every athlete
        for athlete in db(yearQuery).select():
            points = 0
            #calculate overall points
            for sport in athlete.sport.select():
                points += sport.points
                #get athlete
            row = db((db.athlete.name == athlete.name) & yearQuery).select().first()
            #write overall result to db
            row.update_record(score=points)
            #get ordered overall points
    return db(yearQuery).select(orderby=~db.athlete.score)