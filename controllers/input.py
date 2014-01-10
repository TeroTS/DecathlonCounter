# -*- coding: utf-8 -*- 
from datetime import date
from pylab import *
import input
import counter
import compound
import aam
import results
import records
import figures

################################################################
#this is the main controller function
################################################################
def osallistujat2():
    if session.logged_in_user:

        ############################################
        #Checkbox form to input athletes (Laskuri)
        ############################################
        #set the year
        yearNow = date.today().year
        #form including all the athletes' names and age group selection
        athletesInputForm = input.athletesForm()
        #if succesful form validation: Get names of the athletes, get age selection, db insert athlete year and name
        if athletesInputForm.process(formname="form10", keepvalues=True).accepted:
            #selected athletes list
            session.athletes = input.getAthleteNames(athletesInputForm.vars)
            #age selection string
            session.ageSelect = input.getAgeSelection(athletesInputForm.vars)
            #initialize calculated points dictionary
            session.points = input.initCalculatedPoints(session.athletes)
            #initialize event results dictionary
            session.results = input.initEventResults(session.athletes)
            #write database athlete records and return indexes
            session.id = input.writeAthleteData(session.athletes, yearNow)

        #######################################################################################
        #input forms for sport event results and calculated points (Laskuri)
        ########################################################################################
        #event object list, event object includes event name, low and high border values for validation and
        #event selection (track or field event)
        events = counter.createEvents()
        #create input forms
        eventForm = []
        for idx, event in enumerate(events):
            #create form
            eventForm.append(counter.generateEventForm(session.athletes, event, session.results, session.points))
            #if succesful form validation: Calculate points and write sport record
            if eventForm[idx].process(formname="form%d"%idx, keepvalues=True).accepted:
                eventName = events[idx].name
                session.results[eventName], session.points[eventName] = counter.writeSportsData(session.athletes, session.ageSelect, eventName, eventForm[idx], events[idx].sel, session.id)
                #redirect to the same page to show the calculated points
                redirect(URL('input', 'osallistujat2'))
        ###############################################################################
        #compound points form (yhteistulos)
        ###############################################################################         
        compoundForm = compound.compoundForm()
        session.rowsOverall = []
        #if succesful form validation: calculate overall points
        if compoundForm.process(formname='form11', keepvalues=True).accepted:
            session.rowsOverall = compound.getCompoundResults(compoundForm)

        ###############################################################################
        #AAM points form (AAM)
        ###############################################################################         
        aamForm = aam.aamForm()
        session.rowsAam = []
        #if succesful form validation: calculate AAM points
        if aamForm.process(formname='form12', keepvalues=True).accepted:
            session.rowsAam = aam.getAamResults(aamForm)

        ##########################################################################################
        #this form includes all the results from a single year (muut tulokset - vanhat tulokset)
        ##########################################################################################         
        oldResultsForm = results.oldResultsForm()
        session.oldNames = []
        session.oldAidat = []
        session.oldPituus = []
        session.oldKuula = []
        session.oldSatanen = []
        session.oldSeivas = []
        session.oldNeljasataa = []
        session.oldKorkeus = []
        session.oldKiekko = []
        session.oldKeihas = []
        session.oldTuhatviisisataa = []
        #if succesful form validation: Print all results from a single year
        if oldResultsForm.process(formname='form13', keepvalues=True).accepted:
            oldResults = results.getOldResults(oldResultsForm)
            session.oldNames = oldResults['names']
            session.oldAidat = oldResults['aidat']
            session.oldPituus = oldResults['pituus']
            session.oldKuula = oldResults['kuula']
            session.oldSatanen = oldResults['satanen']
            session.oldSeivas = oldResults['seivas']
            session.oldNeljasataa = oldResults['neljasataa']
            session.oldKorkeus = oldResults['korkeus']
            session.oldKiekko = oldResults['kiekko']
            session.oldKeihas = oldResults['keihas']
            session.oldTuhatviisisataa = oldResults['tuhatviisisataa']

        ##########################################################################################
        #records are printed here (Muut Tulokset - Ennätykset)
        ##########################################################################################                                 
        session.recordAidat = records.getTrackEventRecord('aidat')
        session.nameAidat = records.getRecordNameAndYear(session.recordAidat.athlete_id)
        session.recordPituus = records.getFieldEventRecord('pituus')
        session.namePituus = records.getRecordNameAndYear(session.recordPituus.athlete_id)
        session.recordKuula = records.getFieldEventRecord('kuula')
        session.nameKuula = records.getRecordNameAndYear(session.recordKuula.athlete_id)
        session.recordSatanen = records.getTrackEventRecord('satanen')
        session.nameSatanen = records.getRecordNameAndYear(session.recordSatanen.athlete_id)
        session.recordSeivas = records.getFieldEventRecord('seivas')
        session.nameSeivas = records.getRecordNameAndYear(session.recordSeivas.athlete_id)
        session.recordNeljasataa = records.getTrackEventRecord('neljasataa')
        session.nameNeljasataa = records.getRecordNameAndYear(session.recordNeljasataa.athlete_id)
        session.recordKorkeus = records.getFieldEventRecord('korkeus')
        session.nameKorkeus = records.getRecordNameAndYear(session.recordKorkeus.athlete_id)
        session.recordKiekko = records.getFieldEventRecord('kiekko')
        session.nameKiekko = records.getRecordNameAndYear(session.recordKiekko.athlete_id)
        session.recordKeihas = records.getFieldEventRecord('keihas')
        session.nameKeihas = records.getRecordNameAndYear(session.recordKeihas.athlete_id)
        session.recordTuhatviisisataa = records.getTrackEventRecord('tuhatviisisataa')
        session.nameTuhatviisisataa = records.getRecordNameAndYear(session.recordTuhatviisisataa.athlete_id)
        ############################################################
        #figure plot controller (Muut Tulokset - Trendit)
        ############################################################
        figuresForm = figures.figuresForm()
        #get all years
        yearRows = db().select(db.athlete.year, distinct=True)
        #initialize data lists
        session.xData = [None] * yearRows.__len__()
        session.figureName = ''
        session.scoreResult = [0] * yearRows.__len__()
        session.aamResult = [0] * yearRows.__len__()
        session.aidatResult = [0] * yearRows.__len__()
        session.pituusResult = [0] * yearRows.__len__()
        session.kuulaResult = [0] * yearRows.__len__()
        session.satanenResult = [0] * yearRows.__len__()
        session.seivasResult = [0] * yearRows.__len__()
        session.neljasataaResult = [0] * yearRows.__len__()
        session.korkeusResult = [0] * yearRows.__len__()
        session.kiekkoResult = [0] * yearRows.__len__()
        session.keihasResult = [0] * yearRows.__len__()
        session.tuhatviisisataaResult = [0] * yearRows.__len__()
        #if succesful form validation: Create data for images
        if figuresForm.process(formname="form14", keepvalues=True).accepted:
            #all event data (x- and y-axis data for images)
            eventData = figures.getEventData(figuresForm, yearRows)
            plot('Yhteistulos', 'AAM', '110m-aidat', 'Pituus', figures.X_TITLE, figures.Y_TITLE, eventData['xData'], eventData['scoreResult'],
                 eventData['aamResult'], eventData['aidatResult'], eventData['pituusResult'], figures.FIGURE_INDEX_0)
            plot('satanen', 'Kuula', 'Seivas', '400m', figures.X_TITLE, figures.Y_TITLE, eventData['xData'], eventData['satanenResult'],
                 eventData['kuulaResult'], eventData['seivasResult'], eventData['neljasataaResult'], figures.FIGURE_INDEX_1)
            plot('Korkeus', 'Kiekko', 'Keihas', '1500m', figures.X_TITLE, figures.Y_TITLE, eventData['xData'], eventData['korkeusResult'],
                 eventData['kiekkoResult'], eventData['keihasResult'], eventData['tuhatviisisataaResult'], figures.FIGURE_INDEX_2)

        ######################                                               
        #send forms to view
        ######################
        return dict(athletesInputForm=athletesInputForm,
                    compoundForm=compoundForm,
                    aamForm=aamForm,
                    oldResultsForm=oldResultsForm,
                    figuresForm=figuresForm,
                    eventForm = eventForm)

    else:
        redirect(URL('default', 'login'))
    
