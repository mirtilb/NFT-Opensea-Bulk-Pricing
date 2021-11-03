# GENERAL
import os
import sys
import csv
import json
import time
import traceback
from datetime import datetime
from termcolor import colored

# SELENIUM
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# EXCEPTIONS
from selenium.common.exceptions import TimeoutException

# GLOBAL VARIABLES
BASE_DIR = os.getcwd()
PATH_TO_SYSTEM_FILES = os.path.join( BASE_DIR, "system" )
PATH_TO_CHROME_DRIVER = os.path.join( PATH_TO_SYSTEM_FILES, "drivers", "chromedriver" )
PATH_TO_EXTENSION =  os.path.join( PATH_TO_SYSTEM_FILES, "extensions", "metamask.crx")
PATH_TO_CSV_FILE = os.path.join( BASE_DIR, "assets", "input", "updatePrice.csv" )

# MODULES
def fileExists(path):
    return os.path.exists(path)

def readData(path=PATH_TO_CSV_FILE):
    if not fileExists(path):
        text = colored(f"File at path {path} not found.", "red")
        print(text)
        print("Please add the CSV file and re-run the program to continue.")
        raise SystemExit
    # if file found
    data = list()
    with open(path) as csvFile:
        csvFile = csv.reader(csvFile, delimiter=',')
        line_count = 0
        for row in csvFile:
            if line_count == 0:
                # Skip the headers
                # print(f"Header/Column names are {', '.join(row)}")
                line_count = line_count + 1
            else:
                # strip it here of  ' ' to avoid empty linespython
                try:
                    if row[0] and row[1]:
                        data.append({'url': row[0], 'price': row[1]})
                    line_count = line_count + 1
                except:
                    pass
        # print(f"Processed {line_count} lines.")
    return data

def writeData(finalResult):
    # csv header
    fieldnames = ['url', 'price', 'status', 'timestamp', 'case', 'errorType']
    # csv data in finalResult
    if finalResult:
        rows = finalResult
        PATH_TO_OUTPUT = os.path.join( BASE_DIR, "assets", "output", f"{ datetime.now().strftime('%d_%m_%Y__%H_%M_%S') }.csv")
        with open(PATH_TO_OUTPUT, 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

def initalizeDriver(path=PATH_TO_CHROME_DRIVER):
    options = Options()
    # prefs = {'profile.managed_default_content_settings.images': 2}
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_experimental_option('prefs', prefs)
    options.add_extension(PATH_TO_EXTENSION)
    driver = webdriver.Chrome(executable_path=path, options=options)
    return driver

def waitForLogin():
    txt = "Please login to OpenSea website."
    color = "green"
    text = colored(txt, color)
    print(text)
    condition = True
    while(condition):
        val = input("Please 'Y/y' key again to continue: ")
        if val == 'Y' or val == 'y':
            condition = False

def continueOrExit():
    val = input("Press any key except Q/q to continue: ")
    if val == 'Q' or val == 'q':
        raise SystemExit

def getElement(waittime, xpath, driver):
    return WebDriverWait(driver, waittime).until(
        EC.presence_of_element_located((By.XPATH, xpath)))

def getElements(waittime, xpath, driver):
    try:
        elem = WebDriverWait(driver, waittime).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath)))
    except TimeoutException:
        elem = None
    except Exception as e:
        elem = None
    finally:
        return elem

# GENERAL CODE
if __name__ == '__main__':
    print("Please execute main.py to run the program.")


# wait for this element
# //footer/a[contains(., 'View Item')]






