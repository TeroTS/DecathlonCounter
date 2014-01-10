# -*- coding: utf-8 -*-
__author__ = 'teros'

from gluon import *

#low and high border values for events
LOW_110_AIDAT = 10
HIGH_110_AIDAT = 30
LOW_PITUUS = 2
HIGH_PITUUS = 9
LOW_KUULA = 5
HIGH_KUULA = 20
LOW_100M = 9
HIGH_100M = 20
LOW_KORKEUS = 1
HIGH_KORKEUS = 2.5
LOW_400M = 40
HIGH_400M = 80
LOW_SEIVAS = 1
HIGH_SEIVAS = 6
LOW_KIEKKO = 10
HIGH_KIEKKO = 70
LOW_KEIHAS = 15
HIGH_KEIHAS = 80
LOW_1500M = 180
HIGH_1500M = 480

#event names including all decathlon events
eventName = ['aidat', 'pituus', 'kuula', 'satanen', 'seivas', 'neljasataa', 'korkeus', 'kiekko', 'keihas', 'tuhatviisisataa']
#event low and high lists for validation
eventLow = [LOW_110_AIDAT, LOW_PITUUS, LOW_KUULA, LOW_100M, LOW_KORKEUS, LOW_400M, LOW_SEIVAS, LOW_KIEKKO, LOW_KEIHAS, LOW_1500M]
eventHigh = [HIGH_110_AIDAT, HIGH_PITUUS, HIGH_KUULA, HIGH_100M, HIGH_KORKEUS, HIGH_400M, HIGH_SEIVAS, HIGH_KIEKKO, HIGH_KEIHAS, HIGH_1500M]
#event selection list
eventSel = ['track', 'field', 'field', 'track', 'field', 'track', 'field', 'field', 'field', 'track']

#sport class: name of the event, range of valid result values and selector to select is the event track or field event
#Created to make method interfaces more compact (=less parameters)
class sport:
    def __init__(self, name, low, high, sel):
        self.name = name
        self.low = low
        self.high = high
        self.sel = sel

#create event object list
def createEvents():
    events = []
    for idx, name in enumerate(eventName):
        events.append(sport(name, eventLow[idx], eventHigh[idx], eventSel[idx]))
    return events

#coefficients to calculate points using the formulas from: http://netisto.fi/ottelu/kaavat.htm
dictCoeffA = {'satanen': 25.4348, 'pituus': 90.5674, 'kuula': 51.39, 'korkeus': 585.65, 'neljasataa': 1.53775,
            'aidat': 5.74354, 'kiekko': 12.91, 'seivas': 140.1820, 'keihas': 10.14, 'tuhatviisisataa': 0.03768}
dictCoeffB = {'satanen': 18, 'pituus': 2.2, 'kuula': 1.5, 'korkeus': 0.75, 'neljasataa': 82,
            'aidat': 28.5, 'kiekko': 4, 'seivas': 1, 'keihas': 7, 'tuhatviisisataa': 480}
dictCoeffC = {'satanen': 1.81, 'pituus': 1.4, 'kuula': 1.05, 'korkeus': 1.42, 'neljasataa': 1.81,
            'aidat': 1.92, 'kiekko': 1.1, 'seivas': 1.35, 'keihas': 1.08, 'tuhatviisisataa': 1.85}
dictCoeffM35 = {'satanen': 0.9893, 'pituus': 1.0510, 'kuula': 1.0, 'korkeus': 1.0546, 'neljasataa': 0.9702,
            'aidat': 0.9999, 'kiekko': 1.0, 'seivas': 1.0390, 'keihas': 1.0434, 'tuhatviisisataa': 0.9872}
dictCoeffM40 = {'satanen': 0.9545, 'pituus': 1.1112, 'kuula': 1.0271, 'korkeus': 1.1059, 'neljasataa': 0.9350,
            'aidat': 0.9562, 'kiekko': 1.0, 'seivas': 1.1046, 'keihas': 1.1283, 'tuhatviisisataa': 0.9387}

#track events: P = A*(result-B)**C
def calcTrackEventPoints(event, result):
    points = dictCoeffA[event]*pow((dictCoeffB[event] - result), dictCoeffC[event])
    return points

#field events: P = A*(B-result)**C
def calcFieldEventPoints(event, result):
    points = dictCoeffA[event]*pow((result - dictCoeffB[event]), dictCoeffC[event])
    return points

#calculate points from the results
def calculatePoints(form, sport, eventSel, idx1):
    if eventSel == 'track':
        return calcTrackEventPoints(sport, float(form.vars["name%d"%idx1]))
    else:
        return calcFieldEventPoints(sport, float(form.vars["name%d"%idx1]))

#Form fuction, returns a form helper takes low and high border values,
#athlete index (used to name the form) and name as parameters
def form(low, high, idx, athleteName, points, result):
    errorMessage = 'Syota numero %d'%low + ' ja ' + '%d'%high + ' valilla !'
    return FORM(TABLE(TR(athleteName, INPUT(_type='decimal', _name="name%d"%idx, _value=result, requires=[IS_NOT_EMPTY("Tyhja lomake !"), IS_DECIMAL_IN_RANGE(low, high, error_message=errorMessage, dot=",")]), INPUT(_type='decimal', _value=int(round(points)), _name="points%d"%idx, _readonly=ON))))

#single form row
def element(low, high, idx, athleteName, points, result):
    errorMessage = 'Syota numero %d'%low + ' ja ' + '%d'%high + ' valilla !'
    return TR(athleteName, INPUT(_type="decimal", _name="name%d"%idx, _value=result, requires=[IS_NOT_EMPTY("Tyhja lomake !"), IS_DECIMAL_IN_RANGE(low, high, error_message=errorMessage, dot=",")]), INPUT(_type='decimal', _value=int(round(points)), _name="points%d"%idx, _readonly=ON))

#generate result and calculated points form
def generateEventForm(athletes, sport, results, points):
    formEvent = FORM()
    #dynamic generation of the forms
    for idx1, athlete in enumerate(athletes):
        #initialize form
        if idx1 == 0:
            formEvent = form(sport.low, sport.high, idx1, athlete, points[sport.name][idx1], results[sport.name][idx1])
        #add elements (=rows) to form
        else:
            elementEvent = element(sport.low, sport.high, idx1, athlete, points[sport.name][idx1], results[sport.name][idx1])
            formEvent[0].append(elementEvent)
    #print button only if athletes number > 0
    if athletes:
        submit = TR("", INPUT(_type="submit", _value="OK"))
        formEvent[0].append(submit)
    return formEvent

def calculateEventPoints(ageSelect, eventForm, eventName, eventSel, index):
    #calculate points from given data for each athlete
    if ageSelect == 'm35':
        eventPoints = dictCoeffM35[eventName] * calculatePoints(eventForm, eventName, eventSel, index)
    elif ageSelect == 'm40':
        eventPoints = dictCoeffM40[eventName] * calculatePoints(eventForm, eventName, eventSel, index)
    else:
        eventPoints = calculatePoints(eventForm, eventName, eventSel, index)
    return eventPoints

#write database sport records
def writeSportsData(athletes, ageSelect, eventName, eventForm, eventSel, athleteId):
    db = current.db
    #list that includes results for all athletes
    athleteResults = []
    #list that includes calculated points for all athletes
    eventPoints = []
    #calculate points and write database
    for idx1, athlete in enumerate(athletes):
        calculatedPoints = calculateEventPoints(ageSelect, eventForm, eventName, eventSel, idx1)
        #add calculated points to list, this is returned to view
        eventPoints.append(calculatedPoints)
        #add results to list, this is used to keep result value in form when redirected
        athleteResults.append(eventForm.vars["name%d" % idx1])
        #write or update sport record
        db.sport.update_or_insert(
            (db.sport.athlete_id == athleteId[idx1]) & (db.sport.name == eventName),
            athlete_id=athleteId[idx1],
            name=eventName,
            result=eventForm.vars["name%d" % idx1],
            points=eventPoints[idx1]
        )
    #return results and calculated points
    return (athleteResults, eventPoints)
