import os
import re
import shutil
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select


class DownloadXML:
    """
        Logs into contentDM with selenium, and exports selected collection
    """

    def setup(self, filepath, driver_path):
        """
            Sets up selenium webdriver, and sets options
            Inputs include desired directory filepath.
        """
        self.filepath = filepath
        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            "prefs",
            {
                "download.default_directory": filepath,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True,
            },
        )

        self.driver = webdriver.Chrome(
            executable_path=driver_path, chrome_options=options
        )

        self.driver.get(
            "https://server16001.contentdm.oclc.org/cgi-bin/admin/start.exe"
        )
        self.driver.implicitly_wait(3)

        collections_tab = self.driver.find_element_by_xpath(
            "//a[@id='acolls' and @title='collections']"
        )
        collections_tab.click()

        self.driver.implicitly_wait(10)

        self.collections = self.get_cdm_collections()

    def select_and_export(self, collection_number):
        """
            Selects and Export by collection number
        """
        element = self.driver.find_element_by_xpath('//select[@name="CISODB"]')
        sel = Select(element)
        sel.select_by_value("/{}".format(collection_number.replace("/", "")))
        self.driver.find_element_by_xpath(
            '//input[@type="submit" and @value="change"]'
        ).click()
        time.sleep(0.5)
        export_tab = self.driver.find_element_by_xpath(
            "/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody/tr[2]/td/span/a[5]"
        )
        export_tab.click()

        dcxpath = "/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody/tr[2]/td/table/tbody/tr[5]/td/span/input"
        dublin_core = self.driver.find_element_by_xpath(dcxpath)

        dublin_core.click()

        # go to export page
        self.driver.find_element_by_xpath('//*[@id="subbut"]').click()

        exportxpath = "/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/span/a"
        export_link = self.driver.find_element_by_xpath(exportxpath)

        filexpath = "/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/span/a"
        g = self.driver.find_element_by_xpath(filexpath)
        url = g.get_attribute("href")

        self.driver.get(url)
        self.driver.get(
            "https://server16001.contentdm.oclc.org/cgi-bin/admin/start.exe"
        )
        self.driver.implicitly_wait(3)

        collections_tab = self.driver.find_element_by_xpath(
            "//a[@id='acolls' and @title='collections']"
        )
        collections_tab.click()

    def get_cdm_collections(self):
        self.driver.get(
            "https://server16001.contentdm.oclc.org/cgi-bin/admin/collections.exe"
        )

        options = self.driver.find_elements_by_xpath("//select/option")

        collections = [o.get_attribute("value") for o in options]

        return collections
