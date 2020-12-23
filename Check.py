from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def takeInput():
    return input("Enter Choice")
def start():
    start.driver = webdriver.Chrome(executable_path="D:\Sourav\Python\Chrome\chromedriver.exe")
    start.driver.get("https://www.youtube.com/watch?v=hoNb6HuNmU0")
    video = start.driver.find_element_by_id('movie_player')
    video.send_keys(Keys.SPACE)  

def pares():
    video = start.driver.find_element_by_id('movie_player')
    video.send_keys(Keys.SPACE) 

def another():
    elem = start.driver.find_element_by_xpath('//*[@class="ytp-next-button ytp-button"]')
    elem.click() 
def sikender():
    while(True):
        value = takeInput()
        if(value=="start"):
            start()
        elif(value=="pause" or value=="resume"):
            pares()
        elif(value=="next"):
            another()

sikender()



""" elem = driver.find_element_by_xpath('//*[@class="ytp-next-button ytp-button"]')
elem.click() """
""" video = driver.find_element_by_id('movie_player')
video.send_keys(Keys.SPACE)  """


