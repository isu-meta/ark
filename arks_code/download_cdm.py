import re
import os
import shutil
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DownloadXML():
    '''
        Logs into contentDM with selenium, and exports selected collection
    '''

    def setup(self, filepath):
        """
            Sets up selenium webdriver, and sets options
            Inputs include desired directory filepath.
        """
        self.filepath = filepath
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
            "download.default_directory": filepath,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        self.driver = webdriver.Chrome(executable_path=r'D:/Users/rwolfsla/Desktop/sphinx_docs/project_code/chromedriver',
                                       chrome_options=options)

        self.driver.get(
            'https://server16001.contentdm.oclc.org/cgi-bin/admin/start.exe')
        self.driver.implicitly_wait(3)

        collections_tab = self.driver.find_element(
            By.XPATH, "//a[@id='acolls' and @title='collections']")
        collections_tab.click()

        self.driver.implicitly_wait(10)

    def select_and_export(self, collection_number):
        '''
            Selects and Export by collection number
        '''
        element = self.driver.find_element(
            By.XPATH, '//select[@name="CISODB"]')
        sel = Select(element)
        sel.select_by_value('/{}'.format(collection_number.replace('/', '')))
        self.driver.find_element(
            By.XPATH, '//input[@type="submit" and @value="change"]').click()
        time.sleep(0.5)
        export_tab = self.driver.find_element(By.XPATH,
                                              '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody/tr[2]/td/span/a[5]')
        export_tab.click()

        dcxpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody/tr[2]/td/table/tbody/tr[5]/td/span/input'
        dublin_core = self.driver.find_element(By.XPATH, dcxpath)

        dublin_core.click()

        # go to export page
        self.driver.find_element(By.XPATH, '//*[@id="subbut"]').click()


        exportxpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/span/a'
        export_link = self.driver.find_element(By.XPATH, exportxpath)

        filexpath = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/span/a'
        g = self.driver.find_element(By.XPATH, filexpath)
        url = g.get_attribute('href')

        self.driver.get(url)
        self.driver.get(
            'https://server16001.contentdm.oclc.org/cgi-bin/admin/start.exe')
        self.driver.implicitly_wait(3)

        collections_tab = self.driver.find_element(
            By.XPATH, "//a[@id='acolls' and @title='collections']")
        collections_tab.click()

        
def cdm_collections():
    collections = [
    "/p16001coll16",
    "/p16001coll13",
    "/p16001coll3",
    "/p15031coll11",
    "/p16001coll1",
    "/p15031coll20",
    "/p15031coll9",
    "/p15031coll5",
    "/p16001coll7",
    "/p16001coll26",
    "/p15031coll12",
    "/p15031coll14",
    "/p16001coll28",
    "/p16001coll27",
    "/p15031coll26",
    "/p16001coll18",
    "/p15031coll22",
    "/p15031coll3",
    "/p15031coll10",
    "/p16001coll10",
    "/p15031coll7",
    "/p16001coll5",
    "/p15031coll6",
    "/p16001coll15",
    "/p16001coll2",
    "/p16001coll29",
    "/p16001coll30",
    "/p16001coll21",
    "/p16001coll22",
    "/p15031coll18",
    "/p15031coll24",
    "/p16001coll17",
    "/p16001coll8",
    "/p16001coll14",
    "/p15031coll19",
    "/p16001coll6",
    "/p16001coll11",
    "/p15031coll21",
    "/p16001coll9",
    "/p16001coll12",
    "/p15031coll15",
    "/p15031coll17",
    "/p15031coll16",
    "/p16001coll4",
    "/p16001coll19",
    "/p16001coll32",
    "/p16001coll33",
    "/p16001coll34",
    "/p16001coll36",
    "/p16001coll20",
    "/p16001coll23",
    "/p16001coll24",
    "/p16001coll25",
    "/p16001coll31",
    "/p16001coll35",
    "/p16001coll37",
    "/p16001coll38",
    "/p16001coll39",
    "/p16001coll40",
    "/p16001coll41",
    "/p16001coll42",
    "/p16001coll43",
    "/p16001coll44",
    "/p16001coll45",
    "/p16001coll46",
    "/p16001coll47",
    ]
    return collections
