import os, sys, re
import speech_recognition as sr
import webbrowser
from gtts import gTTS
from playsound import playsound


def main():
    username = get_username()
    mode = choose_mode()
    greeting(username)


def get_username():
    FIRST_MESSAGE = "Hello there! What is your name?\n"   
    print(FIRST_MESSAGE, end="")  
    speak(FIRST_MESSAGE)
    username = user_voice_command()
    # username = input().strip().lower()\
    username = re.sub("i'm|i am|my name is ", "", username).strip().capitalize()
    return username or "user"


def choose_mode():
    while True:
        try:
            mode = input("What mode do you prefer: text or voice input? (type t/ v) ").lower().strip()
            if (mode == "t" or mode == "v"):
                return mode
            else:
                continue
        except KeyboardInterrupt:
            sys.exit("Goodbye :)")


def greeting(username):
    GREETING_MESSAGE = f"Hi, {username}! How can I help you?\n" 
    print(GREETING_MESSAGE + "To print all possible commands please type 'list'")
    speak(GREETING_MESSAGE)
    user_voice_command()  

def speak(message):
    tts = gTTS(message)
    file_name = "sound.mp3"
    tts.save(file_name)
    playsound(file_name)
    os.remove(file_name)

def get_command():
    try:
        command = input("Couldn't recognize. Please type here: ").strip().lower()
        return command
    except KeyboardInterrupt:
        sys.exit("Goodbye :)")    

def user_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        attempt = 2
        while(True):
            try:
                print("I'm listening...")
                speech = recognizer.listen(source, timeout = 10)
                command = recognizer.recognize_google(speech)
                print(command.capitalize())
                return command              
            except (sr.WaitTimeoutError, sr.UnknownValueError):
                if attempt == 0:
                    command = get_command()
                    attempt = 2
                    return command
                print("Couldn't recognize. Please try again") 
                attempt -= 1
                continue 
            except KeyboardInterrupt:
                speak("Goodbye")
                sys.exit("Goodbye :)")          


if  __name__ == "__main__":
    main()
