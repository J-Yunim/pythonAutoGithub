import sys
import os
from selenium import webdriver

path = "/Users/jinyunwang/Documents/Projects/"
browser = webdriver.Chrome()
browser.get("http://github.com/login")

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path+folderName)
    python_button = browser.find_element_by_xpath("//*[@id='login_field']")[0]
    python_button.send_keys('J-Yunim')
    python_button = browser.find_element_by_xpath("//*[@id='password']")[0]
    python_button.send_keys('jin20021024')
    python_button = browser.find_element_by_xpath("//*[@id='login']/form/div[4]/input[12]")[0]
    python_button.click()
    browser.get("https://github.com/new")
    python_button = browser.find_element_by_xpath("//*[@id='repository_name']")
    python_button.send_keys(folderName)
    python_button = browser.find_element_by_xpath("//*[@id='new_repository']/div[4]/button")
    python_button.click()
    browser.quit()

if __name__ == "__main__":
    create()