import pyttsx3
import datetime
import webbrowser
import speech_recognition as sr
import looseversion
import wikipedia
import time
import pyautogui as pg



def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()



def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning, Suryakumar ")
    if hour >= 12 and hour < 18:
        speak("Good After Noon, Suryakumar")
    else :
        speak("Good Evening, Suryakumar")
        
    speak("Im Jarvis, How Can I Help You Today Sir?")
        
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        if 'open youtube' in query:
            speak("Opening Youtube")
            time.sleep(0.8)
            webbrowser.open("www.youtube.com")
            
        elif 'open google' in query:
            speak("Opening Google")
            time.sleep(0.8)
            webbrowser.open("www.google.com")
            
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        if 'search this' in query:
            time.sleep(3)
            pg.write(query.replace("search this" , " "))
            
            pg.press("enter")
            
            
        
            
            