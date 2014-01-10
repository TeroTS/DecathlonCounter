# -*- coding: utf-8 -*-
__author__ = 'teros'

from gluon import *
import matplotlib.pyplot as plt

#figure plot numbers
FIGURE_INDEX_0 = 0
FIGURE_INDEX_1 = 0
FIGURE_INDEX_2 = 0

X_TITLE = 'vuosi'
Y_TITLE = 'pisteet'

def figuresForm():
    return FORM(TABLE(TR(INPUT(_type='radio', _name='nameSel', _value='Antti Puhakka'), 'Antti Puhakka',
                         INPUT(_type='radio', _name='nameSel', _value='Antti Sepponen'), 'Antti Sepponen',
                         INPUT(_type='radio', _name='nameSel', _value='Esa Mikkonen'), 'Esa Mikkonen'),
                      TR(INPUT(_type='radio', _name='nameSel', _value='Harri Muikku'), 'Harri Muikku',
                         INPUT(_type='radio', _name='nameSel', _value='Jan Kiljunen'), 'Jan Kiljunen',
                         INPUT(_type='radio', _name='nameSel', _value='Jani Taivalantti'), 'Jani Taivalantti'),
                      TR(INPUT(_type='radio', _name='nameSel', _value='Jari Kurvinen'), 'Jari Kurvinen',
                         INPUT(_type='radio', _name='nameSel', _value='Jari Rantalainen'), 'Jari Rantalainen',
                         INPUT(_type='radio', _name='nameSel', _value='Jarmo Marttinen'), 'Jarmo Marttinen'),
                      TR(INPUT(_type='radio', _name='nameSel', _value='Panu Tuomikko'), 'Panu Tuomikko',
                         INPUT(_type='radio', _name='nameSel', _value='Pauli Kartano'), 'Pauli Kartano',
                         INPUT(_type='radio', _name='nameSel', _value='Pekka Miettinen'), 'Pekka Miettinen'),
                      TR(INPUT(_type='radio', _name='nameSel', _value='Sami Vesalainen'), 'Sami Vesalainen',
                         INPUT(_type='radio', _name='nameSel', _value='Teemu Tiusanen'), 'Teemu Tiusanen',
                         INPUT(_type='radio', _name='nameSel', _value='Tero Suhonen'), 'Tero Suhonen',
                         INPUT(_type='radio', _name='nameSel', _value='Ville Syrjalainen'), 'Ville Syrjäläinen'),
                         P('')),
                         INPUT(_type="submit", _value="OK"))

#generate data for trend images
#data includes: Compound points, aam points and event points for selected athlete
#this is bad !!! too much looping !!! fix later !!!!
def getEventData(form, years):
    db = current.db
    #name selection variable
    names = form.vars
    figureName = names['nameSel']
    xData = []
    aamResult = []
    scoreResult = []
    aidatResult = []
    pituusResult = []
    kuulaResult = []
    satanenResult = []
    seivasResult = []
    neljasataaResult = []
    korkeusResult = []
    kiekkoResult = []
    keihasResult = []
    tuhatviisisataaResult = []
    #loop through all years
    for row in years:
        #set x-axis data (years)
        xData.append(row.year)
        #tmp = session.figureName
        yearQuery = (db.athlete.year == row.year)
        #get the last aam result for the athlete (not necessarily current year)
        tmpRow = db((db.athlete.name == figureName) & (db.athlete.year <= row.year)).select(db.athlete.aam).last()
        if tmpRow:
            aamResult.append(tmpRow.aam)
            #loop through all the athletes in a given year
        for athlete in db(yearQuery).select():
            #if athlete name selected, get compound result AAM result and
            #sport results for selected athlete
            if athlete.name == figureName:
                scoreResult.append(athlete.score)
                #loop through all sport results
                for sport in athlete.sport.select():
                    if sport.name == 'aidat':
                        aidatResult.append(sport.points)
                    if sport.name == 'pituus':
                        pituusResult.append(sport.points)
                    if sport.name == 'kuula':
                        kuulaResult.append(sport.points)
                    if sport.name == 'satanen':
                        satanenResult.append(sport.points)
                    if sport.name == 'seivas':
                        seivasResult.append(sport.points)
                    if sport.name == 'neljasataa':
                        neljasataaResult.append(sport.points)
                    if sport.name == 'korkeus':
                        korkeusResult.append(sport.points)
                    if sport.name == 'kiekko':
                        kiekkoResult.append(sport.points)
                    if sport.name == 'keihas':
                        keihasResult.append(sport.points)
                    if sport.name == 'tuhatviisisataa':
                        tuhatviisisataaResult.append(sport.points)
    return {'athleteName':figureName, 'xData':xData, 'aamResult':aamResult, 'scoreResult':scoreResult,
            'aidatResult':aidatResult, 'pituusResult':pituusResult, 'kuulaResult':kuulaResult, 'satanenResult':satanenResult,
            'seivasResult':seivasResult, 'neljasataaResult':neljasataaResult, 'korkeusResult':korkeusResult, 'kiekkoResult':kiekkoResult,
            'tuhatviisisataaResult':tuhatviisisataaResult}

#figure plotting fuctions
def setPlot(ax, title, xlab, ylab, dataX, dataY):
    if title:
        ax.set_title(title)
    if xlab:
        ax.set_xlabel(xlab)
    if ylab:
        ax.set_ylabel(ylab)
    ax.plot(dataX, dataY)

def plot(title0, title1, title2, title3,
         xlab, ylab, dataX,
         dataY0, dataY1, dataY2, dataY3, index):
    fig = plt.figure()
    fig.set_facecolor('white')
    fig.subplots_adjust(wspace=0.5, hspace=0.75)
    ax0 = fig.add_subplot(2, 2, 1)
    ax1 = fig.add_subplot(2, 2, 2)
    ax2 = fig.add_subplot(2, 2, 3)
    ax3 = fig.add_subplot(2, 2, 4)
    setPlot(ax0, title0, xlab, ylab, dataX, dataY0)
    setPlot(ax1, title1, xlab, ylab, dataX, dataY1)
    setPlot(ax2, title2, xlab, ylab, dataX, dataY2)
    setPlot(ax3, title3, xlab, ylab, dataX, dataY3)
    fig.savefig('applications/kymppilaskuri/static/images/graph_%d.png' % index)

