#!/usr/bin/env/scraper_env
# -*- coding: utf-8 -*-

# Coder: David Yen-Chieh Liao

import re
import time
import random
from termcolor import colored
import pandas as pd
import numpy as np
import itertools
from tika import parser
import emoji # pip install emoji

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized") #open Browser in maximized mode
options.add_argument("--no-sandbox") # bypass OS security model
options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

def speeches_scraper():
    start_page =int(input("Start Page (default, 1):") )
    end_page =int(input("End Page (minimum: 2, maximum: 1680):"))
    appended_content = []
    appended_links = []
    appended_webindex = []
    for page in range(start_page, end_page, 1):
        try:
            driver = webdriver.Chrome("/Users/yenchiehliao/Dropbox/Nicole's Project/webscrape/chromedriver")
            #driver = webdriver.Chrome(ChromeDriverManager().install()) # activate chrome webdriver
            driver.implicitly_wait(60)
            driver.get('https://www.bis.org/cbspeeches/')
            dest_search = driver.find_element_by_xpath("""//*[@id="cbspeeches_list"]/div/div[2]/nav/div/div[2]/div/div[4]/input""")
            dest_search.clear()
            dest_search.send_keys(page)
            dest_search.send_keys(Keys.ENTER)
            time.sleep(random.uniform(1, 2))  # 隨機停頓模擬人的行為
            # get content
            num_rows = len(driver.find_elements_by_xpath("""//*[@id="cbspeeches_list"]/div/table/tbody/tr"""))         # counting the number of rows
            for i in range(num_rows):                                                                                  # for loop the table based on  the number of rows
                #time.sleep(random.uniform(2, 3)) # randomly sleep
                num_rows = len(driver.find_elements_by_xpath("""//*[@id="cbspeeches_list"]/div/table/tbody/tr"""))     # counting the number of rows
                content = driver.find_elements_by_xpath("""//*[@id="cbspeeches_list"]/div/table/tbody/tr""")[i].text   # get link
                link = driver.find_elements_by_xpath("""//*[@id="cbspeeches_list"]/div/table/tbody/tr/td/div/a""")     # get title the number of rows
                appended_content.append(content)
                appended_links.append(link[i].get_attribute("href"))
            #time.sleep(random.uniform(0, 2)) # randomly sleep
            driver.close()
            # get web page index as list
            appended_webindex.append([page]*num_rows)
            print(colored(page, "green"), colored("of 1,679 Pages", "green"), colored("is Perfectly Webscraped!!", "green"), emoji.emojize(':thumbs_up:'))
        except exceptions.StaleElementReferenceException as e:
            print(colored("Something else went wrong with that page", "red", attrs=['bold']), colored(page, "red", attrs=['bold']), emoji.emojize(':bug: :'), e, colored("StaleElementReferenceException", "grey", attrs=['bold']))
            pass
        except (NoSuchWindowException, NoSuchElementException) as e:
            print(colored("Something else wen wrong with that page", "red", attrs=['bold']), colored(page, "red", attrs=['bold']), emoji.emojize(':beetle: :') ,e , colored("Due to NoSuchWindowException or NoSuchElementException", "grey", attrs=['bold']))
            pass
        except (AttributeError, IndexError) as e:
            print(colored("Something else went wrong with that page, again", "red", attrs=['bold']), colored(page, "red", attrs=['bold']), emoji.emojize(':spider: :') ,e , colored("Due to AttributeError", "grey", attrs=['bold']))
            pass


def format_dataframe():

    soup = BeautifulSoup(html, 'html.parser')
    results = {}
    for field in FIELDS:
        results[field] = soup.find('table').find('tr', id='places_{}__row'.format(field)).find('td', class_='w2p_fw').text
    return results

def main():
    speeches_scraper()



if __name__ == '__main__':
    main()
