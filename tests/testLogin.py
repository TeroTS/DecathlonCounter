# -*- coding: utf-8 -*-
__author__ = 'teros'


import unittest
from helpers import *
from constants import *
from pyvirtualdisplay import Display

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()

    def testValidLogin(self):
        self.browser = doLogin(URL, VALID_USERNAME, VALID_PASSWD)
        self.assertEqual(MAIN_PAGE_TITLE, str(self.browser.title))

    def testInvalidLogin(self):
        self.browser = doLogin(URL, INVALID_USERNAME, INVALID_PASSWD)
        self.assertEqual(LOGIN_PAGE_TITLE, str(self.browser.title))

    def tearDown(self):
        self.browser.quit()
        self.display.stop()

if __name__ == '__main__':
    unittest.main()