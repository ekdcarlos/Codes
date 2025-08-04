import speech_recognition as sr
import pyttsx3
import datetime

# Initialize the TTS engine
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            return command
        except sr.WaitTimeoutError:
            speak("Sorry, I didn't hear anything.")
            return ""
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return ""
        except Exception as e:
            speak("An error occurred. Please try again.")
            print(f"Error: {e}")
            return ""

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. How can I help you?")

def run_jarvis():
    greet()
    while True:
        command = listen()
        if "time" in command:
            now = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {now}")
        elif "stop" in command or "exit" in command:
            speak("Goodbye!")
            break
        elif command:
            speak("I don't understand that command.")

if __name__ == "__main__":
    run_jarvis()