#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------------------ #
# @author: davidycliao                                                                       #
# @email: davidycliao@gmail.com                                                              #
# @date: 9-May-2021                                                                          #
# @info: An Automation Webcrawler for Extracting Central Bankers' Speeches from BIS Website  #
# ------------------------------------------------------------------------------------------ #


import time
import random
import pandas as pd
import emoji

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized")  # open Browser in maximized mode
options.add_argument("--no-sandbox")  # bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


def scraper():
    start_page = int(input("Start Page (default, 1):"))
    end_page = int(input("End Page (minimum: 2, maximum: 1680):"))
    appended_content = []
    appended_links = []
    appended_webindex = []
    for page in range(start_page, end_page, 1):
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            # driver = webdriver.Chrome(ChromeDriverManager().install()) # activate chrome webdriver
            driver.implicitly_wait(60)
            driver.get('https://www.bis.org/cbspeeches/')
            dest_search = driver.find_element_by_xpath(
                """//*[@id="cbspeeches_list"]/div/div[2]/nav/div/div[2]/div/div[4]/input""")
            dest_search.clear()
            dest_search.send_keys(page)
            dest_search.send_keys(Keys.ENTER)
            time.sleep(random.uniform(1, 2))
            # get content
            num_rows = len(driver.find_elements_by_xpath(
                """//*[@id="cbspeeches_list"]/div/table/tbody/tr"""))  # counting the number of rows
            for i in range(num_rows):  # for loop the table based on  the number of rows
                # time.sleep(random.uniform(2, 3)) # randomly sleep
                num_rows = len(driver.find_elements_by_xpath(
                    """//*[@id="cbspeeches_list"]/div/table/tbody/tr"""))  # counting the number of rows
                content = driver.find_elements_by_xpath("""//*[@id="cbspeeches_list"]/div/table/tbody/tr""")[
                    i].text  # get link
                link = driver.find_elements_by_xpath(
                    """//*[@id="cbspeeches_list"]/div/table/tbody/tr/td/div/a""")  # get title the number of rows
                appended_content.append(content)
                appended_links.append(link[i].get_attribute("href"))
            # time.sleep(random.uniform(0, 2)) # randomly sleep
            driver.close()
            # get web page index as list
            appended_webindex.append([page] * num_rows)
            print(page, " of 1,711  is perfectly scraped!!", emoji.emojize(':thumbs_up:'))
        except exceptions.StaleElementReferenceException as e:
            print("Something else went wrong with that page", page, emoji.emojize(':bug: :'), e,
                  "StaleElementReferenceException")
            pass
        except (NoSuchWindowException, NoSuchElementException) as e:
            print("Something else wen wrong with that page", page, emoji.emojize(':beetle: :'), e,
                  "Due to NoSuchWindowException or NoSuchElementException")
            pass
        except (AttributeError, IndexError) as e:
            print("Something else went wrong with that page, again", page, emoji.emojize(':spider: :'), e,
                  "Due to AttributeError")
            pass

    concate_to_df = pd.DataFrame({'appended_content': appended_content,
                                  'appended_links': appended_links,
                                  'appended_webindex': [item for sublist in appended_webindex for item in sublist]})
    date_list = []
    for i in range(0, len(concate_to_df)):
        date_list.append(concate_to_df['appended_content'][i].split('\n')[0])

    title_list = []
    for i in range(len(concate_to_df)):
        title_list.append(concate_to_df['appended_content'][i].split('\n')[1].split(":")[1:])
        # insert empty list with "The title is emtpy"
        if len(title_list[i]) == 0:
            title_list[i] = ['The title is emtpy'.upper()]
        # flat lists in the list
        title_list[i] = ' '.join(map(str, title_list[i]))
    name_list = []
    for i in range(0, len(concate_to_df), 1):
        name_list.append(concate_to_df['appended_content'][i].split('\n')[1].split(":", 1)[0])
    pdf_list = []
    for i in range(0, len(concate_to_df), 1):
        pdf_list.append(concate_to_df['appended_links'][i].replace(".htm", ".pdf"))
    id_list = []
    for i in range(0, len(concate_to_df), 1):
        id_list.append(pdf_list[i].split('/')[-1])
    central_bank_speeches = pd.DataFrame({'Name': name_list,
                                          'Date': pd.to_datetime(date_list),
                                          'Title': title_list,
                                          'Link': appended_links,
                                          'pdf': pdf_list,
                                          'Web Index': [item for sublist in appended_webindex for item in sublist],
                                          'ID': id_list})

    central_bank_speeches.to_csv(r'central_bank_speeches.csv', index=False)





if __name__ == '__main__':scraper()
