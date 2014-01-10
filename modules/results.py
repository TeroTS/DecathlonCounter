# -*- coding: utf-8 -*-
__author__ = 'teros'

from gluon import *

def oldResultsForm():
    return FORM(P(INPUT(_type="integer", _name="year", requires=[IS_NOT_EMPTY("Anna vuosiluku !"), IS_INT_IN_RANGE(1998, 2015)])),
                P('', INPUT(_type="submit", _value="OK")))

#get old results
def getOldResults(form):
    db = current.db
    oldNames = []
    oldAidat = []
    oldPituus = []
    oldKuula = []
    oldSatanen = []
    oldSeivas = []
    oldNeljasataa = []
    oldKorkeus = []
    oldKiekko = []
    oldKeihas = []
    oldTuhatviisisataa = []
    yearQuery = (db.athlete.year == form.vars['year'])
    for athlete in db(yearQuery).select():
        #get names
        oldNames.append(athlete.name)
        #get sport results
        for sport in athlete.sport.select():
            if sport.name == 'aidat':
                oldAidat.append(sport.result)
            elif sport.name == 'pituus':
                oldPituus.append(sport.result)
            elif sport.name == 'kuula':
                oldKuula.append(sport.result)
            elif sport.name == 'satanen':
                oldSatanen.append(sport.result)
            elif sport.name == 'seivas':
                oldSeivas.append(sport.result)
            elif sport.name == 'neljasataa':
                oldNeljasataa.append(sport.result)
            elif sport.name == 'korkeus':
                oldKorkeus.append(sport.result)
            elif sport.name == 'kiekko':
                oldKiekko.append(sport.result)
            elif sport.name == 'keihas':
                oldKeihas.append(sport.result)
            elif sport.name == 'tuhatviisisataa':
                oldTuhatviisisataa.append(sport.result)
    return {'names':oldNames, 'aidat':oldAidat, 'pituus':oldPituus,
            'kuula':oldKuula, 'satanen':oldSatanen, 'seivas':oldSeivas,
            'neljasataa':oldNeljasataa, 'korkeus':oldKorkeus, 'kiekko':oldKiekko,
            'keihas':oldKeihas, 'tuhatviisisataa':oldTuhatviisisataa}
