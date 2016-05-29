# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re

class ALinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://deanza.edu/"
        self.verificationErrors = []
    
    def test_a_links(self):
        link_title = {
            "Library/De Hart Learning Center" : "De Anza College :: Library :: Home",
            "Library West Computer Lab" : "De Anza College :: Library :: Library West Computer Lab",
            "Listening and Speaking Center" : "De Anza College :: Listening and Speaking Center (LSC) :: Home",
            "Mandarin Department" : "De Anza College :: Mandarin :: Home",
            "Manufacturing & CNC Technology" : "De Anza College Manufacturing/CNC Department",
            "Map" : "De Anza College :: Campus Map :: Home",
            "Office of Communications" : "De Anza College :: Office of Communications :: Home",
            "Journalism and Mass Communication" : "De Anza College :: Journalism and Mass Communication :: Home",	 
 	 }
        
        driver = self.driver
        driver.get(self.base_url + "directory/dir-az.html")

        for link in link_title:
            title = link_title[link]
            driver.find_element_by_link_text(link).click()
            try: self.assertEqual(title, driver.title)
            except AssertionError as e: self.verificationErrors.append(str(e))
            driver.back()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
