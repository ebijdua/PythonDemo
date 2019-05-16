import pytest
from selenium import webdriver
import time
import os


@pytest.fixture()
def setUptearDown():
    global driver
    path=os.getcwd()+"\driver\chromedriver.exe"
    driver=webdriver.Chrome(executable_path=path)
    driver.maximize_window()
    driver.get("https://www.google.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield
    driver.close()
    driver.quit()

def test_method1(setUptearDown):
    driver.find_element_by_name('q').send_keys("Blue Prism")
    driver.find_element_by_name('btnK').click()
    time.sleep(2)
    
def test_method2(setUptearDown):
    driver.find_element_by_name('q').send_keys("Uipath")
    driver.find_element_by_name('btnK').click()
    time.sleep(2)