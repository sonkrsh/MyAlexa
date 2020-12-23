import pyttsx3
import speech_recognition as s
import googletrans
import pywhatkit as kit
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import vlc 
import pafy 

options = Options()
options.headless = True

gt = googletrans.Translator()
sr = s.Recognizer()
play=""
with s.Microphone() as m:
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



 