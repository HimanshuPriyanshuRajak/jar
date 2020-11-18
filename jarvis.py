import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    elif hour>=18 and hour<21:
        speak("Good Evening")

    else:
        speak("Good Night!")

    speak("I am Jarvis Sir. Please tell me how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-en')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
         query = takeCommand().lower()
         if 'wikipedia' in query:
            speak('Searching Wikipedia, all right')
            query =  query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

         elif 'open youtube' in query:
            speak('sir opening youtube')
            webbrowser.open("youtube.com")

         elif 'open google' in query:
            speak('sir opening google')
            webbrowser.open("google.com")

         elif 'time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"sir ,The time is {strTime}")

         elif 'open code' in query:
             speak('sir opening visual studio code')
             codePath = "C:\\Users\\ad\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
             os.startfile(codePath)

         elif 'open email' in query:
             speak('sir opening gmail')
             webbrowser.open("www.google.com/gmail/")

         elif 'play music' in query:
             music_dir = 'C:\\Users\\Public\\Music\\Sample Music'
             songs = os.listdir(music_dir)
             os.startfile(os.path.join(music_dir, songs[0]))

         elif 'open excel' in query:
             speak('sir opening microsoft office excel')
             codePath = "C:\\Users\\ad\\Desktop\\Microsoft Office Excel 2007"
             os.startfile(codePath)

         elif 'open powerpoint' in query:
             speak('sir opening microsoft office powerpoint')
             codePath = "C:\\Users\\ad\\Desktop\\Microsoft Office PowerPoint 2007"
             os.startfile(codePath)

         elif 'open microsoft edge' in query:
             speak('sir opening microsoft edge')
             codePath = "C:\\Users\\ad\\Desktop\\Microsoft Edge"
             os.startfile(codePath)

         elif 'open notepad' in query:
             speak('sir opening notepad')
             codePath = "C:\\Users\\ad\\Desktop\\Notepad"
             os.startfile(codePath)

         elif 'open python' in query:
             speak('sir opening python')
             codePath = "C:\\Users\\ad\\Desktop\\IDLE (Python 3.8 32-bit)"
             os.startfile(codePath)

         elif 'open calculator' in query:
             speak('sir opening calculator')
             codePath = "C:\\Users\\ad\\Desktop\\Calculator"
             os.startfile(codePath)

         elif 'open chrome' in query:
             speak('sir opening chrome')
             codePath = "C:\\Users\\ad\\Desktop\\chorme"
             os.startfile(codePath)

         elif 'open text' in query:
             speak('sir opening Sublime Text 3')
             codePath = "C:\\Users\\ad\\Desktop\\Sublime Text 3 (2)"
             os.startfile(codePath)

         elif 'open paint' in query:
             speak('sir opening paint')
             codePath = "C:\\Users\\ad\\Desktop\\Paint"
             os.startfile(codePath)

         elif 'hey jarvis' in query:
             speak('hey sir')

         elif 'thank you jarvis' in query:
             speak('thankyou sir ,have a ice day')

         elif 'open game' in query:
             speak('sir opening game')
             codePath = "D:\\MINI GAME\\BLOCKS"
             os.startfile(codePath)

         elif 'online play' in query:
             speak('sir opening webbrowser games')
             webbrowser.open("www.agame.com/")

         elif 'playlist game' in query:
             speak('sir opening game playlist')
             codePath = "D:\\MINI GAME"
             os.startfile(codePath)

         else:
             speak('sorry sir say that again please')