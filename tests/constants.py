# -*- coding: utf-8 -*-
__author__ = 'teros'

URL = 'http://127.0.0.1:8000/kymppilaskuri/default/login'
VALID_USERNAME = 'demo'
VALID_PASSWD = 'test'
INVALID_USERNAME = 'user'
INVALID_PASSWD = 'passwd'
MAIN_PAGE_TITLE = 'Kymppilaskuri'
LOGIN_PAGE_TITLE = 'Login'
WAIT_TIME_IN_SECONDS = 0.5
SPORT_EVENTS = ['110m-aidat', 'Pituus', 'Kuula', '100m', 'Seiväs', '400m', 'Korkeus', 'Kiekko', 'Keihas', '1500m']
SPORT_RESULTS = [15, 6, 10.5, 12.5, 3.5, 55.5, 1.8, 30.5, 45, 300]
SPORT_POINTS = ['850', '617', '516', '551', '502', '562', '662', '475', '538', '553']
#page texts and attributes
ATHLETE_NAME_TEXT = 'Antti Puhakka'
VALUE_ATTRIBUTE = 'value'
COMPOUND_TEXT = 'Yhteistulos'
COMPOUND_YEAR = '2014'
COMPOUND_RESULT = '5819'
AAM_TEXT = 'AAM'
AAM_YEAR = '2014'
AAM_RESULT = '22406'

#page elements
USERNAME = 'username'
PASSWORD = 'password'
OK_BUTTON_LOGIN = "//input[@type='submit']"
OK_BUTTON_COUNTER = "//input[@type='submit']"
ATHLETE_NAME_COUNTER = "//input[@name='Antti Puhakka']"
AGE_SELECT_COUNTER = "//input[@value='m35']"
INPUT_FORM_COMPOUND = '//div[2]/div/form/p/input'
SEL_COMPOUND = '//div[2]/div/form/p[2]/input'
OK_BUTTON_COMPOUND = '//div[2]/div/form/p[3]/input'
INPUT_FORM_AAM = '//div[3]/div/form/p/input'
SEL_AAM = '//div[3]/div/form/p[2]/input'
OK_BUTTON_AAM = '//div[3]/div/form/p[3]/input'
INPUT_FORM_OTHER = '//div/div/form/p/input'
OK_BUTTON_OTHER = '//div/form/p[2]/input'

#/html/body/div/div[2]/div[2]/div/div[3]/div/form/p[3]/input

#//div[3]/div/form/p[2]/input

#/html/body/div/div[2]/div[2]/div/div[3]/div/form/p/input

#/html/body/div/div[2]/div[2]/div/div[4]/div/div/div/div/div/form/p/input

#DRIVER = webdriver.Firefox()
#event link texts

#/html/body/div/div[2]/div[2]/div/div[3]/div/form/p/input
#/html/body/div/div[2]/div[2]/div/div[3]/div/form/p[2]/input
#/html/body/div/div[2]/div[2]/div/div[3]/div/form/p[3]/input
#/html/body/div/div[2]/div[2]/div/div[4]/div/div/div/div/div/form/p/input
#/html/body/div/div[2]/div[2]/div/div[4]/div/div/div/div/div/form/p[2]/input