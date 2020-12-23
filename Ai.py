import pyttsx3
import speech_recognition as s
import googletrans
import pywhatkit as kit
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import vlc 
import pafy 
import time

options = Options()
options.headless = True

gt = googletrans.Translator()
sr = s.Recognizer()
play=""

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)

def talk(text):
    engine.say(text)
    engine.runAndWait()
talk('Hello , Sikandar is Your Personal Assistance')
def skip():
    while(start.driver.find_element_by_xpath('//*[@id="skip-button:1a"]/span/button')):
        start.driver.find_element_by_xpath('//*[@id="skip-button:1a"]/span/button').click()
def listener():
    check='true'
    with s.Microphone() as m: 
        i=0
        while(i<=10):
            print('I am Listing......') 
            sr.pause_threshold = 1
            audio = sr.listen(m,timeout=2,phrase_time_limit=8)
            try:
                query = sr.recognize_google(audio,language='en-In')
                print(query)
                text = gt.translate(query,src='en',dest='en')
                query= text.text.lower()
                
                if any(c in query for c in ['sikandar','Bandar','dukandar','secunder','standard','Jitendra','sikander','sikendar','sikender']):
                    i=11
                    query = query.replace('sikandar', '')
                else:
                     talk("Can't Get You Please Try Again")
            except:
                pass
        return query    

def start(command):
    start.driver = webdriver.Chrome(executable_path="D:\Sourav\Python\Chrome\chromedriver.exe")
    start.driver.get('https://www.youtube.com/results?search_query='+command.replace(" ", "+"))
    start.driver.find_element_by_id("img").click()
    #video = start.driver.find_element_by_id('movie_player')
    #video.send_keys(Keys.SPACE)


def pares():
    video = start.driver.find_element_by_id('movie_player')
    video.send_keys(Keys.SPACE) 

def another():
    elem = start.driver.find_element_by_xpath('//*[@class="ytp-next-button ytp-button"]')
    elem.click() 

def sikandar():
    while(True):
        command = listener()
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            start(song)
        elif 'roko' in command:
            pares()
        elif 'dusra' in command:
            another()
        elif 'ignore' in command:
            skip()
        else:
            talk("Can't Get You Please Try Again")

sikandar()
























""" with s.Microphone() as m:
    print('I am Listing......') 
    sr.pause_threshold = 1
    audio = sr.listen(m,timeout=1,phrase_time_limit=5)
    query = sr.recognize_google(audio,language='en-In')
    text = gt.translate(query,src='en',dest='en')
    query= text.text
    print(query)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',150)
    browser = webdriver.Chrome('D:\Sourav\Python\Chrome\chromedriver.exe', chrome_options=options)
    browser.get('https://www.youtube.com/results?search_query='+query.replace(" ", "+"))
    elem = browser.find_element_by_id("thumbnail")
    play = elem.get_attribute('href')
    engine.runAndWait()
    url = play
    video = pafy.new(url) 
    best = video.getbest() 
    media = vlc.MediaPlayer(best.url) 
    media.play() 
    while True:
        pass        


 """
 