# -*- coding: utf-8 -*-
__author__ = 'teros'

from gluon import *

def aamForm():
    return FORM(P(INPUT(_type="integer", _name="year", requires=[IS_NOT_EMPTY("Anna vuosiluku !"), IS_INT_IN_RANGE(1998, 2015)])),
                P(INPUT(_type='checkbox', _name='calcAam'), 'Laske Pisteet'),
                P('', INPUT(_type="submit", _value="OK")))

#remove duplicates from ordered aam list (kind of hack, but distinct=db.athlete.name didn't work)
def removeDuplicateRows(rows):
    namesAam = []
    rowsAam = []
    for row in rows:
        #if aam for this name not yet available, get it
        if not (row.name in namesAam):
            rowsAam.append(row)
            namesAam.append(row.name)
    return rowsAam

#aam result calculation form (AAM)
#calculate aam result and update db
def getAamResults(form):
    db = current.db
    #get the names of all athletes and loop through them
    for athlete in db().select(db.athlete.name, distinct=True):
        yearQuery = (db.athlete.year <= form.vars['year'])
        writeCheck = form.vars['calcAam']
        #write db only if write tab on and athlete exists
        if writeCheck == 'on':
            #get all rows of a single athlete
            athleteRows = db((db.athlete.name == athlete.name) & yearQuery).select()
            points = 0
            #calculate AAM points
            for rowAthlete in athleteRows:
                points += rowAthlete.score
                #if athlete row exists
            if athleteRows:
                #get the last (=latest) athlete row
                row = db((db.athlete.name == athlete.name) & yearQuery).select().last()
                #write AAM result to db
                row.update_record(aam=points)
    #get ordered AAM points
    rowsAamTmp = db(db.athlete.year <= form.vars['year']).select(db.athlete.name, db.athlete.aam,
                                                                 orderby=~db.athlete.aam)
    return removeDuplicateRows(rowsAamTmp);


