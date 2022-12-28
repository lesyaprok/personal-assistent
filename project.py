import os, sys, re
import speech_recognition as sr
import webbrowser
from gtts import gTTS
from playsound import playsound
from interpreter import get_input, interpreter

mode = "t"

def main():  
    global mode
    mode = choose_mode() 
    username = get_username()
    execute_command(username)


def choose_mode():
    while True:
        try:
            mode = get_mode()
            if (mode == "t" or mode == "v"):
                return mode
            else:
                continue
        except KeyboardInterrupt:
            sys.exit("\nGoodbye :)")


def get_username():
    FIRST_MESSAGE = "Hello! What is your name?\n"   
    print(FIRST_MESSAGE, end="")  
    speak(FIRST_MESSAGE)
    if mode == "v":
        username = user_voice_command()
    else:
        username = input("")
    username = recognize_username(username)
    return username


def greeting(username):
    GREETING_MESSAGE = f"\nHi, {username}! How can I help you?\n" 
    speak(GREETING_MESSAGE)
    return GREETING_MESSAGE + "To print all possible commands please type 'list'"


def get_command():
    try:
        command = get_command_from_user_input("\nCouldn't recognize. Please type here: ")
    except KeyboardInterrupt:
        sys.exit("\nGoodbye :)")    


def execute_command(username):
    print(greeting(username))
    if mode == "v":
        while(True):
            try:
                command = user_voice_command()
                answer = interpreter(command)
                speak(answer)
            except AssertionError:
                continue
    else:
        user_text_command()
 

def user_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        attempt = 1
        while(True):
            try:
                print("\nI'm listening...")
                speech = recognizer.listen(source, timeout = 10)
                command = recognizer.recognize_google(speech)
                print(command.capitalize())
                return command              
            except (sr.WaitTimeoutError, sr.UnknownValueError):
                if attempt == 0:
                    command = get_command()
                    attempt = 1
                    return command
                print("\nCouldn't recognize. Please try again") 
                attempt -= 1
                continue 
            except KeyboardInterrupt:
                speak("Goodbye")
                sys.exit("\nGoodbye :)")          


def user_text_command():
    get_input()


def get_mode():
    mode = get_command_from_user_input("What mode do you prefer: text or voice input? (type t/v) ")
    return mode


def modify_input(string):
    return string.strip().lower()


def get_command_from_user_input(message):
    command = modify_input(input(message))
    return command  
 

def recognize_username(user_input):
    name = re.sub("i'm|i am|my name is ", "", user_input, flags=re.IGNORECASE).strip().capitalize()
    return name or "user"


def speak(message):
    tts = gTTS(message)
    file_name = "sound.mp3"
    tts.save(file_name)
    playsound(file_name)
    os.remove(file_name)
  

if  __name__ == "__main__":
    main()
