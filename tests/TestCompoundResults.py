# -*- coding: utf-8 -*-
__author__ = 'teros'

import unittest
from helpers import *
from constants import *

class TestCompoundResults(unittest.TestCase):

    def setUp(self):
        self.display = startVirtualDisplay()
        self.browser = doLogin(URL, VALID_USERNAME, VALID_PASSWD)

    def testResults(self):
        driver = self.browser
        #click compound result tab
        compoundTab = driver.find_element_by_link_text(COMPOUND_TEXT)
        compoundTab.click()
        #find year input form
        yearForm = driver.find_element_by_xpath(INPUT_FORM_COMPOUND)
        yearForm.send_keys(COMPOUND_YEAR)
        #select count points
        countCheckbox = driver.find_element_by_xpath(SEL_COMPOUND)
        countCheckbox.click()
        clickOkButton(driver, OK_BUTTON_COMPOUND)
        #verify calculated points
        textFound = findTextOnPage(driver, COMPOUND_RESULT)
        self.assertNotEqual(textFound, None)

    def tearDown(self):
        self.browser.quit()
        stopVirtualDisplay(self.display)
