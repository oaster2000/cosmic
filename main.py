import pyaudio,os
import speech_recognition as sr
import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate',175)
engine.setProperty('voice', voices[2].id)

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
        engine.setProperty('rate', 175)
        return True
    except:
        t = "Sorry I couldn't understand and handle this input"
        print(t)
        return False
        
def tell_time():
    try:
        time = datetime.datetime.now().strftime("%H:%M:%S")
    except Exception as e:
        print(e)
        time = False
    return time
    
def open(option):
    if "excel" in option.casefold():
        excel()
    elif "internet" in option.casefold():
        internet()
    elif "music" in option.casefold():
        media()
    else:
        speak("Nothing could be found sir.")

def excel():
        os.system("start excel.exe")

def internet():
        os.system("start chrome.exe")

def media():
        os.system("start wmplayer.exe")
        
def exit():
    quit()

def mainfunction(source):
    audio = r.listen(source, phrase_time_limit=60)
    input = ""
    try:
        input = r.recognize_google(audio)
    except:
        pass
    print(input)
    if "cosmic" in input.casefold():
        if "open" in input.casefold():
            open(input)
        elif "shut down"in input.casefold():
            hour = int(datetime.datetime.now().hour)
            if hour>=7 and hour<18:
                speak("Good day")
            else:
                speak("Good night")
            exit()
        
def startup():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = tell_time()
    speak(f"Currently it is {c_time}")
    speak("I am Cosmic. Online and ready. Please tell me how may I help you")
    

if __name__ == "__main__":
    #startup()
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = tell_time()
    speak(f"Currently it is {c_time}")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        engine.say("Initialized and ready to go")
        engine.runAndWait()
        while 1:
            mainfunction(source)