# -*- coding: utf-8 -*- 
__author__ = 'teros'

from gluon import *

def athletesForm():
    return FORM(TABLE(
            TR('Antti Puhakka', INPUT(_type='checkbox', _name='Antti Puhakka')),
            TR('Antti Sepponen', INPUT(_type='checkbox', _name='Antti Sepponen')),
            TR('Esa Mikkonen', INPUT(_type='checkbox', _name='Esa Mikkonen')),
            TR('Harri Muikku', INPUT(_type='checkbox', _name='Harri Muikku')),
            TR('Jan Kiljunen', INPUT(_type='checkbox', _name='Jan Kiljunen')),
            TR('Jani Taivalantti', INPUT(_type='checkbox', _name='Jani Taivalantti')),
            TR('Jari Kurvinen', INPUT(_type='checkbox', _name='Jari Kurvinen')),
            TR('Jari Rantalainen', INPUT(_type='checkbox', _name='Jari Rantalainen')),
            TR('Jarmo Marttinen', INPUT(_type='checkbox', _name='Jarmo Marttinen')),
            TR('Panu Tuomikko', INPUT(_type='checkbox', _name='Panu Tuomikko')),
            TR('Pauli Kartano', INPUT(_type='checkbox', _name='Pauli Kartano')),
            TR('Pekka Miettinen', INPUT(_type='checkbox', _name='Pekka Miettinen')),
            TR('Sami Vesalainen', INPUT(_type='checkbox', _name='Sami Vesalainen')),
            TR('Teemu Tiusanen', INPUT(_type='checkbox', _name='Teemu Tiusanen')),
            TR('Tero Suhonen', INPUT(_type='checkbox', _name='Tero Suhonen')),
            TR('Ville Syrjäläinen', INPUT(_type='checkbox', _name='Ville Syrjalainen')),
            P(''),
            TR('Yleinen', INPUT(_type='radio', _name='ageSelect', _value='yleinen')),
            TR('M35', INPUT(_type='radio', _name='ageSelect', _value='m35')),
            TR('M40', INPUT(_type='radio', _name='ageSelect', _value='m40')),
            P(''),
            TR('', INPUT(_type='submit', _value='OK'))
           ))

#get the names of the selected athletes
def getAthleteNames(names):
    #athlete list
    athletes = []
    for key in names:
        if names[key] == 'on':
            athletes.append(key)
    return athletes

#get the selected age group (common, m35, m40)
def getAgeSelection(names):
    return names['ageSelect']

#initialize calculated points dictionary
def initCalculatedPoints(athletes):
    zeroList = [0] * len(athletes)
    return {'aidat': zeroList, 'pituus': zeroList, 'kuula': zeroList, 'satanen': zeroList, 'seivas': zeroList,
            'neljasataa': zeroList, 'korkeus': zeroList, 'kiekko': zeroList, 'keihas': zeroList,
            'tuhatviisisataa': zeroList}

#initialize event results dictionay
def initEventResults(athletes):
    noneList = [None] * len(athletes)
    return {'aidat': noneList, 'pituus': noneList, 'kuula': noneList, 'satanen': noneList,
            'seivas': noneList, 'neljasataa': noneList, 'korkeus': noneList, 'kiekko': noneList, 'keihas': noneList,
            'tuhatviisisataa': noneList}

#insert athlete records into database and return index
def writeAthleteData(athletes, year):
    db = current.db
    athleteId = [0] * len(athletes)
    for idx, athlete in enumerate(athletes):
        query = db((db.athlete.year == year) & (db.athlete.name == athlete.strip()))
        rows = query.select()
        #no write if data allready available
        if rows.__len__() == 0:
            athleteId[idx] = db.athlete.insert(year=year, name=athlete.strip())
        else:
            athleteId[idx] = rows[0].id
    return athleteId
    
