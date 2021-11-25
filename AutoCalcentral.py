import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

def access():
    url = "https://auth.berkeley.edu/cas/login?service=https%3A%2F%2Fcalcentral.berkeley.edu%2Fauth%2Fcas%2Fcallback%3Furl%3Dhttps%253A%252F%252Fcalcentral.berkeley.edu%252F"
    username = "jinyun_wang"
    password = "Jin20021024W$"

    driver = webdriver.Chrome()
    driver.get(url)
    u = driver.find_element_by_id("username").send_keys(username)
    p = driver.find_element_by_id("password").send_keys(password+Keys.RETURN)
    print("Loging in to Calcentral\n")
    p = WebDriverWait(driver).until(lambda d: d.find_element_by_class_name("row-label push-label")).click()
    print("Sending Duo Push\n")
    a = WebDriverWait(driver).until(lambda d: d.find_element_by_xpath('//a[@href="'+"/academics"+'"]'))
    print("Successfully Logged in\n")
    driver.get("https://bcsweb.is.berkeley.edu/psc/bcsprd/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_MD_SP_FL.GBL?Action=U&MD=Y&GMenu=SSR_STUDENT_FL&GComp=SSR_START_PAGE_FL&GPage=SSR_START_PAGE_FL&scname=CS_SSR_MANAGE_CLASSES_NAV&AJAXTransfer=y&ICAJAXTrf=true&ICMDListSlideout=true&ucFrom=CalCentral&ucFromText=My%20Academics&ucFromLink=https%3A%2F%2Fcalcentral.berkeley.edu%2Facademics")
    print("Getting Shopping Cart\n")
    WebDriverWait(driver).until(lambda d: d.find_element_by_id("win5divSCC_NAV_TAB_row$3")).click()
    WebDriverWait(driver).until(lambda d: d.find_element_by_id("GRID_TERM_SRC5$0_row_1")).click()
    courses = WebDriverWait(driver).until(lambda d: d.find_elements_by_class_name("ps-checkbox"))
    print("Enrolling")
    for c in courses:
        c.click()
        print(" "+c.text)
    print("\n")
    WebDriverWait(driver).until(lambda d: d.find_element_by_class_name("DERIVED_SSR_FL_SSR_ENROLL_FL")).click()
    WebDriverWait(driver).until(lambda d: d.find_element_by_class_name("ps_box-button psc_yes")).click()


if __name__ == "__main__":
    access() 
    
    

