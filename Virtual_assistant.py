import speech_recognition
import pyttsx3
from datetime import date, datetime
ai_ear = speech_recognition.Recognizer()
ai_mouth = pyttsx3.init()
ai_brain = ""
while True :

    with speech_recognition.Microphone() as mic :
        print("AI : I'm listening...")
        audio = ai_ear.listen(mic)
    print("AI is thinking....")
    try :
        you = ai_ear.recognize_google(audio)
    except :
        you = ""
    print("You: " + you)


    if you =="":
        ai_brain = " I can't hear you, please try again"
    elif "hello" in you :
        ai_brain ="hello"
    elif "today" in you :
        today = date.today()
        ai_brain = today.strftime("%B %d, %Y")
    elif you == "current time" :
        now = datetime.now()
        ai_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "time" in you :
        now = datetime.now()
        ai_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "bye" in you :
        ai_brain = "bye, see you"
        print("AI brain: " + ai_brain)
        ai_mouth.say(ai_brain)
        ai_mouth.runAndWait()
        break
    else :
        ai_brain = "I'm so sorry, I can't understand what you just say, please try again"

    print("AI brain: " + ai_brain)
    ai_mouth.say(ai_brain)
    ai_mouth.runAndWait()