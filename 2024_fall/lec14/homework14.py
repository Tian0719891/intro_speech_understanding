import datetime
import random
import calendar
from gtts import gTTS

def what_time_is_it(lang, filename):
    """
    Tell me what time it is.
    
    Parameters:
    lang (str) - language in which to speak
    filename (str) - the filename into which the audio should be recorded
    """
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M")  # 24-hour format (e.g., "14:30")
    
    tts = gTTS(f"The time is {time_str}", lang=lang)
    tts.save(filename)


def tell_me_a_joke(lang, audiofile):
    """
    Tell me a joke.
    
    @params:
    lang (str) - language
    audiofile (str) - audiofile in which to record the joke
    """
    jokes = [
        "Why did the chicken cross the road? To get to the other side!",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "Why don’t skeletons fight each other? Because they don’t have the guts!"
    ]
    
    joke = random.choice(jokes)
    
    tts = gTTS(joke, lang=lang)
    tts.save(audiofile)


def what_day_is_it(lang, audiofile):
    """
    Tell me what day it is.
    
    @params:
    lang (str) - language in which to record the date
    audiofile (str) - filename in which to read the date
    
    @returns:
    url (str) - URL that you can look up in order to see the calendar for this month and year
    """
    now = datetime.datetime.now()
    date_str = now.strftime("%A, %B %d, %Y")  # Example: "Monday, January 1, 2024"
    
    tts = gTTS(f"Today is {date_str}", lang=lang)
    tts.save(audiofile)

    calendar_url = f"https://www.timeanddate.com/calendar/?year={now.year}&month={now.month}"
    return calendar_url


def personal_assistant(lang, filename):
    """
    Listen to the user, and respond to one of three types of requests:
    What time is it?
    What day is it?
    Tell me a joke!
    
    @params:
    lang (str) - language
    filename (str) - filename in which to store the result
    """
    print("What would you like to ask? (time / date / joke)")
    user_input = input().strip().lower()

    if user_input in ["time", "what time is it?", "current time"]:
        what_time_is_it(lang, filename)
    elif user_input in ["date", "what day is it?", "today's date"]:
        what_day_is_it(lang, filename)
    elif user_input in ["joke", "tell me a joke"]:
        tell_me_a_joke(lang, filename)
    else:
        tts = gTTS("I'm sorry, I don't understand.", lang=lang)
        tts.save(filename)
