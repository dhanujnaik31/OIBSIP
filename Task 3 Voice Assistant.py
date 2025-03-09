import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to get the current date and time
def get_current_datetime():
    now = datetime.datetime.now()
    return now.strftime("%A, %B %d, %Y"), now.strftime("%I:%M %p")

# Function to handle user voice input
def handle_user_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            user_input = r.recognize_google(audio).lower()
            print("User said:", user_input)
            if "date" in user_input or "today" in user_input:
                current_date, _ = get_current_datetime()
                engine.say("Today's date is " + current_date)
                engine.runAndWait()
            elif "time" in user_input or "current time" in user_input:
                _, current_time = get_current_datetime()
                engine.say("The current time is " + current_time)
                engine.runAndWait()
            elif "hello" in user_input or "hi" in user_input:
                engine.say("Hello! How can I assist you today?")
                engine.runAndWait()
            elif "how are you" in user_input:
                engine.say("I'm doing great, thanks for asking! How about you?")
                engine.runAndWait()
            elif "what is your name" in user_input:
                engine.say("My name is Voice Assistant. Nice to meet you!")
                engine.runAndWait()
            elif "bye" in user_input or "goodbye" in user_input:
                engine.say("Goodbye! It was nice chatting with you.")
                engine.runAndWait()
                return False
            elif "open google" in user_input:
                engine.say("Opening Google...")
                engine.runAndWait()
                webbrowser.open("https://www.google.com")
            elif "open youtube" in user_input:
                engine.say("Opening YouTube...")
                engine.runAndWait()
                webbrowser.open("https://www.youtube.com")
            elif "play" in user_input and "youtube" in user_input:
                engine.say("Playing on YouTube...")
                engine.runAndWait()
                song = user_input.replace("play", "").replace("on youtube", "").strip()
                webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
            elif "how was your day" in user_input:
                engine.say("It's been a great day, thanks for asking! I've been chatting with users like you.")
                engine.runAndWait()
            elif "what can you do" in user_input:
                engine.say("I can help with a wide range of tasks, such as telling you the date and time, answering general knowledge questions, and even having a conversation with you.")
                engine.runAndWait()
            elif "tell me a joke" in user_input:
                engine.say("Here's one: Why couldn't the bicycle stand up by itself? Because it was two-tired!")
                engine.runAndWait()
            else:
                engine.say("Sorry, I didn't understand that. Please try again.")
                engine.runAndWait()
        except sr.UnknownValueError:
            engine.say("Sorry, I didn't understand that. Please try again.")
            engine.runAndWait()
        except sr.RequestError:
            engine.say("Sorry, I'm having trouble connecting to the internet. Please try again later.")
            engine.runAndWait()
    return True

# Main loop
engine.say("Hi Dhanuj!")
engine.runAndWait()
while True:
    if not handle_user_input():
        break
