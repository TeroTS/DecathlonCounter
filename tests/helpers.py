# -*- coding: utf-8 -*-
__author__ = 'teros'

from selenium import webdriver
import re
import time
from constants import *
from pyvirtualdisplay import Display

def startVirtualDisplay():
    display = Display(visible=0, size=(800, 600))
    display.start()
    return display

def stopVirtualDisplay(display):
    display.stop()

def waitFor(seconds):
    time.sleep(seconds)

def clickOkButton(browser, okButtonElement):
    okButton = browser.find_element_by_xpath(okButtonElement)
    okButton.click()
    waitFor(WAIT_TIME_IN_SECONDS)
    #return browser

def doLogin(url, username, password):
    browser = getUrl(url)
    #input username and password
    usernameElement = browser.find_element_by_name(USERNAME)
    usernameElement.send_keys(username)
    passwordElement = browser.find_element_by_name(PASSWORD)
    passwordElement.send_keys(password)
    clickOkButton(browser, OK_BUTTON_LOGIN)
    return browser

def findTextOnPage(driver, stringToSearch):
    src = driver.page_source
    return re.search(stringToSearch, src)

def getUrl(url):
    browser = webdriver.Firefox()
    browser.get(url)
    waitFor(WAIT_TIME_IN_SECONDS)
    return browser

def getResultsElement(idx):
    return "//div[%d]/form/table/tbody/tr/td[2]/input"%(idx+2)

def getOkButtonElement(idx):
    return '//div[%d]/form/table/tbody/tr[2]/td[2]/input'%(idx+2)

def getPointsElement(idx):
    return "//div[%d]/form/table/tbody/tr/td[3]/input"%(idx+2)