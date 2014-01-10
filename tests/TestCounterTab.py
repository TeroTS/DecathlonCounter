__author__ = 'teros'

import unittest
from helpers import *
from constants import *

class TestCounterTab(unittest.TestCase):

    def setUp(self):
        self.display = startVirtualDisplay()
        self.browser = doLogin(URL, VALID_USERNAME, VALID_PASSWD)

    #test that all sport tabs have correct data (athlete name and data input form)
    #and events' points calculation logic works
    def testAllSportTabs(self):
        driver = self.browser
        #select athlete and age group
        athleteCheckbox = driver.find_element_by_xpath(ATHLETE_NAME_COUNTER)
        athleteCheckbox.click()
        ageSelection = driver.find_element_by_xpath(AGE_SELECT_COUNTER)
        ageSelection.click()
        clickOkButton(driver, OK_BUTTON_COUNTER)
        for idx, event in enumerate(SPORT_EVENTS):
            #select event tab
            eventTab = driver.find_element_by_link_text(event)
            eventTab.click()
            #input event result and click ok button to calculate the points
            resultForm = driver.find_element_by_xpath(getResultsElement(idx))
            resultForm.send_keys('%f'%SPORT_RESULTS[idx])
            clickOkButton(driver, getOkButtonElement(idx))
            #verify name and calculated points
            textFound = findTextOnPage(driver, ATHLETE_NAME_TEXT)
            self.assertNotEqual(textFound, None)
            pointsForm = driver.find_element_by_xpath(getPointsElement(idx))
            self.assertEqual(str(pointsForm.get_attribute(VALUE_ATTRIBUTE)), SPORT_POINTS[idx])

    def tearDown(self):
        self.browser.quit()
        stopVirtualDisplay(self.display)

if __name__ == '__main__':
    unittest.main()