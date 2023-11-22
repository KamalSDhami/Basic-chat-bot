import pyfiglet
from datetime import datetime


def pifi(text):
    print(pyfiglet.figlet_format(text, font="slant"))


def get_time_period():
    current_time = datetime.now().time()

    if (
        current_time >= datetime.strptime("00:00", "%H:%M").time()
        and current_time < datetime.strptime("12:00", "%H:%M").time()
    ):
        return "morning"
    elif (
        current_time >= datetime.strptime("12:00", "%H:%M").time()
        and current_time < datetime.strptime("17:00", "%H:%M").time()
    ):
        return "afternoon"
    elif (
        current_time >= datetime.strptime("17:00", "%H:%M").time()
        and current_time < datetime.strptime("20:00", "%H:%M").time()
    ):
        return "evening"
    else:
        return "night"
    